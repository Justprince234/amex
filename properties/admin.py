from django.contrib import admin

from . models import Property, Contact


admin.site.site_header = 'Pay Everything with AMEX'
admin.site.site_title = 'Pay Everything with AMEX'
admin.site.index_title = 'Pay Everything with AMEX ADMIN'

# Register your models here.
class PropertyAdmin(admin.ModelAdmin):

    list_display = ('title', 'available')
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ('title',)
    search_fields = ('title', 'country')
    list_per_page = 25

admin.site.register(Property, PropertyAdmin)

class ContactAdmin(admin.ModelAdmin):
    
    list_display = ('id','full_name', 'email')
    list_display_links = ('id', 'email')
    search_fields = ('email',)
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)