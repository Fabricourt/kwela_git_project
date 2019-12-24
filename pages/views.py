from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import price_choices, plot_size_choices, location_choices, town_choices,company_choices
from django.contrib.admin.views.decorators import staff_member_required
from testimonials.models import Testimonial
from listings.models import Listing
from realtors.models import Realtor
from blog.models import Post
from abouts.models import About, Proposal, Howtojoin, Faq
from pages.models import Property_link, Link, Background_image
from home.models import Topbar,header_carousel_pics, Footer
from booking.models import Bookspot
from booking.forms import BookspotForm
from django.contrib import messages, auth
from members.models import Member
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    proposals = Proposal.objects.order_by('-reload').filter(is_published=True)[:1]
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    testimonials = Testimonial.objects.order_by('-post_date').filter(is_published=True)[:3]
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    header_carousel_picss = header_carousel_pics.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]

    #property links
    property_links =Property_link.objects.order_by('link_date').filter(is_published=True)

    #construction link
    links = Link.objects.order_by('link_date').filter(is_published=True)
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]

    context = {
        'proposals': proposals,
        'background_images':'background_images',
        'property_links':property_links,
        'topbars': topbars,
        'header_carousel_picss': header_carousel_picss,
        'footers': footers,
        'links': links,
        'posts': posts,
        'listings': listings,
        'town_choices': town_choices,  
        'company_choices': company_choices,
        'location_choices': location_choices,
        'plot_size_choices': plot_size_choices,
        'price_choices': price_choices,
        'testimonials': testimonials,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    abouts = About.objects.order_by('-reload').filter(is_published=True)[:1]
    realtors = Realtor.objects.order_by('-hire_date')
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]

    context = {
        'abouts': abouts,
        'topbars': topbars,
        'footers': footers,
        'posts':posts,
        'background_images':'background_images',        
        'realtors': realtors,
        'town_choices': town_choices,  
        'location_choices': location_choices,
        'company_choices': company_choices,
        'plot_size_choices': plot_size_choices,
        'price_choices': price_choices,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)

def lamu(request):
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]

    context = {
        'background_images':'background_images',        
        'posts':posts
    }
    return render(request, 'pages/lamu.html', context)

def comingsoon(request):
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]

    context = {
        'background_images':'background_images',
        'posts':posts
    }
    return render(request, 'pages/comingsoon.html', context)


def getland(request):
    proposals = Proposal.objects.order_by('-reload').filter(is_published=True)[:1]
    howtojoins = Howtojoin.objects.order_by('-reload').filter(is_published=True)[:1]
    faqs = Faq.objects.order_by('-reload').filter(is_published=True)[:1]
    bookspots = Bookspot.objects.order_by('-timestamp').filter(is_published=True)
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]

    context = {
        'proposals': proposals,
        'faqs': faqs,
        'howtojoins': howtojoins,
        'bookspots': bookspots, 
        'topbars': topbars,
        'footers': footers,
    }
    return render(request, 'pages/getland.html', context) 


def howtojoin(request):
    proposals = Proposal.objects.order_by('-reload').filter(is_published=True)[:1]
    howtojoins = Howtojoin.objects.order_by('-reload').filter(is_published=True)[:1]
    faqs = Faq.objects.order_by('-reload').filter(is_published=True)[:1]
    bookspots = Bookspot.objects.order_by('-timestamp').filter(is_published=True)
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
  

    if request.method == "POST":
        form = BookspotForm(request.POST)

        if form.is_valid():
            form.save()
    else:

        form = BookspotForm()
        messages.success(request, 'Your Booking having sent out successfully')
    
    
  

    context = {
        'faqs': faqs,
        'form': form,
        'howtojoins': howtojoins,
        'bookspots': bookspots, 
        'topbars': topbars,
        'footers': footers,
    }    

    return render(request, 'pages/howtojoin.html', context) 

@login_required
def faq(request):
    proposals = Proposal.objects.order_by('-reload').filter(is_published=True)[:1]
    howtojoins = Howtojoin.objects.order_by('-reload').filter(is_published=True)[:1]
    faqs = Faq.objects.order_by('-reload').filter(is_published=True)[:1]
    bookspots = Bookspot.objects.order_by('-timestamp').filter(is_published=True)
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]

    context = {
        'faqs': faqs,
        'howtojoins': howtojoins,
        'bookspots': bookspots, 
        'topbars': topbars,
        'footers': footers,
    }
    return render(request, 'pages/faq.html', context) 

@login_required
def members(request):
    members = Member.objects.order_by('timestamp').filter(is_published=True)
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]

    
    context = {
        'members': members,
        'topbars': topbars,
        'footers': footers,
    }
    return render(request, 'pages/members.html', context) 

@login_required
def member(request):
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
    members = Member.objects.order_by('-timestamp').filter(is_published=True)
    member = get_object_or_404(Member, pk=member_id)
  
    context = {
        'members': members,
        'topbars': topbars,
        'footers': footers,
    }
    return render(request, 'pages/members.html', context) 

@staff_member_required
def mobile(request):
    return render(request, 'pages/mobile.html') 

@staff_member_required
def tablet(request):
    return render(request, 'pages/tablet.html') 

@staff_member_required
def laptop(request):
    return render(request, 'pages/laptop.html') 