from django.urls import path

from . import views

urlpatterns = [
    path('', views.machines, name='machines'),
    path('<int:machine_id>', views.machine, name='machine'),
    path('findit', views.findit, name='findit'),
  
    
]