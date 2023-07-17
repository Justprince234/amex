from django.db import models
from django.db.models import Sum
from django.conf import settings
import uuid
from django.contrib.auth import get_user_model
from django.urls import reverse
from decimal import Decimal

from store.models import Product

User = get_user_model()

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders')
    order_number = models.CharField(max_length=32, unique=True, null=False, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    amount = models.DecimalField(default=0, max_digits=50, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'

    # def get_absolute_url(self):
    #     return reverse('orders:order_create', args=[self.id])


    def get_total_cost(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total
    
    def formated_amount(self):
        balance = self.get_total_cost
        real_balance = "{:,.2f}".format(balance)
        return real_balance

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def grand_total(self):
        """
        Override the original save method to set the grand total
        if it hasn't been set already.
        """
        final_total = 0
        final_total = Decimal(self.get_total_cost()) + Decimal(self.delivery_cost)
        return final_total

    # def save(self, *args, **kwargs):
    #     self.grand_total = self.amount + self.delivery_cost
    #     super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    

    def get_cost(self):
        return self.price * self.quantity
        
    def __str__(self):
        return f'Owned by {self.order.first_name}, Order number: {self.order.order_number}'
    
    def get_total_item_price(self):
        return self.quantity * self.product.price
    