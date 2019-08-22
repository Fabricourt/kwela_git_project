from django.urls import path

from . import views

urlpatterns = [
    path('', views.trucks, name='trucks'),
    path('<int:truck_id>', views.truck, name='truck'),
    path('searchit', views.searchit, name='searchit'),
  
    
]