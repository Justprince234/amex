from django.contrib import admin
from .models import Amex

# Register your models here.
class AmexAdmin(admin.ModelAdmin):

    list_display = ('user', 'amount_on_card')
    list_display_links = ('user',)
    search_fields = ('user',)
    list_per_page = 25

admin.site.register(Amex)