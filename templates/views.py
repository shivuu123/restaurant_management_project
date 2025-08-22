from django.shortcuts import render
from .models import MenuItem
from .models import RestaurantAddress
from .models import Restaurant

def reservations_view(request):
    return render(request, 'reservations.html')

def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, "menu_list.html", {"menu_items": menu_items, "restaurant_name": "Your Restaurant Name"})

def home(request):
    restaurant = Restaurant.objects.first()
    cart = request.session.get('cart', {})
    total_items = sum(cart.values())

    context = {
        'restaurant': restaurant,
        'total_items': total_items.
    }
    return render(request, 'homepage.html', context)

def add_to_cart(request, item_id):
    cart = request.session.get('cart', {})
    cart[str(item_id)] = cart.get(str(item_id), 0) + 1
    request.session['cart'] = cart
    return redirect('homepage')

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

def homepage(request):
    address = RestaurantAddress.objects.first()
    return render(request, 'homepage.html', {'address': address})
        