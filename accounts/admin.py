from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    
    list_display = [
        "email",
        "username",
        "first_name",
        "last_name",
        "phone_number",
        "is_staff",
    ]
    
    # tuple: (12, "hello") (cannot change the value)
    # fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("first_name", "last_name", "phone_number")}), )
    # add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("first_name", "last_name", "phone_number")}), )

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
