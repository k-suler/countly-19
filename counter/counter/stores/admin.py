from django.contrib import admin
from .models import Store, Event


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'maxNumberOfCustomers', 'current_number')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('number', 'store', 'date_time')
