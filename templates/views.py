from django.shortcuts import render
from .models import MenuItem

def reservations_view(request):
    return render(request, 'reservations.html')

def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, "menu_list.html", {"menu_items": menu_items, "restaurant_name": "Your Restaurant Name"})

def home(request):
    context = {
        'restaurant_name': settings.restaurant_name
    }
    return render(request, 'homepage.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})

def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'menu.html', {'items': items})
        