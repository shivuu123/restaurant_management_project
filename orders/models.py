from django.db import models
from decimal import Decimal
from home.models import MenuItem
from django.contrib.auth.models import User

try:
    from orders.utils import calculate_discount
except ImportError:
    calculate_discount = None


class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_items = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=True)

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    ]

    customer = models.ForeignKey('account.Customer', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    short_id = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return f"Order {self.short_id} - {self.status}"
(
    def get_total_item_count(self):
        return sum(item.quantity for item in self.orderitem_set.all())
        
    @staticmethod
    def calculate_total_price(self):
        return sum((item.price * item.quantity) for item in self.items.all())

    def __str__(self):
        return f"Order #{self.id} - {self.customer_username}"

class ActiveOrderManager(models.Manager):
    def get_active_order(self):
        return self.filter(status__in=['pending','processing'])

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.menu_item.price
        super().save(*args, **kwargs)

class OrderQuerySet(models.QuerySet):
    def with_status(self, status):
        """ Return orders with the given status."""
        return self.filter(status=status)

class OrderManager(models.Manager):
    def get_queryset(self):
        return OrderQuerySet(self.model, using=self._db)

    def pending(self):
        """Shortcut to get all pending orders."""
        return self.get_queryset().with_status('pending')

    def with_status(self, status):
        """Generic filter for any status."""
        return self.get_queryset().with_status(status)

class Order(models.Model):
    def calculate_total(self):
        total = 0
        for item in self.orderitem_set.all():
            price = calculate_discount(item) if calculate_discount else item.unit_price * item.quantity
            total += price
        )
        return round(total, 2)

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)
    valid_from = models.DateField()
    valid_until = models.DateField()

    def __str__(self):
        return f"{self.code} - {self.discount_percentage}%"
