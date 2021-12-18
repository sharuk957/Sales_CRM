from django.contrib import admin
from .models import Account,Users
from django.contrib.auth.admin import UserAdmin




# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('email', 'name', 'mobile_number', 'company_name', 'role', 'last_login', 'is_admin', 'is_staff', 'is_active', 'date_joined')
    readonly_fields = ('id', 'date_joined', 'last_login')
    ordering = ('-date_joined')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account)
admin.site.register(Users)