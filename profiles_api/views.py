from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test API View """


    def get(self,request,format=None):
        """ return a list of APIViews features"""
        an_apiview=[
        'Uses Http methods as functions (get,post,patch,put,delete)',
        'similar to traditional django view',
        'defines application logic',
        'is mapped manually to URLs',
        ]
        return Response( {'message':'Hello!', 'an_apiview': an_apiview })
