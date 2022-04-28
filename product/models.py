from django.db import models
import uuid


class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, editable=False)
    product_name = models.CharField(max_length=250, null=False, blank=False)
    product_category = models.CharField(max_length=150)
    product_start_price = models.FloatField(max_length=10, null=False, blank=False)
    product_description = models.TextField(max_length=500)


class ProductImage(models.Model):
    image_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    image_url = models.CharField(max_length=500)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

