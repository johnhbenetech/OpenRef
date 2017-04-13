from django.contrib import admin
from .models import Provider, Update


admin.site.register(Update)


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','street_address', 'street_address2', 'city', 'state', 'zipcode', 'created_date','updated_date')
	
	
admin.site.register(Provider, ProviderAdmin)