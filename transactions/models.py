from django.db import models
from  accounts.models import User
from django.utils import timezone
from datetime import timedelta


import uuid

Status = (
    ('Debit', 'Debit'),
    ('Credit', 'Credit')
)

def return_date_time():
    now = timezone.now()
    return now + timedelta(days=1)

# Create your models here.
class History(models.Model):
    user =  models.ForeignKey(User, related_name='history', on_delete=models.CASCADE) 
    description = models.CharField(max_length=100, default="")
    transaction_type = models.CharField(choices=Status, default= "Debit", max_length=10)
    amount = models.DecimalField(default=0, max_digits=50, decimal_places=2)
    transaction_reference = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    date = models.DateField(default=return_date_time)

    class Meta:
        verbose_name_plural = "Histories"