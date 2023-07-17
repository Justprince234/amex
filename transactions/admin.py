from django.contrib import admin
from .models import History

# Register your models here.
class HistoryAdmin(admin.ModelAdmin):
    
    list_display = ('id','user', 'transaction_type')
    list_display_links = ('id', 'user')
    search_fields = ('user',)
    list_per_page = 25

admin.site.register(History, HistoryAdmin)