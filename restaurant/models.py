from django.db import models

class Restraunt(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    opening_days = model.CharField(
        max_length=100,
        help_text="Comma-separated days (e.g. Mon,Tue,Wed,Thu,Fri,Sat,Sun)"
    )
    def __str__(self):
        return self.name