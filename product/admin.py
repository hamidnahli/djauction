from django.contrib import admin

from .models import Product, Category, Image


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # pass
    fields = (
        'product_id', 'product_name', 'category', 'product_start_price', 'product_description',
        'product_bid_start_time', 'product_bid_end_time', 'product_end_price',
    )
    readonly_fields = (
        'product_id',
    )


@admin.register(Category)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ProductImageAdmin(admin.ModelAdmin):
    pass
