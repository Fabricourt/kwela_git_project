from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, lot_size_choices, state_choices

from listings.models import Listing
from realtors.models import Realtor
from pages.models import Photoi, Photoa

def index(request):
    pages = Photoi.objects.order_by('title').filter(is_published=True)[:3]
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'pages': pages,
        'listings': listings,
        'state_choices': state_choices,
        'lot_size_choices': lot_size_choices,
        'price_choices': price_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    pages = Photoa.objects.order_by('title').filter(is_published=True)[:3]
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'pages': pages,
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)