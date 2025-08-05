from django.shortcuts import render

# Create your views here.
def menu_home(request):
    return render(request, 'menu.html')
