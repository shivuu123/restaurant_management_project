import string
import secrets
from django.db import models
from django.core.mail import send_mail
from .models import Order
from django.db.models import Sum

class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.code

def generate_coupon_code(length=10):
    """
    Generate a unique alphanumeric coupon code.
    :param length: Length of the generated code (default: 10)
    :return: A unique coupon code string
    """
    characters = string.ascii_uppercase + string.digits

    while True:
        code = ''.join(secrets.choice(characters) for _ in range(length))
        if not Coupon.objects.filter(code=code).exists():
            return code



def generate_unique_order_id(length=8):
    """
    Generate a unique short alphanumeric ID for an order.
    Ensures no collisions in the database.
    """

    alphabet = string.ascii_uppercase + string.digits
    while True:
        new_id = ''.join(secrets.choice(alphabet) for _ in range(length))
        if not Order.objects.filter(unique_id=new_id).exists():
            return new_id

def get_daily_sales_total(d):

    """Return total sales for a given date."""
    
    return Order.objects.filter(created_at__date=d).aggregate(s=Sum("total_price"))["s"] or 0



