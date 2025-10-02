from rest_framework import serializers
from .models import Table
from .models import MenuCategory
from .models import UserReview

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ["table_number", "capacity", "is_available"]

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id', 'name']

class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields = ['id', 'user', 'menu_item', 'rating', 'comment', 'review_date']
        read_only_fields = ['id', 'review_date', 'user']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

