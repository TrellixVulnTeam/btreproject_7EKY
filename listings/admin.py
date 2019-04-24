from django.contrib import admin

# Register your models here.
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)   #display side filter
    list_editable = ('is_published',)  # helps in editing
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price') #adds search bar
    list_per_page = 25
admin.site.register(Listing,ListingAdmin)
