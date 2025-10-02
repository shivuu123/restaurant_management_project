from rest_framework import serializers
from .models import Table
from .models import MenuCategory

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ["table_number", "capacity", "is_available"]

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id', 'name']