from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

import random
import string
import secrets
import uuid

User = get_user_model()

def random_alphanumeric_string(length):
    return ''.join(
        secrets.choice(string.ascii_letters + string.digits)
        for _ in range(length)
    )

def booking():
    print(random_alphanumeric_string(15).upper())

def gen_random_string():
    return str(uuid.uuid4()).replace('-', '')[:15]

def make_gen_random_string():
    print(gen_random_string().upper())


# Create your models here.
class Flight_Prices(models.Model):
    economy_class = models.DecimalField(default=0, max_digits=50, decimal_places=2)
    business_class = models.DecimalField(default=0, max_digits=50, decimal_places=2)
    private_flight = models.DecimalField(default=0, max_digits=50, decimal_places=2)


class Bookings(models.Model):
    """Creates a database instance booking in database."""
    home = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    def __str__(self):
        return self.destination


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='customers')
    booking_reference_number = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    flight_reference_number = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    flight_class = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    passport = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name