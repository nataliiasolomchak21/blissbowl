from django.contrib import admin
from .models import Product, Category, Comment


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image'
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'text',
        'created_at',
    )


admin.site.register(Comment, CommentAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
