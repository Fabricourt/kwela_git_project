from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .choices import price_choices,  town_choices
from django.contrib.auth.models import User
from blog.models import Post
from .models import Msupplier
from pages.models import Background_image

def msuppliers(request):
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    msuppliers = Msupplier.objects.order_by('-created_on').filter(is_published=True)

    paginator = Paginator(msuppliers, 10)
    page = request.GET.get('page')
    paged_msuppliers = paginator.get_page(page)    
    context = {
        'background_images':'background_images',
        'msuppliers':paged_msuppliers,
        'posts':posts,
        'town_choices': town_choices,
        'price_choices': price_choices,
 
    }
    return render(request, 'msuppliers/msuppliers.html', context)



def msupplier(request, women_id):
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
    msupplier = get_object_or_404(Msupplier, pk=msupplier_id)
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    context = {
        'background_images':background_images,
        'msupplier': msupplier,
        'posts':posts,
    }
    return render(request, 'msuppliers/msupplier.html', context)


# Create your views here.
def findus(request):
  background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
  posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
  queryset_list = Women.objects.order_by('-created_on')

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


  # service charge
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
        'background_images':'background_images',
        'posts':posts,
        'town_choices': town_choices,
        'price_choices': price_choices,
        'msuppliers': queryset_list,
        'values': request.GET

  }

  return  render(request, 'msuppliers/findus.html', context)