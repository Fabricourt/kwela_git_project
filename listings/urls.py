from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('<slug:slug>/', views.snippet_detail),
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    url(r'^listing/$', views.listing, name='listing'),
    
    url(r'(?P<id>\d+)/favourite_listing/$', views.favourite_listing, name="favourite_listing"),
    path('search', views.search, name='search'),
]