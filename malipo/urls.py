from django.urls import path

from . import views

urlpatterns = [
#path('malipo', views.Malipo, name='malipo'),
    path('', views.index, name='malipos'),
    path('malipo/<int:pk>', views.MalipoDetailView.as_view(), name='malipo'),
    
]
