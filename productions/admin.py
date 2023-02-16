from django.contrib import admin
from .models import Products


class ShopAdmin(admin.ModelAdmin):
    list_display = ['title','price','cover']

admin.site.register(Products,ShopAdmin)