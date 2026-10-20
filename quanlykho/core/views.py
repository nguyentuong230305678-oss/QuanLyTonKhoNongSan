from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import transaction
from django.db.models import Count, Sum
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from datetime import date, timedelta
from decimal import Decimal
import io
import urllib.parse

from .models import (
    RoleChoice, UserProfile, Category, Location, Product, Supplier,
    Partner, Receipt, Batch, Issue, IssueDetail, InventoryAudit,
    AuditDetail, WasteReport, CustomerOrder, CustomerOrderItem
)


def get_user_role(user):
    if not user.is_authenticated:
        return 'PUBLIC'
    try:
        return user.profile.role
    except Exception:
        if user.is_superuser:
            return RoleChoice.ADMIN
        return RoleChoice.STAFF


def login_view(request):
    next_url = request.GET.get('next') or request.POST.get('next')
    if request.user.is_authenticated:
        if next_url:
            return redirect(next_url)
        role = get_user_role(request.user)
        if role == RoleChoice.CUSTOMER:
            return redirect('store')
        return redirect('dashboard')

    if request.method == 'POST':
        u = request.POST.get('username', '').strip()
        p = request.POST.get('password', '').strip()
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            role = get_user_role(user)
            messages.success(request, f"Chào mừng bạn, {user.username}!")
            if next_url:
                return redirect(next_url)
            if role == RoleChoice.CUSTOMER:
                return redirect('store')
            return redirect('dashboard')
        else:
            messages.error(request, "Tên tài khoản hoặc mật khẩu không chính xác.")

    return render(request, 'login.html', {'next': next_url})


def logout_view(request):
    logout(request)
    messages.info(request, "Bạn đã đăng xuất khỏi hệ thống.")
    return redirect('login')


def register_view(request):
    """Đăng ký tài khoản dành riêng cho Khách hàng / Đối tác mua sỉ"""
    if request.user.is_authenticated:
        return redirect('store')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()
        full_name = request.POST.get('full_name', '').strip()
        phone = request.POST.get('phone', '').strip()
        address = request.POST.get('address', '').strip()

        if not (username and password and full_name):
            messages.error(request, "Vui lòng nhập đầy đủ Tên đăng nhập, Mật khẩu và Họ tên!")
        elif password != confirm_password:
            messages.error(request, "Xác nhận mật khẩu không trùng khớp!")
        elif User.objects.filter(username=username).exists():
            messages.error(request, f"Tên đăng nhập '{username}' đã được sử dụng. Vui lòng chọn tên khác!")
        else:
            with transaction.atomic():
                user = User.objects.create_user(username=username, password=password)
                UserProfile.objects.create(
                    user=user,
                    role=RoleChoice.CUSTOMER,
                    full_name=full_name,
                    phone=phone
                )
                # Tự động tạo đối tác khách hàng tương ứng để phục vụ quản lý xuất kho
                Partner.objects.get_or_create(
                    name=full_name,
                    defaults={'phone': phone, 'address': address, 'contact_person': full_name}
                )

                # Tự động đăng nhập
                login(request, user)
                messages.success(request, f"Chúc mừng {full_name}! Bạn đã đăng ký tài khoản khách hàng thành công.")
                return redirect('store')

    return render(request, 'register.html')


