from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of PIView features"""
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if seralizer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
            seralizer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk=None):
        """Handle updating an object. updates a specific object using that object's primary key(pk)"""
        return Respones({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handles a partial update of an object."""
        return Response({'method': 'PATCH'})

    def delete (self, request, pk=None):
        """Deletes an object"""
        return Response({'method': 'DELETE'})
