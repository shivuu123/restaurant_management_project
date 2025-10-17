from django.db import models
from django.contrib.auth.models import User


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.imageField(upload_to='menu_images/', blank=True, null=True)
    is_daily_special = models.BooleanField(default=False)
    availability = models.BooleanField(default=True)
    discount = models.FloatField(default=0.0)
    image_url = models.URLField(blank=True, null=True)
    cuisine_type = models.CharField(max_length=50)

    def get_final_price(self):
        return float(self.price) * (1 - self.discount / 100)

    def __str__(self):
        return self.name
    
    @classmethod
    def filter_by_cuisine(cls, cuisine_type):
        return cls.objects.filter(cuisine_type__iexact=cuisine_type)

class RestaurantLocation(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}, {self.address}, {self.city}, {self.state}, {self.zip_code}"

class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.menu_item.name} - {self.rating}"

class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    table_number = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @classmethod
    def find_available_slots(cls, start, end, slot=timedelta(hours=1)):
        
        """
        Returns a list of available time slots between start and end.
        Each slot is a tuple: (slot_start, slot_end)
        """ 

        booked = cls.objects.filter(start_time__lt=end, end_time__g=start).order_by('start_time')
        free, now = [], start
        for b in booked:
            if now + slot <= b.start_time:
                free.append((now, b.start_time))
            now = max(now, b.end_time)
        if now + slot <= end:
            free.append((now, end))
        return free

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.rating}/5"

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, blank=True, null=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    timezone = models.CharField(max_length=50, default='EST')

    def __str__(self):
        return self.name

    def get_total_menu_items(self):
        """
        Returns the total number of items in the database.
        """
        from .models import MenuItem
        return MenuItem.objects.count()

class OpeningHours(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),

    ]
    day = models.CharField(max_length=10, choices=DAY_CHOICES, unique=True)
    Opening_time = models.TimeField()
    closing_time = models.TimeField()
    def __str__(self):
        return f"(self.day): {self.opening_time} - {self.closing_time}"

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

