from django.db import models

class Category(models.Model):
    STORAGE = [("COOL", "Kho mát"), ("FROZEN", "Kho đông"), ("DRY", "Kho khô")]
    name = models.CharField(max_length=100, unique=True)
    storage_type = models.CharField(max_length=10, choices=STORAGE)
    description = models.TextField(blank=True)
    def __str__(self): return self.name

class Product(models.Model):
    STRATEGY = [("FEFO", "FEFO"), ("FIFO", "FIFO")]
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    unit = models.CharField(max_length=20)                      # kg, tấn, thùng
    safety_stock = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    storage_temp = models.CharField(max_length=50, blank=True)  # ví dụ: 2-8°C
    strategy = models.CharField(max_length=4, choices=STRATEGY, default="FEFO")
    price = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    def __str__(self): return f"{self.code} - {self.name}"

class Supplier(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    def __str__(self): return self.name

class Partner(models.Model):          # khách mua sỉ / đối tác
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    def __str__(self): return self.name

class Location(models.Model):
    zone = models.CharField(max_length=30)    # khu
    shelf = models.CharField(max_length=30)   # kệ
    level = models.CharField(max_length=30)   # tầng
    class Meta:
        unique_together = ("zone", "shelf", "level")
    def __str__(self): return f"{self.zone}-{self.shelf}-{self.level}"