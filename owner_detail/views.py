from django.shortcuts import render
from django.http import HttpResponse
from owner_detail.models import Owner
# Create your views here.

def say_hello(request):
    query_set =  Owner.objects.all()
    #q_object = Owner.objects.get(pk = 2)
    q_object = Owner.objects.filter(pk=2).first()

    return HttpResponse("Hello")