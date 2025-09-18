from rest_framework import serializers
from .models import MenuCategory

class MenuCategorySerializer(serializers.ModelSerializers):
    class Meta:
        model = MenuCategory
        fields = ['name']