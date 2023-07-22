from django.contrib import admin

from .models import Customer, Flight_Prices

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('name', 'flight_class', 'paid')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 25
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Flight_Prices)