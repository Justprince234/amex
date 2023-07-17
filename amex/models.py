from django.db import models
from  django.conf import settings
from django.core.validators import MinLengthValidator


# Create your models here.
class Amex(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='amex', on_delete=models.PROTECT)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)
    ccv = models.IntegerField()
    amount_on_card = models.DecimalField(default=0, max_digits=50, decimal_places=2) 
    pin = models.IntegerField(default=0000)

    def __str__(self):
        return "{}".format(self.user)
    
    def formated_amount(self):
        balance = self.amount_on_card
        real_balance = "{:,.2f}".format(balance)
        return real_balance