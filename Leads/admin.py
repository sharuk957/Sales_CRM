from django.contrib import admin

from .models import Person,Product


admin.site.register(Product)
admin.site.register(Person)
# Register your models here.
