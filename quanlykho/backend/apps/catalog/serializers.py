from rest_framework import serializers
from .models import Category, Product, Supplier, Partner, Location

class CategorySerializer(serializers.ModelSerializer):
    class Meta: model = Category; fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    class Meta: model = Product; fields = "__all__"

class SupplierSerializer(serializers.ModelSerializer):
    class Meta: model = Supplier; fields = "__all__"

class PartnerSerializer(serializers.ModelSerializer):
    class Meta: model = Partner; fields = "__all__"

class LocationSerializer(serializers.ModelSerializer):
    class Meta: model = Location; fields = "__all__"

class PublicProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    class Meta:
        model = Product
        fields = ["code", "name", "unit", "category_name", "storage_temp"]