from django.contrib import admin
from .models import *

class itemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'amount', 'distance')
    search_fields = ('name', 'id')

admin.site.register(item, itemAdmin)