from django.contrib import admin
from .models import Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'name', 'price', 'category', 'is_hot','quantity',
    list_filter = 'is_hot',
    search_fields = 'name', 'category__name'
    readonly_fields = 'quantity',
