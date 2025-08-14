from django.shortcuts import render
from .models import MenuItem

def reservations_view(request):
    return render(request, 'reservations.html')

def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, "menu_list.html", {"menu_items": menu_items, "restaurant_name": "Your Restaurant Name"})