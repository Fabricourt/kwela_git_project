from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name='catalog'),
    path('propertys/', views.PropertyListView.as_view(), name='propertys'),
    path('property/<int:pk>', views.PropertyDetailView.as_view(), name='property-detail'),
    path('buyers/', views.BuyerListView.as_view(), name='buyers'),
    path('buyer/<int:pk>', views.BuyerDetailView.as_view(), name='buyer-detail'),
    path('owners/', views.OwnerListView.as_view(), name='owners'),
    path('owner/<int:pk>', views.OwnerDetailView.as_view(), name='owner-detail'),
    path('locations/', views.LocationListView.as_view(), name='locations'),
    path('location/<int:pk>', views.LocationDetailView.as_view(), name='location-detail'),
   
]


