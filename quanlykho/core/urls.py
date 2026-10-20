from django.contrib import admin
from django.urls import path
from core.views import (
    login_view, logout_view, register_view, forgot_password_view, dashboard,
    products_view, product_detail_view, inbound_view, batches_view, barcode_label_view, outbound_view,
    issue_detail_view, audit_view, reports_view, partners_view, users_view,
    store_view, checkout_view, order_success_view, orders_view, profile_view
)

urlpatterns = [
    # Xác thực & Tài khoản
    path('', dashboard, name='dashboard'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('forgot-password/', forgot_password_view, name='forgot_password'),
    path('profile/', profile_view, name='profile'),

    # Cổng mua hàng & Thanh toán cho Khách hàng
    path('store/', store_view, name='store'),
    path('public/', store_view, name='public_products'), # Đường dẫn tắt
    path('checkout/', checkout_view, name='checkout'),
    path('order-success/<int:order_id>/', order_success_view, name='order_success'),
    path('orders/', orders_view, name='orders'),

    # Luồng 2: Nông sản & Danh mục & Vị trí
    path('products/', products_view, name='products'),
    path('products/<int:product_id>/', product_detail_view, name='product_detail'),

    # Luồng 3: Nhập kho & Lô hàng & Tem Barcode
    path('inbound/', inbound_view, name='inbound'),
    path('batches/', batches_view, name='batches'),
    path('batches/<int:batch_id>/barcode/', barcode_label_view, name='barcode_label'),

    # Luồng 4: Xuất kho FEFO
    path('outbound/', outbound_view, name='outbound'),
    path('issues/<int:issue_id>/', issue_detail_view, name='issue_detail'),

    # Luồng 5: Kiểm kê & Hao hụt
    path('audit/', audit_view, name='audit'),

    # Quản lý đối tác
    path('partners/', partners_view, name='partners'),

    # Luồng 6: Báo cáo & Thống kê
    path('reports/', reports_view, name='reports'),

    # Luồng 1: Quản trị tài khoản & Role (ADMIN)
    path('users/', users_view, name='users'),

    path('admin/', admin.site.urls),
]