def forgot_password_view(request):
    """Tính năng Quên mật khẩu & Đặt lại mật khẩu"""
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        new_password = request.POST.get('new_password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        if not (username and new_password):
            messages.error(request, "Vui lòng nhập Tên tài khoản và Mật khẩu mới!")
        elif new_password != confirm_password:
            messages.error(request, "Xác nhận mật khẩu mới không trùng khớp!")
        else:
            user = User.objects.filter(username=username).first()
            if not user:
                messages.error(request, f"Không tìm thấy tài khoản có tên đăng nhập '{username}'!")
            else:
                user.set_password(new_password)
                user.save()
                messages.success(request, f"Đặt lại mật khẩu cho tài khoản '{username}' thành công! Vui lòng đăng nhập bằng mật khẩu mới.")
                return redirect('login')

    return render(request, 'forgot_password.html')


def dashboard(request):
    role = get_user_role(request.user)
    if role == RoleChoice.CUSTOMER:
        return redirect('store')

    today = date.today()

    # Thống kê số liệu thật từ CSDL
    total_products = Product.objects.filter(is_active=True).count()
    
    # Tổng giá trị tồn kho từ các lô còn tồn
    active_batches = Batch.objects.filter(status='ACTIVE', qty_current__gt=0)
    total_inventory_value = sum(b.qty_current * b.unit_cost for b in active_batches)

    # Phiếu nhập tháng này
    first_day_month = today.replace(day=1)
    receipts_this_month = Receipt.objects.filter(created_at__gte=first_day_month).count()

    month_starts = []
    for months_back in range(5, -1, -1):
        month_index = today.year * 12 + today.month - 1 - months_back
        year, month_index = divmod(month_index, 12)
        month_starts.append(date(year, month_index + 1, 1))

    first_chart_month = month_starts[0]
    receipt_months = {
        (row['created_at__year'], row['created_at__month']): row
        for row in Receipt.objects.filter(created_at__date__gte=first_chart_month)
        .values('created_at__year', 'created_at__month')
        .annotate(count=Count('id'), value=Sum('total_amount'))
    }
    issue_months = {
        (row['created_at__year'], row['created_at__month']): row['count']
        for row in Issue.objects.filter(
            created_at__date__gte=first_chart_month,
            status='COMPLETED',
        )
        .values('created_at__year', 'created_at__month')
        .annotate(count=Count('id'))
    }
    monthly_activity = []
    for month_start in month_starts:
        key = (month_start.year, month_start.month)
        receipt_data = receipt_months.get(key, {})
        monthly_activity.append({
            'label': f'T{month_start.month:02d}',
            'receipt_count': receipt_data.get('count', 0),
            'issue_count': issue_months.get(key, 0),
            'receipt_value': receipt_data.get('value') or Decimal(0),
        })

    max_activity = max(
        (max(month['receipt_count'], month['issue_count']) for month in monthly_activity),
        default=0,
    ) or 1
    activity_axis_mid = max_activity // 2
    for month in monthly_activity:
        month['receipt_height'] = month['receipt_count'] * 100 / max_activity
        month['issue_height'] = month['issue_count'] * 100 / max_activity

    max_receipt_value = max((month['receipt_value'] for month in monthly_activity), default=Decimal(0))
    if max_receipt_value:
        value_trend_points = ' '.join(
            f'{index * 100 / (len(monthly_activity) - 1):.1f},'
            f'{90 - float(month["receipt_value"] / max_receipt_value) * 70:.1f}'
            for index, month in enumerate(monthly_activity)
        )
    else:
        value_trend_points = '0.0,90.0 20.0,90.0 40.0,90.0 60.0,90.0 80.0,90.0 100.0,90.0'

    # Cảnh báo hạn sử dụng (< 7 ngày)
    critical_limit = today + timedelta(days=7)
    expiring_soon_count = active_batches.filter(exp_date__lte=critical_limit).count()

    # Danh sách các lô hàng cận hạn (3 mức: ĐỎ, VÀNG, XANH)
    warning_limit = today + timedelta(days=15)
    critical_batches = active_batches.filter(exp_date__lte=critical_limit).order_by('exp_date')[:5]
    warning_batches = active_batches.filter(exp_date__gt=critical_limit, exp_date__lte=warning_limit).order_by('exp_date')[:5]
    safe_batches = active_batches.filter(exp_date__gt=warning_limit).order_by('exp_date')[:5]

    # Sản phẩm tồn dưới định mức
    low_stock_products = [p for p in Product.objects.filter(is_active=True) if p.is_low_stock][:5]

    # Các hoạt động gần đây
    recent_receipts = Receipt.objects.order_by('-created_at')[:4]
    recent_issues = Issue.objects.order_by('-created_at')[:4]
    new_orders_count = CustomerOrder.objects.filter(order_status='NEW').count()

    context = {
        'role': role,
        'user': request.user,
        'total_products': total_products,
        'total_inventory_value': total_inventory_value,
        'receipts_this_month': receipts_this_month,
        'expiring_soon_count': expiring_soon_count,
        'critical_batches': critical_batches,
        'warning_batches': warning_batches,
        'safe_batches': safe_batches,
        'low_stock_products': low_stock_products,
        'recent_receipts': recent_receipts,
        'recent_issues': recent_issues,
        'new_orders_count': new_orders_count,
        'today': today,
        'monthly_activity': monthly_activity,
        'max_activity': max_activity,
        'activity_axis_mid': activity_axis_mid,
        'value_trend_points': value_trend_points,
    }
    return render(request, 'dashboard.html', context)


# -------------------------------------------------------------
# CỔNG MUA HÀNG CHO KHÁCH & GỢI Ý NÔNG SẢN THEO MÙA
# -------------------------------------------------------------
def store_view(request):
    """Cổng đặt hàng mua sắm trực tuyến cho Khách hàng & Đối tác với gợi ý theo mùa và lọc danh mục"""
    role = get_user_role(request.user)
    season_filter = request.GET.get('season', 'ALL')
    cat_filter = request.GET.get('category', '').strip()
    q = request.GET.get('q', '').strip()

    products = Product.objects.filter(is_active=True).select_related('category', 'supplier')

    if season_filter != 'ALL':
        products = products.filter(season=season_filter)
    if cat_filter:
        products = products.filter(category_id=cat_filter)
    if q:
        products = products.filter(name__icontains=q) | products.filter(code__icontains=q)

    categories = Category.objects.all()
    # Đếm số lượng sản phẩm đang có của từng danh mục
    for c in categories:
        c.product_count = Product.objects.filter(category=c, is_active=True).count()
    total_products_count = Product.objects.filter(is_active=True).count()

    # Xác định mùa hiện tại theo tháng thực tế (hoặc tháng thử nghiệm qua tham số ?month=)
    month_param = request.GET.get('month')
    if month_param and month_param.isdigit() and 1 <= int(month_param) <= 12:
        current_month = int(month_param)
        is_test_month = True
    else:
        current_month = date.today().month
        is_test_month = False

    # Logic phân chia 4 mùa Việt Nam:
    # Tháng 1, 2, 3: Mùa Xuân
    # Tháng 4, 5, 6: Mùa Hạ
    # Tháng 7, 8, 9: Mùa Thu
    # Tháng 10, 11, 12: Mùa Đông
    if current_month in (1, 2, 3):
        current_season = 'SPRING'
        current_season_name = 'Mùa Xuân'
        season_title = f'Mùa Xuân (Tháng 1 - 3 & Đón Tết)'
    elif current_month in (4, 5, 6):
        current_season = 'SUMMER'
        current_season_name = 'Mùa Hạ'
        season_title = f'Mùa Hạ (Tháng 4 - 6 & Trái cây rộ vụ)'
    elif current_month in (7, 8, 9):
        current_season = 'AUTUMN'
        current_season_name = 'Mùa Thu'
        season_title = f'Mùa Thu (Tháng 7 - 9 & Nông sản ngọt lành)'
    else:
        current_season = 'WINTER'
        current_season_name = 'Mùa Đông'
        season_title = f'Mùa Đông (Tháng 10 - 12 & Vụ đông xuân)'

    context = {
        'role': role,
        'products': products,
        'categories': categories,
        'total_products_count': total_products_count,
        'season_filter': season_filter,
        'cat_filter': cat_filter,
        'q': q,
        'current_month': current_month,
        'current_season': current_season,
        'current_season_name': current_season_name,
        'season_title': season_title,
        'is_test_month': is_test_month,
    }
    return render(request, 'store.html', context)


def checkout_view(request):
    """Trang điền thông tin đặt hàng (Chưa hiện QR và chưa hiện phương thức TT - theo đúng yêu cầu)"""
    if not request.user.is_authenticated:
        messages.warning(request, "Vui lòng đăng nhập tài khoản trước khi tiến hành đặt hàng nông sản!")
        return redirect(f"/login/?next={urllib.parse.quote(request.get_full_path())}")

    role = get_user_role(request.user)
    profile = getattr(request.user, 'profile', None)

    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        qty = Decimal(request.GET.get('qty', 1))
        product = get_object_or_404(Product, id=product_id)

        # Tính toán tổng tiền
        total = product.price * qty

        # Mã đặt hàng dự kiến
        order_code = f"DH-{timezone.now().strftime('%Y%m%d%H%M%S')}"

        default_name = (profile.full_name if profile and profile.full_name else request.user.get_full_name()) or request.user.username
        default_phone = profile.phone if profile else ""
        default_address = profile.address if profile else ""

        context = {
            'role': role,
            'product': product,
            'qty': qty,
            'total': total,
            'order_code': order_code,
            'user': request.user,
            'default_name': default_name,
            'default_phone': default_phone,
            'default_address': default_address,
        }
        return render(request, 'checkout.html', context)

    elif request.method == 'POST':
        product_id = request.POST.get('product_id')
        qty = Decimal(request.POST.get('qty', 1))
        order_code = request.POST.get('order_code')
        customer_name = request.POST.get('customer_name')
        customer_phone = request.POST.get('customer_phone')
        shipping_address = request.POST.get('shipping_address')
        note = request.POST.get('note', '')

        product = get_object_or_404(Product, id=product_id)
        total = product.price * qty

        with transaction.atomic():
            # Khởi tạo đơn hàng ở trạng thái PENDING chờ quét QR thanh toán hoặc COD
            order = CustomerOrder.objects.create(
                code=order_code,
                customer=request.user if request.user.is_authenticated else None,
                customer_name=customer_name,
                customer_phone=customer_phone,
                shipping_address=shipping_address,
                payment_method='VIETQR', # Mặc định chuyển sang bước thanh toán quét VietQR
                payment_status='PENDING', # Chờ thanh toán
                order_status='NEW',
                total_amount=total,
                note=note
            )

            CustomerOrderItem.objects.create(
                order=order,
                product=product,
                quantity=qty,
                unit_price=product.price
            )

            # Tự động đồng bộ sang bảng Đối tác/Khách hàng nếu chưa có
            Partner.objects.get_or_create(
                name=customer_name,
                defaults={'phone': customer_phone, 'address': shipping_address}
            )

            messages.success(request, f"Xác nhận đặt hàng thành công! Mã đơn: {order.code}. Quý khách vui lòng quét mã VietQR hoặc chọn phương thức thanh toán.")
            return redirect('order_success', order_id=order.id)


def order_success_view(request, order_id):
    """Trang thanh toán đơn hàng & Hiển thị mã VietQR chính xác bằng số tiền trong đơn hàng"""
    order = get_object_or_404(CustomerOrder, id=order_id)

    # Xử lý khi khách hàng đổi sang COD hoặc xác nhận đã chuyển khoản
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'confirm_transfer':
            order.payment_status = 'PAID'
            order.payment_method = 'VIETQR'
            order.save()
            messages.success(request, f"Đã ghi nhận thông báo chuyển khoản thành công cho đơn hàng {order.code}! Thủ kho sẽ chuẩn bị xuất hàng theo FEFO.")
            return redirect('order_success', order_id=order.id)
        elif action == 'switch_cod':
            order.payment_method = 'COD'
            order.payment_status = 'PENDING'
            order.save()
            messages.success(request, f"Đã chuyển sang hình thức Thanh toán tiền mặt khi nhận hàng (COD) cho đơn hàng {order.code}!")
            return redirect('order_success', order_id=order.id)
        elif action == 'switch_vietqr':
            order.payment_method = 'VIETQR'
            order.payment_status = 'PENDING'
            order.save()
            messages.success(request, f"Đã chuyển sang hình thức Chuyển khoản VietQR cho đơn hàng {order.code}!")
            return redirect('order_success', order_id=order.id)

    # Logic tạo mã VietQR: SỐ TIỀN BẮT BUỘC BẰNG CHÍNH XÁC TỔNG TIỀN ĐƠN HÀNG
    amount = int(order.total_amount)
    account_no = "0901234567"
    bank_id = "MB"  # Ngân hàng Quân Đội MBBank
    account_name = urllib.parse.quote("KHO NONG SAN XANH")
    add_info = urllib.parse.quote(f"THANH TOAN {order.code}")
    qr_url = f"https://img.vietqr.io/image/{bank_id}-{account_no}-compact2.png?amount={amount}&addInfo={add_info}&accountName={account_name}"

    context = {
        'order': order,
        'qr_url': qr_url,
        'amount': amount,
        'account_no': account_no,
        'bank_id': bank_id,
        'account_name': "KHO NONG SAN XANH",
        'add_info': f"THANH TOAN {order.code}",
    }
    return render(request, 'order_success.html', context)


def orders_view(request):
    """Danh sách đơn đặt hàng của khách (Thủ kho/Admin xem để chuẩn bị hàng, Khách xem đơn của mình)"""
    role = get_user_role(request.user)
    if not request.user.is_authenticated:
        return redirect('login')

    if role == RoleChoice.CUSTOMER:
        orders = CustomerOrder.objects.filter(customer=request.user).order_by('-created_at')
    else:
        orders = CustomerOrder.objects.all().order_by('-created_at')

    context = {
        'role': role,
        'orders': orders,
    }
    return render(request, 'orders.html', context)


# -------------------------------------------------------------
# LUỒNG 2: QUẢN LÝ SẢN PHẨM & DANH MỤC & VỊ TRÍ
# -------------------------------------------------------------
def products_view(request):
    role = get_user_role(request.user)
    if role not in (RoleChoice.ADMIN, RoleChoice.WAREHOUSE_MANAGER, RoleChoice.STAFF):
        return redirect('store')

    q = request.GET.get('q', '').strip()
    cat_id = request.GET.get('category', '').strip()

    products = Product.objects.select_related('category', 'supplier').filter(is_active=True)
    if q:
        products = products.filter(name__icontains=q) | products.filter(code__icontains=q)
    if cat_id:
        products = products.filter(category_id=cat_id)

    categories = Category.objects.all()
    locations = Location.objects.all()
    suppliers = Supplier.objects.all()

    # Thêm sản phẩm mới (Quản trị viên và Thủ kho)
    if request.method == 'POST' and role in (RoleChoice.ADMIN, RoleChoice.WAREHOUSE_MANAGER):
        code = request.POST.get('code', '').strip().upper()
        name = request.POST.get('name', '').strip()
        c_id = request.POST.get('category_id')
        supplier_id = request.POST.get('supplier_id')
        unit = request.POST.get('unit', 'kg')
        safety_stock = Decimal(request.POST.get('safety_stock', 50))
        storage_temp = request.POST.get('storage_temp', '2°C - 8°C')
        strategy = request.POST.get('strategy', 'FEFO')
        price = Decimal(request.POST.get('price', 0))
        season = request.POST.get('season', 'ALL_YEAR')
        image_url = request.POST.get('image_url', '').strip()
        origin = request.POST.get('origin', '').strip()
        quality_standard = request.POST.get('quality_standard', 'VietGAP').strip()
        description = request.POST.get('description', '').strip()

        if code and name and c_id:
            cat = get_object_or_404(Category, id=c_id)
            supp = Supplier.objects.filter(id=supplier_id).first() if supplier_id else None
            Product.objects.create(
                code=code, name=name, category=cat, supplier=supp, unit=unit,
                safety_stock=safety_stock, storage_temp=storage_temp,
                strategy=strategy, price=price, season=season,
                image_url=image_url, origin=origin,
                quality_standard=quality_standard, description=description
            )
            messages.success(request, f"Đã thêm nông sản: {name} ({code}) thành công!")
            return redirect('products')

    context = {
        'role': role,
        'products': products,
        'categories': categories,
        'locations': locations,
        'suppliers': suppliers,
        'product_count': Product.objects.filter(is_active=True).count(),
        'category_count': categories.count(),
        'supplier_count': suppliers.count(),
        'q': q,
        'cat_id': cat_id,
        'seasons': Product.SEASON_CHOICES,
    }
    return render(request, 'products.html', context)


def product_detail_view(request, product_id):
    """Chi tiết sản phẩm nông sản với thông tin vùng trồng, tiêu chuẩn, cơ sở nhập và các lô hàng thực tế"""
    role = get_user_role(request.user)
    product = get_object_or_404(Product.objects.select_related('category', 'supplier'), id=product_id)

    today = date.today()
    active_batches = product.batches.filter(status='ACTIVE', qty_current__gt=0).select_related('location').order_by('exp_date')
    related_products = Product.objects.filter(category=product.category, is_active=True).exclude(id=product.id)[:4]

    context = {
        'role': role,
        'product': product,
        'active_batches': active_batches,
        'related_products': related_products,
        'today': today,
    }
    return render(request, 'product_detail.html', context)


# -------------------------------------------------------------
# LUỒNG 3: QUẢN LÝ NHẬP KHO & LÔ HÀNG (BATCH CODE & TEM NHÃN)
# -------------------------------------------------------------
def inbound_view(request):
    role = get_user_role(request.user)
    if role not in (RoleChoice.ADMIN, RoleChoice.WAREHOUSE_MANAGER, RoleChoice.STAFF):
        messages.error(request, "Bạn cần đăng nhập với quyền Thủ kho hoặc Nhân viên để thao tác Nhập kho.")
        return redirect('login')

    receipts = Receipt.objects.select_related('supplier', 'created_by').order_by('-created_at')[:15]
    suppliers = Supplier.objects.all()
    products = Product.objects.filter(is_active=True)
    locations = Location.objects.all()

    # Xử lý Lập phiếu nhập kho & Tự động sinh Lô hàng
    if request.method == 'POST':
        supplier_id = request.POST.get('supplier_id')
        note = request.POST.get('note', '')
        product_id = request.POST.get('product_id')
        qty = Decimal(request.POST.get('qty', 0))
        unit_cost = Decimal(request.POST.get('unit_cost', 0))
        location_id = request.POST.get('location_id')
        mfg_date_str = request.POST.get('mfg_date')
        exp_date_str = request.POST.get('exp_date')

        if not (supplier_id and product_id and qty > 0 and exp_date_str):
            messages.error(request, "Vui lòng nhập đầy đủ thông tin: Nhà cung cấp, Nông sản, Số lượng và Hạn sử dụng!")
        else:
            with transaction.atomic():
                supplier = get_object_or_404(Supplier, id=supplier_id)
                product = get_object_or_404(Product, id=product_id)
                loc = Location.objects.filter(id=location_id).first() if location_id else None

                today_str = timezone.now().strftime('%Y%m%d')
                count_today = Receipt.objects.filter(code__startswith=f"PNK-{today_str}").count() + 1
                receipt_code = f"PNK-{today_str}-{count_today:03d}"

                total_amount = qty * unit_cost
                receipt = Receipt.objects.create(
                    code=receipt_code,
                    supplier=supplier,
                    created_by=request.user,
                    total_amount=total_amount,
                    note=note
                )

                batch_count = Batch.objects.filter(batch_code__startswith=f"LOT-{product.code}").count() + 1
                batch_code = f"LOT-{product.code}-{timezone.now().strftime('%y%m%d')}-{batch_count:02d}"

                mfg_date = date.fromisoformat(mfg_date_str) if mfg_date_str else date.today()
                exp_date = date.fromisoformat(exp_date_str)

                batch = Batch.objects.create(
                    batch_code=batch_code,
                    product=product,
                    receipt=receipt,
                    location=loc,
                    mfg_date=mfg_date,
                    exp_date=exp_date,
                    qty_initial=qty,
                    qty_current=qty,
                    unit_cost=unit_cost,
                    status='ACTIVE'
                )

                messages.success(request, f"Lập phiếu nhập thành công! Đã tạo mã Lô mới: {batch.batch_code} (Số lượng: {qty} {product.unit})")
                return redirect('inbound')

    context = {
        'role': role,
        'receipts': receipts,
        'suppliers': suppliers,
        'products': products,
        'locations': locations,
        'today': date.today().isoformat(),
        'default_exp': (date.today() + timedelta(days=14)).isoformat(),
    }
    return render(request, 'inbound.html', context)


def batches_view(request):
    role = get_user_role(request.user)
    if role not in (RoleChoice.ADMIN, RoleChoice.WAREHOUSE_MANAGER, RoleChoice.STAFF):
        return redirect('login')

    q = request.GET.get('q', '').strip()
    status_filter = request.GET.get('status', 'ACTIVE')

    batches = Batch.objects.select_related('product', 'location', 'receipt').all()
    if status_filter != 'ALL':
        batches = batches.filter(status=status_filter)
    if q:
        batches = batches.filter(batch_code__icontains=q) | batches.filter(product__name__icontains=q)

    context = {
        'role': role,
        'batches': batches,
        'q': q,
        'status_filter': status_filter,
    }
    return render(request, 'batches.html', context)


def barcode_label_view(request, batch_id):
    batch = get_object_or_404(Batch, id=batch_id)
    return render(request, 'barcode_label.html', {'batch': batch})


# -------------------------------------------------------------
# LUỒNG 4: QUẢN LÝ XUẤT KHO THÔNG MINH THEO NGUYÊN TẮC FEFO
# -------------------------------------------------------------
def outbound_view(request):
    role = get_user_role(request.user)
    if role not in (RoleChoice.ADMIN, RoleChoice.WAREHOUSE_MANAGER, RoleChoice.STAFF):
        return redirect('login')

    partners = Partner.objects.all()
    products = Product.objects.filter(is_active=True)
    recent_issues = Issue.objects.select_related('partner', 'created_by').order_by('-created_at')[:15]

    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.GET.get('action') == 'fefo_suggest':
        p_id = request.GET.get('product_id')
        need_qty = Decimal(request.GET.get('quantity', 0))

        product = get_object_or_404(Product, id=p_id)
        today = date.today()

        available_batches = Batch.objects.filter(
            product=product,
            qty_current__gt=0,
            exp_date__gte=today,
            status='ACTIVE'
        ).order_by('exp_date')

        total_avail = sum(b.qty_current for b in available_batches)
        if need_qty > total_avail:
            return JsonResponse({
                'success': False,
                'message': f"Không đủ tồn kho! Nhu cầu xuất: {need_qty} {product.unit}, nhưng tổng tồn khả dụng chỉ còn: {total_avail} {product.unit}."
            }, status=400)

        rem = need_qty
        allocations = []
        for b in available_batches:
            if rem <= 0:
                break
            take = min(b.qty_current, rem)
            allocations.append({
                'batch_id': b.id,
                'batch_code': b.batch_code,
                'exp_date': b.exp_date.strftime('%d/%m/%Y'),
                'qty_current': float(b.qty_current),
                'take_qty': float(take),
                'days_left': (b.exp_date - today).days,
                'location': str(b.location) if b.location else 'Chưa gán',
            })
            rem -= take

        return JsonResponse({
            'success': True,
            'product_name': product.name,
            'total_avail': float(total_avail),
            'allocations': allocations
        })

    if request.method == 'POST':
        partner_id = request.POST.get('partner_id')
        product_id = request.POST.get('product_id')
        total_qty = Decimal(request.POST.get('total_qty', 0))
        unit_price = Decimal(request.POST.get('unit_price', 0))
        note = request.POST.get('note', '')

        batch_ids = request.POST.getlist('batch_id[]')
        take_qtys = request.POST.getlist('take_qty[]')

        if not (partner_id and product_id and total_qty > 0):
            messages.error(request, "Vui lòng chọn đối tác nhận hàng và số lượng xuất!")
        else:
            try:
                with transaction.atomic():
                    partner = get_object_or_404(Partner, id=partner_id)
                    product = get_object_or_404(Product, id=product_id)

                    today_str = timezone.now().strftime('%Y%m%d')
                    count_today = Issue.objects.filter(code__startswith=f"PXK-{today_str}").count() + 1
                    issue_code = f"PXK-{today_str}-{count_today:03d}"

                    total_amount = total_qty * unit_price
                    issue = Issue.objects.create(
                        code=issue_code,
                        partner=partner,
                        created_by=request.user,
                        total_amount=total_amount,
                        note=note
                    )

                    for b_id, q_str in zip(batch_ids, take_qtys):
                        q_take = Decimal(q_str)
                        if q_take > 0:
                            b = get_object_or_404(Batch, id=b_id)
                            if q_take > b.qty_current:
                                raise ValueError(f"Lô {b.batch_code} không đủ số lượng để trừ (cần {q_take}, chỉ còn {b.qty_current})!")
                            
                            b.qty_current -= q_take
                            if b.qty_current == 0:
                                b.status = 'DEPLETED'
                            b.save()

                            IssueDetail.objects.create(
                                issue=issue,
                                batch=b,
                                quantity=q_take,
                                unit_price=unit_price
                            )

                    messages.success(request, f"Xuất kho FEFO thành công! Mã phiếu: {issue.code} (Tổng xuất: {total_qty} {product.unit})")
                    return redirect('issue_detail', issue_id=issue.id)
            except Exception as e:
                messages.error(request, f"Lỗi xuất kho: {str(e)}")

    context = {
        'role': role,
        'partners': partners,
        'products': products,
        'recent_issues': recent_issues,
    }
    return render(request, 'outbound.html', context)


def issue_detail_view(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    return render(request, 'issue_detail.html', {'issue': issue})


# -------------------------------------------------------------
# LUỒNG 5: KIỂM KÊ KHO & GHI NHẬN HAO HỤT HƯ HỎNG
# -------------------------------------------------------------
def audit_view(request):
    role = get_user_role(request.user)
    if role not in (RoleChoice.ADMIN, RoleChoice.WAREHOUSE_MANAGER, RoleChoice.STAFF):
        return redirect('login')

    audits = InventoryAudit.objects.order_by('-audit_date')
    waste_reports = WasteReport.objects.select_related('batch__product').order_by('-report_date')[:15]
    batches = Batch.objects.filter(status='ACTIVE', qty_current__gt=0).select_related('product', 'location')

    if request.method == 'POST' and request.POST.get('form_type') == 'waste':
        b_id = request.POST.get('batch_id')
        waste_qty = Decimal(request.POST.get('quantity', 0))
        reason = request.POST.get('reason', 'DAP_NAT')
        note = request.POST.get('note', '')

        if b_id and waste_qty > 0:
            with transaction.atomic():
                b = get_object_or_404(Batch, id=b_id)
                actual_waste = min(waste_qty, b.qty_current)
                b.qty_current -= actual_waste
                if b.qty_current == 0:
                    b.status = 'DEPLETED'
                b.save()

                today_str = timezone.now().strftime('%Y%m%d')
                cnt = WasteReport.objects.filter(code__startswith=f"PHH-{today_str}").count() + 1
                code = f"PHH-{today_str}-{cnt:03d}"

                WasteReport.objects.create(
                    code=code,
                    batch=b,
                    reported_by=request.user,
                    quantity=actual_waste,
                    reason=reason,
                    note=note
                )
                messages.success(request, f"Đã ghi nhận hao hụt {actual_waste} {b.product.unit} cho lô {b.batch_code} ({reason}) và tự động trừ tồn kho!")
                return redirect('audit')

    context = {
        'role': role,
        'audits': audits,
        'waste_reports': waste_reports,
        'batches': batches,
        'reasons': WasteReport.REASON_CHOICES,
    }
    return render(request, 'audit.html', context)


# -------------------------------------------------------------
# LUỒNG 6: THỐNG KÊ & BÁO CÁO & XUẤT DỮ LIỆU
# -------------------------------------------------------------
def reports_view(request):
    role = get_user_role(request.user)
    if role not in (RoleChoice.ADMIN, RoleChoice.WAREHOUSE_MANAGER):
        messages.error(request, "Chức năng này dành cho Thủ kho và Quản trị viên.")
        return redirect('dashboard')

    today = date.today()
    batches = Batch.objects.select_related('product', 'location').filter(status='ACTIVE')

    critical_list = batches.filter(exp_date__lte=today + timedelta(days=7))
    warning_list = batches.filter(exp_date__gt=today + timedelta(days=7), exp_date__lte=today + timedelta(days=15))
    safe_list = batches.filter(exp_date__gt=today + timedelta(days=15))

    categories = Category.objects.all()
    cat_stats = []
    for c in categories:
        prods = c.products.all()
        c_batches = Batch.objects.filter(product__in=prods, status='ACTIVE')
        val = sum(b.qty_current * b.unit_cost for b in c_batches)
        qty = sum(b.qty_current for b in c_batches)
        cat_stats.append({'name': c.name, 'value': val, 'qty': qty})

    context = {
        'role': role,
        'critical_list': critical_list,
        'warning_list': warning_list,
        'safe_list': safe_list,
        'cat_stats': cat_stats,
        'total_active_batches': batches.count(),
    }
    return render(request, 'reports.html', context)


def partners_view(request):
    role = get_user_role(request.user)
    if role not in (RoleChoice.ADMIN, RoleChoice.WAREHOUSE_MANAGER, RoleChoice.STAFF):
        return redirect('login')

    suppliers = Supplier.objects.all()
    partners = Partner.objects.all()

    if request.method == 'POST' and role in (RoleChoice.ADMIN, RoleChoice.WAREHOUSE_MANAGER):
        ptype = request.POST.get('partner_type')
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        address = request.POST.get('address', '').strip()

        if name:
            if ptype == 'supplier':
                Supplier.objects.create(name=name, phone=phone, address=address)
                messages.success(request, f"Đã thêm Nhà cung cấp: {name}")
            else:
                Partner.objects.create(name=name, phone=phone, address=address)
                messages.success(request, f"Đã thêm Khách mua sỉ: {name}")
            return redirect('partners')

    context = {
        'role': role,
        'suppliers': suppliers,
        'partners': partners,
    }
    return render(request, 'partners.html', context)


def users_view(request):
    role = get_user_role(request.user)
    if role != RoleChoice.ADMIN:
        messages.error(request, "Chỉ Quản trị viên (ADMIN) mới có quyền quản lý người dùng và phân quyền tài khoản!")
        return redirect('dashboard')

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'create':
            username = request.POST.get('username', '').strip()
            password = request.POST.get('password', '').strip()
            full_name = request.POST.get('full_name', '').strip()
            phone = request.POST.get('phone', '').strip()
            address = request.POST.get('address', '').strip()
            user_role = request.POST.get('role', RoleChoice.STAFF)

            if not (username and password):
                messages.error(request, "Vui lòng nhập Tên tài khoản và Mật khẩu!")
            elif User.objects.filter(username=username).exists():
                messages.error(request, f"Tên tài khoản '{username}' đã tồn tại!")
            else:
                u = User.objects.create_user(username=username, password=password)
                UserProfile.objects.create(
                    user=u,
                    role=user_role,
                    full_name=full_name,
                    phone=phone,
                    address=address
                )
                if user_role == RoleChoice.CUSTOMER and full_name:
                    Partner.objects.get_or_create(
                        name=full_name,
                        defaults={'phone': phone, 'address': address}
                    )
                messages.success(request, f"Đã tạo tài khoản '{username}' với vai trò '{user_role}' thành công!")
                return redirect('users')

        elif action == 'update_role':
            user_id = request.POST.get('user_id')
            new_role = request.POST.get('role')
            target_user = get_object_or_404(User, id=user_id)
            if hasattr(target_user, 'profile'):
                target_user.profile.role = new_role
                target_user.profile.save()
            else:
                UserProfile.objects.create(user=target_user, role=new_role)
            messages.success(request, f"Đã cập nhật vai trò tài khoản '{target_user.username}' thành: {target_user.profile.get_role_display()}")
            return redirect('users')

        elif action == 'toggle_status':
            user_id = request.POST.get('user_id')
            target_user = get_object_or_404(User, id=user_id)
            if target_user == request.user:
                messages.error(request, "Bạn không thể tự khóa tài khoản của chính mình!")
            else:
                target_user.is_active = not target_user.is_active
                target_user.save()
                status_label = "Mở khóa / Kích hoạt" if target_user.is_active else "Khóa tài khoản"
                messages.success(request, f"Đã thực hiện: {status_label} cho '{target_user.username}'.")
            return redirect('users')

        elif action == 'reset_password':
            user_id = request.POST.get('user_id')
            new_pwd = request.POST.get('new_password', '').strip()
            target_user = get_object_or_404(User, id=user_id)
            if not new_pwd or len(new_pwd) < 6:
                messages.error(request, "Mật khẩu mới phải có độ dài tối thiểu 6 ký tự!")
            else:
                target_user.set_password(new_pwd)
                target_user.save()
                messages.success(request, f"Đã thiết lập lại mật khẩu thành công cho tài khoản '{target_user.username}'!")
            return redirect('users')

    role_filter = request.GET.get('role', '')
    q = request.GET.get('q', '').strip()

    users = User.objects.select_related('profile').all().order_by('id')
    if role_filter:
        users = users.filter(profile__role=role_filter)
    if q:
        users = users.filter(username__icontains=q) | users.filter(profile__full_name__icontains=q)

    context = {
        'role': role,
        'users': users,
        'roles': RoleChoice.CHOICES,
        'role_filter': role_filter,
        'q': q,
        'total_count': User.objects.count(),
        'active_count': User.objects.filter(is_active=True).count(),
        'admin_count': UserProfile.objects.filter(role=RoleChoice.ADMIN).count(),
        'manager_count': UserProfile.objects.filter(role=RoleChoice.WAREHOUSE_MANAGER).count(),
        'staff_count': UserProfile.objects.filter(role=RoleChoice.STAFF).count(),
        'customer_count': UserProfile.objects.filter(role=RoleChoice.CUSTOMER).count(),
    }
    return render(request, 'users.html', context)


def profile_view(request):
    """Trang thông tin tài khoản cá nhân, cập nhật hồ sơ và đổi mật khẩu cho người dùng"""
    if not request.user.is_authenticated:
        messages.warning(request, "Vui lòng đăng nhập để xem trang thông tin người dùng!")
        return redirect('login')

    role = get_user_role(request.user)
    profile, _ = UserProfile.objects.get_or_create(user=request.user, defaults={'role': role})

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'update_profile':
            full_name = request.POST.get('full_name', '').strip()
            email = request.POST.get('email', '').strip()
            phone = request.POST.get('phone', '').strip()
            address = request.POST.get('address', '').strip()

            request.user.email = email
            request.user.save()

            profile.full_name = full_name
            profile.phone = phone
            profile.address = address
            profile.save()

            messages.success(request, "Cập nhật hồ sơ cá nhân thành công!")
            return redirect('profile')

        elif action == 'change_password':
            old_password = request.POST.get('old_password', '').strip()
            new_password = request.POST.get('new_password', '').strip()
            confirm_password = request.POST.get('confirm_password', '').strip()

            if not request.user.check_password(old_password):
                messages.error(request, "Mật khẩu hiện tại không chính xác!")
            elif len(new_password) < 6:
                messages.error(request, "Mật khẩu mới phải có ít nhất 6 ký tự!")
            elif new_password != confirm_password:
                messages.error(request, "Xác nhận mật khẩu mới không khớp!")
            else:
                request.user.set_password(new_password)
                request.user.save()
                login(request, request.user)
                messages.success(request, "Đổi mật khẩu thành công! Tài khoản của bạn đã được cập nhật an toàn.")
                return redirect('profile')

    user_orders = CustomerOrder.objects.filter(customer=request.user).order_by('-created_at')[:10]
    recent_receipts = Receipt.objects.filter(created_by=request.user).order_by('-created_at')[:5] if role != RoleChoice.CUSTOMER else []

    context = {
        'role': role,
        'profile': profile,
        'user_orders': user_orders,
        'recent_receipts': recent_receipts,
    }
    return render(request, 'profile.html', context)
