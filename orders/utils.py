import string
import secrets
from django.db import models
from django.core.mail import send_email

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

def send_order_confirmation_email(order_id, email, name, amount):
    try:
        send_mail(
            subject=f"Order Confirmation #{order_id}",
            message=f"Hi {name}, your order #{order_id} is confirmed.\nTotal: ${amount}",
            from_email=None,
            recipient_list=[email],
        )
        return True
    except Exception:
        return False

