from rest_framework.views import APIViews
from rest_framework.response import Response
class MenuAPIview(APIView):
    def get(self, request):
        menu = [
            {
            "name": "Margherita Pizza",
            "description": "Classic cheese and tomato pizza with freshbasil.",
            "price": 299
            },
            {
            "name": "Pasta Alfredo",
            "description": "Creamy white sauce pasta with garlic and parmesan.",
            "price": 349
            },
            {
                "name": "Paneer Tikka",
                "description": "Grilled paneer cubes marinated with indian spices.",
                "price": 249
            }
        ]
        return Response(menu)