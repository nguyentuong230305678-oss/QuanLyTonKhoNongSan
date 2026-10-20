from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date, timedelta


class RoleChoice:
    ADMIN = 'ADMIN'
    WAREHOUSE_MANAGER = 'WAREHOUSE_MANAGER'
    STAFF = 'STAFF'
    CUSTOMER = 'CUSTOMER'
    CHOICES = [
        (ADMIN, 'Quản trị viên'),
        (WAREHOUSE_MANAGER, 'Thủ kho'),
        (STAFF, 'Nhân viên kho'),
        (CUSTOMER, 'Khách hàng / Đối tác mua sỉ'),
    ]



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=30, choices=RoleChoice.CHOICES, default=RoleChoice.STAFF)
    full_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"


class Category(models.Model):
    STORAGE_CHOICES = [
        ('COOL', 'Kho mát (2°C - 8°C)'),
        ('FROZEN', 'Kho đông (-18°C)'),
        ('DRY', 'Kho khô thoáng (15°C - 25°C)'),
    ]
    code = models.CharField(max_length=30, unique=True, default='CAT')
    name = models.CharField(max_length=100, unique=True)
    storage_type = models.CharField(max_length=10, choices=STORAGE_CHOICES, default='COOL')
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Nhóm nông sản'
        verbose_name_plural = 'Nhóm nông sản'

    def __str__(self):
        return self.name


class Location(models.Model):
    zone = models.CharField(max_length=30, help_text="Khu vực (Ví dụ: Khu A, Kho Lạnh 1)")
    shelf = models.CharField(max_length=30, help_text="Kệ (Ví dụ: Kệ 01, Kệ 02)")
    level = models.CharField(max_length=30, help_text="Tầng (Ví dụ: Tầng 1, Tầng 2)")
    note = models.CharField(max_length=150, blank=True)

    class Meta:
        unique_together = ('zone', 'shelf', 'level')
        verbose_name = 'Vị trí kho'
        verbose_name_plural = 'Vị trí kho'

    def __str__(self):
        return f"{self.zone} - {self.shelf} - {self.level}"


class Product(models.Model):
    STRATEGY_CHOICES = [
        ('FEFO', 'FEFO (Hạn gần xuất trước)'),
        ('FIFO', 'FIFO (Nhập trước xuất trước)'),
    ]
    SEASON_CHOICES = [
        ('ALL_YEAR', 'Quanh năm'),
        ('SPRING', 'Mùa Xuân (Tháng 1 - 3)'),
        ('SUMMER', 'Mùa Hạ (Tháng 4 - 6)'),
        ('AUTUMN', 'Mùa Thu (Tháng 7 - 9)'),
        ('WINTER', 'Mùa Đông (Tháng 10 - 12)'),
    ]
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    unit = models.CharField(max_length=20, default='kg')  # kg, tấn, thùng, bó, sọt
    safety_stock = models.DecimalField(max_digits=12, decimal_places=2, default=50.0)
    storage_temp = models.CharField(max_length=50, blank=True, default='2°C - 8°C')
    strategy = models.CharField(max_length=4, choices=STRATEGY_CHOICES, default='FEFO')
    price = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    image_url = models.CharField(max_length=500, blank=True)
    season = models.CharField(max_length=20, choices=SEASON_CHOICES, default='ALL_YEAR')
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True, blank=True, related_name='products', verbose_name="Cơ sở nhập / Nhà cung cấp")
    origin = models.CharField(max_length=150, blank=True, default='Việt Nam', verbose_name="Vùng trồng / Xuất xứ")
    quality_standard = models.CharField(max_length=100, blank=True, default='VietGAP', verbose_name="Tiêu chuẩn chất lượng")
    description = models.TextField(blank=True, verbose_name="Mô tả chi tiết & Hướng dẫn bảo quản")


    class Meta:
        verbose_name = 'Nông sản'
        verbose_name_plural = 'Danh mục nông sản'

    def __str__(self):
        return f"{self.code} - {self.name}"

    @property
    def total_stock(self):
        """Tổng số lượng tồn kho khả dụng hiện tại từ các lô còn hạn"""
        today = date.today()
        batches = self.batches.filter(qty_current__gt=0, exp_date__gte=today)
        return sum(b.qty_current for b in batches)

    @property
    def is_low_stock(self):
        return self.total_stock <= self.safety_stock


class Supplier(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=150)
    contact_person = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Receipt(models.Model):
    code = models.CharField(max_length=50, unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='receipts')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='receipts')
    created_at = models.DateTimeField(default=timezone.now)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.code} ({self.supplier.name})"


