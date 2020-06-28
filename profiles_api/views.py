from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

#params self - required for different http requests that can be made to the View
#request object which is passed in by the django rest framework and has details of the request being MessageMiddleware
# format - used to add format suffix to end of endpoint url
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function (get, post, pathch, put, delete)',
        'Is similar to a traditional Django View',
        "Gives you the most control over your applicaton logic",
        "Is mapped manually to URLs",
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
