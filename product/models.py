from django.db import models
from django.utils.crypto import get_random_string


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=250, null=False, blank=False)
    product_start_price = models.FloatField(max_length=10, null=False, blank=False)
    product_description = models.TextField(max_length=500)
    product_bid_start_time = models.DateTimeField()
    product_bid_end_time = models.DateTimeField()
    product_end_price = models.FloatField(max_length=10)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.product_name


class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    image_url = models.CharField(max_length=500)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_id
