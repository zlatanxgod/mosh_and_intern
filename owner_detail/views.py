from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from owner_detail import serializers
from owner_detail.models import Owner
#from .serializers import 
# Create your views here.

@api_view()
def say_hello(request):
    # query_set =  Owner.objects.all()
    # #q_object = Owner.objects.get(pk = 2)
    # q_object = Owner.objects.filter(pk=2).first()
    owner = Owner.objects.all()
    serializer = serializers.OwnerSerializer(owner, many = True)
    return Response(serializer.data)

@api_view()
def owner_detail(request, id):
    owner = Owner.objects.get(pk = id)
    serializer = serializers.OwnerSerializer(owner)
    return Response(serializer.data)