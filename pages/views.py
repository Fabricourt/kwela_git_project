from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, plot_size_choices, location_choices, town_choices
from django.contrib.admin.views.decorators import staff_member_required
from testimonials.models import Testimonial
from listings.models import Listing
from realtors.models import Realtor
from blog.models import Post
from abouts.models import About


from django.contrib.auth.decorators import login_required


def index(request):
    abouts = About.objects.order_by('-reload').filter(is_published=True)[:1]
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:8]
    testimonials = Testimonial.objects.order_by('-post_date').filter(is_published=True)[:3]
    posts = Post.objects.order_by('-list_date').filter(is_published=True)[:3]


    context = {
        'abouts': abouts,
        'posts': posts,
        'listings': listings,
        'town_choices': town_choices,  
        'location_choices': location_choices,
        'plot_size_choices': plot_size_choices,
        'price_choices': price_choices,
        'testimonials': testimonials,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'town_choices': town_choices,  
        'location_choices': location_choices,
        'plot_size_choices': plot_size_choices,
        'price_choices': price_choices,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)

def lamu(request):
    return render(request, 'pages/lamu.html')

def comingsoon(request):
    return render(request, 'pages/comingsoon.html')

@staff_member_required
def mobile(request):
    return render(request, 'pages/mobile.html') 

@staff_member_required
def tablet(request):
    return render(request, 'pages/tablet.html') 

@staff_member_required
def laptop(request):
    return render(request, 'pages/laptop.html') 