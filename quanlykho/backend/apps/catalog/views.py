from rest_framework import viewsets, filters
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from apps.accounts.permissions import role_required
from .models import *
from .serializers import *

class BaseViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            return [IsAuthenticated()]
        return [role_required("ADMIN", "WAREHOUSE_MANAGER")()]

class CategoryViewSet(BaseViewSet):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    search_fields = ["name"]

class ProductViewSet(BaseViewSet):
    queryset = Product.objects.select_related("category").order_by("code")
    serializer_class = ProductSerializer
    search_fields = ["code", "name"]

class SupplierViewSet(BaseViewSet):
    queryset = Supplier.objects.all().order_by("name")
    serializer_class = SupplierSerializer
    search_fields = ["name", "phone"]

class PartnerViewSet(BaseViewSet):
    queryset = Partner.objects.all().order_by("name")
    serializer_class = PartnerSerializer
    search_fields = ["name", "phone"]

class LocationViewSet(BaseViewSet):
    queryset = Location.objects.all().order_by("zone", "shelf", "level")
    serializer_class = LocationSerializer
    search_fields = ["zone", "shelf"]

class PublicProductList(ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = PublicProductSerializer
    queryset = Product.objects.filter(is_active=True).select_related("category")