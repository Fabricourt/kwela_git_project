from django.urls import path

from . import views

urlpatterns = [
    path('', views.womens, name='womens'),
    path('<int:women_id>', views.women, name='women'),
    path('find', views.find, name='find'),
  
    
]