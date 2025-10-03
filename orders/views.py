from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .utils import send_email

@api_view(['POST'])
def notify_customer(request):
    recipient = request.data.get('email')
    if not recipient:
        return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
    email_sent = send_email(recipient, "Order Update", "Your order has been shipped!")
    if email_sent is True:
       
        return Response({"message": "Email sent successfully"}, status=status.HTTP_200_OK)
    return Response({"error": "Failed to send email"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def menu_home(request):
    return render(request, 'menu.html')


@api_view(["GET"])
def get_order_status(request, order_id):
    order = Order.objects.filter(id=order_id.first())
    if not order:
        return Response({"error":"Order not found"}, status=404)
    return Response({"order_id": order.id, "status": order.status})
