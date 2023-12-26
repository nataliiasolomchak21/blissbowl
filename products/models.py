from django.db import models

# Create your models here.
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
    weight = models.FloatField(verbose_name="Weight (lbs)")
    preparation_time = models.CharField(max_length=50, verbose_name="Preparation Time")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Price")
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"