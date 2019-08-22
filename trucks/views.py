from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .choices import price_choices,  town_choices, truck_type_choices
from django.contrib.auth.models import User
from blog.models import Post
from .models import Truck, Truck_type
from pages.models import Background_image

def trucks(request):
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    trucks = Truck.objects.order_by('-created_on').filter(is_published=True)

    paginator = Paginator(trucks, 10)
    page = request.GET.get('page')
    paged_trucks = paginator.get_page(page)    
    context = {
        'background_images':background_images,
        'trucks':paged_trucks,
        'posts':posts,
        'truck_type_choices':truck_type_choices,
        'town_choices': town_choices,
        'price_choices': price_choices,
 
    }
    return render(request, 'trucks/trucks.html', context)



def truck(request, truck_id):
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
    truck = get_object_or_404(Truck, pk=truck_id)
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    context = {
        'background_images':background_images,
        'truck': truck,
        'posts':posts,
    }
    return render(request, 'trucks/truck.html', context)


# Create your views here.
def searchit(request):
  background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
  posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
  queryset_list = Truck.objects.order_by('-created_on')

  #keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(about_me__icontains=keywords)

  #keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(name__icontains=keywords)


# Town
  if 'town' in request.GET:
    town = request.GET['town']
    if town:
      queryset_list = queryset_list.filter(town__iexact=town)

#  Truck
  if 'truck_type' in request.GET:
    truck_type = request.GET['truck_type']
    if truck_type:
      queryset_list = queryset_list.filter(truck_type__iexact=truck_type)

  # service charge
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
        'background_images':background_images,
        'posts':posts,
        'truck_type_choices': truck_type_choices,
        'town_choices': town_choices,
        'price_choices': price_choices,
        'trucks': queryset_list,
        'values': request.GET

  }

  return  render(request, 'trucks/searchit.html', context)