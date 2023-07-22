from django.contrib import admin

from .models import Vehicle_Specification, Contact

# Register your models here.
class Vehicle_SpecificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'make','available')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('name',)
    search_fields = ('name', 'make')
    list_per_page = 25

admin.site.register(Vehicle_Specification, Vehicle_SpecificationAdmin)
admin.site.register(Contact)
