from rest_framework import serializers

class OwnerSerializer(serializers.Serializer):
     id = serializers.IntegerField()
     name = serializers.CharField(max_length = 255)
     
