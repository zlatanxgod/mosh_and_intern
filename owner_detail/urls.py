from django.urls import path
from . import views

urlpatterns = [ 
    path('hello/', views.say_hello),
    path('owner/<int:id>/', views.owner_detail)
]