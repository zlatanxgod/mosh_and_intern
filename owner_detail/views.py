from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from owner_detail.models import Owner
# Create your views here.

@api_view()
def say_hello(request):
    # query_set =  Owner.objects.all()
    # #q_object = Owner.objects.get(pk = 2)
    # q_object = Owner.objects.filter(pk=2).first()

    return Response("Hello")

@api_view()
def owner_detail(request, id):
    return Response(id)