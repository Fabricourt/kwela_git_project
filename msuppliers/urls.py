from django.urls import path

from . import views

urlpatterns = [
    path('', views.msuppliers, name='msuppliers'),
    path('<int:msupplier_id>', views.msupplier, name='msupplier'),
    path('findus', views.findus, name='findus'),
  
    
]