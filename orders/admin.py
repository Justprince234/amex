from django.contrib import admin
from django.http import HttpResponse
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'order_number', 'first_name', 'phone', 'paid']
    list_filter = ['id','paid', 'state', 'country']
    inlines = [OrderItemInline]