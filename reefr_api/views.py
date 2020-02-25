from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_api_view = [
            'Users HTTP methods as function (get, post, patch, put, delete',
            'Is similar to a traditional Django View',
            'Does other stuff',
            'Mapped manually to URLs'
        ]

        return Response({'message': 'hello', 'an_api_view': an_api_view})

