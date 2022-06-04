from django.contrib import admin
from .models import Owner,Number,Vehicle
# Register your models here.

@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    # to display fields
    list_display =['owner', 'code', 'mobile', 'Nationality']
    # to make fields editable
    list_editable = ['mobile']
    # items displayed per page
    list_per_page= 5

    def Nationality(self, number):
        if(int(number.code) == 91) :return "Indian"
        else : return "Foreigner"


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display= ['MOdel','owner']

    # for ordering ,customeized arrow in column cell
    ordering = ['MOdel']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display=['name']


#admin.site.register(Number)
#admin.site.register(Vehicle)

