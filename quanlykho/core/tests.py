from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import RoleChoice, UserProfile


class DashboardViewTests(TestCase):
    def test_dashboard_renders_inventory_overview(self):
        response = self.client.get(reverse('dashboard'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nông Sản Xanh')
        self.assertContains(response, 'Tổng sản phẩm')
        self.assertContains(response, 'Phiếu nhập và xuất kho')
        self.assertContains(response, 'Giá trị nhập kho')
        self.assertEqual(len(response.context['monthly_activity']), 6)


class WarehousePageTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='warehouse-staff', password='test-password')
        UserProfile.objects.create(user=self.user, role=RoleChoice.STAFF)
        self.client.force_login(self.user)

    def test_product_page_renders_summary_and_inventory_list(self):
        response = self.client.get(reverse('products'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nông sản đang quản lý')
        self.assertContains(response, 'Nhóm nông sản')
        self.assertContains(response, 'Cơ sở cung cấp')
        self.assertContains(response, 'Danh sách nông sản')

    def test_operation_pages_render_with_full_width_form_layout(self):
        for page_name in ('inbound', 'outbound', 'audit'):
            with self.subTest(page=page_name):
                response = self.client.get(reverse(page_name))

                self.assertEqual(response.status_code, 200)
                self.assertContains(response, 'operation-layout')