class Batch(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Còn tồn'),
        ('DEPLETED', 'Đã xuất hết'),
        ('EXPIRED', 'Đã hết hạn'),
    ]
    batch_code = models.CharField(max_length=50, unique=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='batches')
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, related_name='batches', null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, related_name='batches')
    mfg_date = models.DateField(default=date.today, verbose_name="Ngày sản xuất (MFG)")
    exp_date = models.DateField(verbose_name="Hạn sử dụng (EXP)")
    qty_initial = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Số lượng nhập")
    qty_current = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Số lượng hiện tại")
    unit_cost = models.DecimalField(max_digits=14, decimal_places=2, default=0, verbose_name="Giá nhập")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='ACTIVE')

    class Meta:
        ordering = ['exp_date']
        verbose_name = 'Lô hàng'
        verbose_name_plural = 'Lô hàng'

    def __str__(self):
        return f"{self.batch_code} - {self.product.name} (HSD: {self.exp_date})"

    @property
    def days_to_expiry(self):
        delta = self.exp_date - date.today()
        return delta.days

    @property
    def expiry_level(self):
        days = self.days_to_expiry
        if days < 0:
            return 'EXPIRED'  # Đã quá hạn
        if days <= 7:
            return 'CRITICAL'  # Dưới 7 ngày (Đỏ)
        if days <= 15:
            return 'WARNING'   # 7 - 15 ngày (Vàng)
        return 'SAFE'          # An toàn (>15 ngày)


class Issue(models.Model):
    STATUS_CHOICES = [
        ('COMPLETED', 'Đã xuất kho'),
        ('CANCELLED', 'Đã hủy'),
    ]
    code = models.CharField(max_length=50, unique=True)
    partner = models.ForeignKey(Partner, on_delete=models.PROTECT, related_name='issues')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='issues')
    created_at = models.DateTimeField(default=timezone.now)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='COMPLETED')
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.code} -> {self.partner.name}"


class IssueDetail(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='details')
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT, related_name='issue_details')
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    unit_price = models.DecimalField(max_digits=14, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.issue.code}: {self.batch.batch_code} ({self.quantity})"


class InventoryAudit(models.Model):
    STATUS_CHOICES = [
        ('DRAFT', 'Đang kiểm kê'),
        ('APPROVED', 'Đã cân bằng kho'),
    ]
    code = models.CharField(max_length=50, unique=True)
    conducted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='audits')
    audit_date = models.DateField(default=date.today)
    zone_name = models.CharField(max_length=50, blank=True, verbose_name="Khu vực kiểm kê")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='DRAFT')
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.code} ({self.get_status_display()})"


class AuditDetail(models.Model):
    audit = models.ForeignKey(InventoryAudit, on_delete=models.CASCADE, related_name='details')
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT, related_name='audit_details')
    system_qty = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Tồn sổ sách")
    actual_qty = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Tồn thực tế")
    diff_qty = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Chênh lệch")
    loss_reason = models.CharField(max_length=150, blank=True)

    def save(self, *args, **kwargs):
        self.diff_qty = self.actual_qty - self.system_qty
        super().save(*args, **kwargs)


class WasteReport(models.Model):
    REASON_CHOICES = [
        ('DAP_NAT', 'Dập nát khi vận chuyển / bốc xếp'),
        ('THOI_HONG', 'Biến chất, thối hỏng do nhiệt độ/ẩm'),
        ('QUA_HAN', 'Quá hạn sử dụng'),
        ('HAO_HUT_TU_NHIEN', 'Hao hụt tự nhiên (bốc hơi nước)'),
    ]
    code = models.CharField(max_length=50, unique=True)
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT, related_name='waste_reports')
    reported_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    report_date = models.DateField(default=date.today)
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    reason = models.CharField(max_length=20, choices=REASON_CHOICES, default='DAP_NAT')
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.code}: {self.batch.batch_code} ({self.quantity} kg - {self.get_reason_display()})"


class CustomerOrder(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('VIETQR', 'Chuyển khoản Ngân hàng (Mã VietQR tự động)'),
        ('COD', 'Thanh toán tiền mặt khi nhận hàng (COD)'),
    ]
    PAYMENT_STATUS_CHOICES = [
        ('PENDING', 'Chờ thanh toán'),
        ('PAID', 'Đã thanh toán'),
    ]
    ORDER_STATUS_CHOICES = [
        ('NEW', 'Đơn mới đặt'),
        ('PROCESSING', 'Đang chuẩn bị hàng / Xuất kho FEFO'),
        ('COMPLETED', 'Đã hoàn tất giao hàng'),
        ('CANCELLED', 'Đã hủy đơn'),
    ]

    code = models.CharField(max_length=50, unique=True)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    customer_name = models.CharField(max_length=150, verbose_name="Họ tên người nhận")
    customer_phone = models.CharField(max_length=20, verbose_name="Số điện thoại")
    shipping_address = models.CharField(max_length=255, verbose_name="Địa chỉ nhận hàng")
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='VIETQR')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='PENDING')
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='NEW')
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    created_at = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True, verbose_name="Ghi chú giao hàng")

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Đơn đặt hàng khách hàng'
        verbose_name_plural = 'Đơn đặt hàng khách hàng'

    def __str__(self):
        return f"{self.code} - {self.customer_name} ({self.total_amount:,.0f} đ)"


class CustomerOrderItem(models.Model):
    order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    unit_price = models.DecimalField(max_digits=14, decimal_places=2)
    subtotal = models.DecimalField(max_digits=15, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order.code}: {self.product.name} x {self.quantity}"

