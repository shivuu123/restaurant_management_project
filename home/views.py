from django.shortcuts import render
from rest_framework.response import APIView
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIview
from .models import Table
from .serializers import TableSerializer

class MenuItemByCategoryView(APIView):
    def get(self, request):
        category = request.query_params.get('category')
        if not category:
            return Response({"error": "Category is required."}, status=400)
        items = MenuItem.objects.filter(category__name__iexact=category)
        return Response(MenuItemSerializer(items, many=True).data)

    
class AvailableTablesAPIView(ListAPIView):
    serializer_class = TableSerializer

    def get_queryset(self):
        return Table.objects.filter(is_available=True)

class TableDetailAPIView(RetrieveAPIview):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
