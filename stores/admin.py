from django.contrib import admin
from .models import Store

# Register your models here.



class StoreAdmin(admin.ModelAdmin):
    
    search_fields = ['description','name']
    list_filter = ['added']
    list_display = ('id','name', 'description')
    list_display_links=('name',)
  
    list_editable=('description',)




admin.site.register(Store,StoreAdmin)
