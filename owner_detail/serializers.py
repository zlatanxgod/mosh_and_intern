from rest_framework import serializers

from owner_detail.models import Owner, Number, Vehicle

class OwnerSerializer(serializers.Serializer):
     id = serializers.IntegerField()
     name = serializers.CharField(max_length = 255)
     Number = serializers.PrimaryKeyRelatedField(
         queryset = Number.objects.all()

     )
     faltu_field = serializers.SerializerMethodField(method_name='faltu_method')

     def faltu_method(self, owner: Owner ): #annotation
        return "string"