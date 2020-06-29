from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
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
# this basically uses our serialiser to validate the input
    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            #name aboce is the name created in the serializer
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """handle partially updating an object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """handle deleting an object"""
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a hello message"""
        a_viewset = [
            "uses actions (list, create, retrievem update partial update)",
            "Automaically maps to URLS using routers",
            "Provides more fnctionality with less code:",
        ]
        return Response({"Message": "hello", "a_viewset": a_viewset})

    def create(self, request):
        """create a new hellow message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=stutus.HTTP_400_BAD_REQUEST
        )

    def retrieve(self, request, pk=None):
        """handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """handle updating an object"""
        return Response ({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})
