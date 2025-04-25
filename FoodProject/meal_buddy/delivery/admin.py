from django.contrib import admin # type: ignore

# Register your models here.
from .models import Customer, Restaurent

admin.site.register(Customer)
admin.site.register(Restaurent)