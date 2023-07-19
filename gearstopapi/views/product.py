"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gearstopapi.models import Product, User, Category

class ProductView(ViewSet):
    """Gear stop product view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single product

        Returns:
            Response -- JSON serialized product
        """
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist as ex:
            return Response({'message': ex.args[0]},
            status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all product

        Returns:
            Response -- JSON serialized list of product
        """
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST requests to get all orders

        Returns:
            Response -- JSON serialized list of orders
        """
        category_id = Category.objects.get(pk=request.data["categoryId"])
        seller_id = User.objects.get(pk=request.data["sellerId"])

        product = Product.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            quantity_available=request.data["quantityAvailable"],
            price=request.data["price"],
            category_id=category_id,
            seller_id=seller_id
        )
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests to get all products

        Returns:
            Response -- JSON serialized list of products
        """
        product = Product.objects.get(pk=pk)
        product.title = request.data["title"]
        product.description = request.data["description"]
        product.quantity_available = request.data["quantityAvailable"]
        product.price = request.data["price"]
        category_id = User.objects.get(pk=request.data["categoryId"])
        product.category_id = category_id
        seller_id = User.objects.get(pk=request.data["sellerId"])
        product.seller_id = seller_id
        product.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle DELETE requests to get all products

        Returns:
            Response -- JSON serialized list of products
        """
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ProductSerializer(serializers.ModelSerializer):
  """JSON serializer for orders"""
  
  class Meta:
      model = Product
      fields = ('id', 'title', 'description', 'quantity_available', 'price', 'category_id', 'seller_id')
      depth = 1
