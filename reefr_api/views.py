from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from reefr_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_api_view = [
            'Users HTTP methods as function (get, post, patch, put, delete',
            'Is similar to a traditional Django View',
            'Does other stuff',
            'Mapped manually to URLs'
        ]

        return Response({'message': 'hello', 'an_api_view': an_api_view})

    def post(self, request):
        """Create a hello message with a name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(selfs, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle deletion of an object"""
        return Response({'method': 'DELETE'})

