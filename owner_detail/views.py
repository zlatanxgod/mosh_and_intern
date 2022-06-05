from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from owner_detail import serializers
from owner_detail.models import Owner
#from .serializers import 
# Create your views here.

@api_view()
def owner_list(request):
    # query_set =  Owner.objects.all()
    # #q_object = Owner.objects.get(pk = 2)
    # q_object = Owner.objects.filter(pk=2).first()
    queryset = Owner.objects.all()
    serializer = serializers.OwnerSerializer(queryset, many = True)
    return Response(serializer.data)

@api_view()
def owner_detail(request, id):
    owner = get_object_or_404(Owner, pk = id)
    serializer = serializers.OwnerSerializer(owner)
    return Response(serializer.data)