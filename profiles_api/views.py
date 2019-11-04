from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """ Test API View """


    serializer_class=serializers.HelloSerializer


    def get(self,request,format=None):
        """ return a list of APIViews features"""
        an_apiview=[
        'Uses Http methods as functions (get,post,patch,put,delete)',
        'similar to traditional django view',
        'defines application logic',
        'is mapped manually to URLs',
        ]
        return Response( {'message':'Hello!', 'an_apiview': an_apiview })


    def post(self,request):
        """ create a hello message with our name """
        serializer=self.serializer_class(data=request.data)
#validate the serializer
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message= f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk=None):
        """ handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """ handle a partial update of the object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """ delete an object """
        return Response({'method':'DELETE'})
