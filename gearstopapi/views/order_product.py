from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gearstopapi.models import OrderProduct, Order, Product

class OrderProductView(ViewSet):
    """Gear Stop Order Products View"""
    
    def create(self, request):
        """POST Order Product"""
        
        order_id = Order.objects.get(pk=request.data["orderId"])
        product_id = Product.objects.get(pk=request.data["productId"])
        order_product = OrderProduct.objects.create(
            order_id = order_id,
            product_id = product_id,
            quantity=request.data["quantity"],
            total=request.data["total"],
        )
        serializer = OrderProductSerializer(order_product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk):
        """GET Single Order Product"""
        
        order_product = OrderProduct.objects.get(pk=pk)
        serializer =OrderProductSerializer(order_product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def list(self, request):
        """GET All Order Products"""

        order_products = OrderProduct.objects.all()
        order_id = request.query_params.get('orderId', None)
        if order_id is not None:
            order_products = order_products.filter(order_id=order_id)
            
        serializer = OrderProductSerializer(order_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk):
        """PUT Order Product"""
        
        order_product = OrderProduct.objects.get(pk=pk)
        order_product.order_id = Order.objects.get(pk=request.data["orderId"])
        order_product.product_id = Product.objects.get(pk=request.data["productId"])
        order_product.quantity = request.data["quantity"]
        order_product.total = request.data["total"]
        order_product.save()
        return Response('Order Product Updated', status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        """DELETE Order Product"""
        
        order_product = OrderProduct.objects.get(pk=pk)
        order_product.delete()
        return Response('Order Product Deleted', status=status.HTTP_204_NO_CONTENT)
      
class OrderProductSerializer(serializers.ModelSerializer):
    """JSON Serializer for Order Products"""
    
    class Meta:
        model = OrderProduct
        fields = ('id', 'order_id', 'product_id', 'quantity', 'total')
        depth = 1
