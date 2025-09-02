from django.shortcuts import render
from datetime import datetime

def home(request):
    opening_hours = {
        "Monday" - "Saturday": "9:00 AM - 10:00 PM",
        "Sunday": "closed"
    }

    return render(request, "home.html", ){
        "current_year": datetime.now().year,
        "opening_hours": opening_hours
    }