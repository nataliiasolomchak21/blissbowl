from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, verbose_name="Product Name")
    calories = models.IntegerField(verbose_name="Calories")
    weight = models.FloatField(max_length=4, verbose_name="Weight (lbs)")
    preparation_time = models.CharField(
        max_length=50, verbose_name="Preparation Time")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Price")
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = CloudinaryField("image", default="placeholder")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"


class Comment(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=90)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.name} - {self.created_at}'
