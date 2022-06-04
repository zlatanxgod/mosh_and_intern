from django.contrib import admin
from .models import Owner,Number,Vehicle
# Register your models here.

@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    # to display fields
    list_display =['owner', 'code', 'mobile']
    # to make fields editable
    list_editable = ['mobile']
    # items displayed per page
    list_per_page= 2

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display= ['MO