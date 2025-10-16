from django.shortcuts import render
from rest_framework.response import APIView
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIview
from .models import Table
from .serializers import TableSerializer

class MenuItemByCategoryView(APIView):
    def get(self, request, category_id, *args, **kwargs):
        items = MenuItem.objects.filter(category_id=category_id)
        serializer = MenuItemSerializer(items, many=True)
        return Response(serializer.data)
       

    
class AvailableTablesAPIView(ListAPIView):
    serializer_class = TableSerializer

    def get_queryset(self):
        return Table.objects.filter(is_available=True)

class TableDetailAPIView(RetrieveAPIview):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

@api_view(['GET'])
def menu_item_availability(request, pk):
    try:
        item = MenuItem.objects.get(id=pk)
        return Response({"id": item.id, "name": item.name, "available": item.availability})
    except MenuItem.DoesNotExist:
        return Response({"error": "Menu item npt found."}, status=status.HTTP_404_NOT_FOUND)
