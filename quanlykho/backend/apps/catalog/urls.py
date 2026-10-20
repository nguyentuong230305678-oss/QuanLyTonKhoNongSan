from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("products", ProductViewSet)
router.register("suppliers", SupplierViewSet)
router.register("partners", PartnerViewSet)
router.register("locations", LocationViewSet)

urlpatterns = [
    path("public/products/", PublicProductList.as_view()),
    path("", include(router.urls)),
]