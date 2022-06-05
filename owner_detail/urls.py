from django.urls import path
from . import views

urlpatterns = [ 
    path('ownerlist/', views.owner_list),
    path('owner/<int:id>/', views.owner_detail)
]