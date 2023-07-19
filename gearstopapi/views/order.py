"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gearstopapi.models import Order, User

class OrderView(ViewSet):
    """Gear stop order view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single order

        Returns:
            Response -- JSON serialized order
        """
        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist as ex:
            return Response({'message': ex.args[0]},
            status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all orders

        Returns:
            Response -- JSON serialized list of orders
        """
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST requests to get all orders

        Returns:
            Response -- JSON serialized list of orders
        """
        customer_id = User.objects.get(pk=request.data["customerId"])

        order = Order.objects.create(
            is_open=request.data["isOpen"],
            is_shipped=request.data["isShipped"],
            order_total=request.data["orderTotal"],
            payment_method=request.data["paymentMethod"],
            customer_id=customer_id
        )
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests to get all orders

        Returns:
            Response -- JSON serialized list of orders
        """
        order = Order.objects.get(pk=pk)
        order.is_open = request.data["isOpen"]
        order.is_shipped = request.data["isShipped"]
        order.order_total = request.data["orderTotal"]
        order.payment_method = request.data["paymentMethod"]
        customer_id = User.objects.get(pk=request.data["customerId"])
        order.customer_id = customer_id
        order.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle DELETE requests to get all orders

        Returns:
            Response -- JSON serialized list of orders
        """
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class OrderSerializer(serializers.ModelSerializer):
  """JSON serializer for orders"""
  
  class Meta:
      model = Order
      fields = ('id', 'is_open', 'is_shipped', 'order_total', 'payment_method', 'customer_id')
      depth = 1
