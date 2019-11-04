from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """ serializes a name view to test out api view """
    name= serializers.CharField(max_length=20)
