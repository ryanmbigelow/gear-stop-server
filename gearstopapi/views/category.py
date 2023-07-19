"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gearstopapi.models import Category

class CategoryView(ViewSet):
    """Gear stop category view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single category

        Returns:
            Response -- JSON serialized category
        """
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]},
            status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all category

        Returns:
            Response -- JSON serialized list of category
        """
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST requests to get all categories

        Returns:
            Response -- JSON serialized list of categories
        """
        category = Category.objects.create(
            label=request.data["label"]
        )
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests to get all categories

        Returns:
            Response -- JSON serialized list of categories
        """
        category = Category.objects.get(pk=pk)
        category.label = request.data["label"]
        category.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle DELETE requests to get all categories

        Returns:
            Response -- JSON serialized list of categories
        """
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CategorySerializer(serializers.ModelSerializer):
  """JSON serializer for orders"""
  
  class Meta:
      model = Category
      fields = ('id', 'label')
      depth = 0
