from django.shortcuts import render
from django.views import generic
from . models import Products


class ClothesListView(generic.ListView):
    model = Products
    template_name = 'productions/shop_menu.html'
    context_object_name = 'menu'
    # produce = Products.objects.all()
    # {'produce':produce}