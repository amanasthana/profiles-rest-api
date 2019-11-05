from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions



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



#create a model view set
class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profiles """
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()

    authentication_classes= (TokenAuthentication,) # so it becomes a tuple
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields= ('name','email',)

class UserLoginApiView(ObtainAuthToken):
    """ handle creating user authentication tokens """
    renderer_classes= api_settings.DEFAULT_RENDERER_CLASSES
