from django.contrib import admin
from shop.models import Order, Products

# Register your models here.
admin.site.register(Products)
admin.site.register(Order)