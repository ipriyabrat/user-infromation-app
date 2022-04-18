from django.contrib import admin
from testapp.models import UserInfo
# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display=['name','address','mobileno','email','blood_group','Identity_card_number',
    'driving_licence_no','bank_ac_no','creditcard_no','atmcard_no',]

   
admin.site.register(UserInfo,UserInfoAdmin)