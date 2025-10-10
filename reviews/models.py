from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Review
from .serializers import ReviewSerializer

class RestaurantReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination

    def get_query(self):
        return Review.objects.filter(restaurant_id=self.kwargs['restaurant_id']).order_by('_created_at')