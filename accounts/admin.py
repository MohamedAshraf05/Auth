from django.contrib import admin
from .models import UserProfile , CustomUser
# Register your models here.

# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ["user" , "id" , "address"]


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username" , "email" , "is_staff" , "is_active"]