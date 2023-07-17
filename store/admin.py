from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'price', 'available')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Product, ProductAdmin)