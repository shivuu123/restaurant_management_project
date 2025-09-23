from django.db import models
from django.contrib.auth.models import User
from home.models import Product

class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_items = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_username}"

class ActiveOrderManager(models.Manager):
    def get_active_order(self):
        return self.filter(status__in=['pending','processing'])