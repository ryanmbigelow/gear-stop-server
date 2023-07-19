"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gearstopapi.models import User

class UserView(ViewSet):
    """Gear stop user view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single user

        Returns:
            Response -- JSON serialized user
        """
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]},
            status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all user

        Returns:
            Response -- JSON serialized list of user
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST requests to get all users

        Returns:
            Response -- JSON serialized list of users
        """
        user = User.objects.create(
            first_name=request.data["firstName"],
            last_name=request.data["lastName"],
            uid=request.data["uid"]
        )
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests to get all users

        Returns:
            Response -- JSON serialized list of users
        """
        user = User.objects.get(pk=pk)
        user.first_name = request.data["firstName"]
        user.last_name = request.data["lastName"]
        user.uid = request.data["uid"]
        user.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle DELETE requests to get all users

        Returns:
            Response -- JSON serialized list of users
        """
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class UserSerializer(serializers.ModelSerializer):
  """JSON serializer for orders"""
  
  class Meta:
      model = User
      fields = ('id', 'first_name', 'last_name', 'uid')
      depth = 0
