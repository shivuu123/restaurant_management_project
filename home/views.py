from django.shortcuts import render
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemByCategoryView(APIView):
    def get(self, request):
        category = request.query_params.get('category')
        if not category:
            return Response({"error": "Category is required."}, status=400)
        items = MenuItem.objects.filter(category__name__iexact=category)
        return Response(MenuItemSerializer(items, many=True).data)
