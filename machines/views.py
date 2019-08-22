from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .choices import price_choices,  town_choices, machine_e_choices
from django.contrib.auth.models import User
from blog.models import Post
from .models import Machine
from pages.models import Background_image

def machines(request):
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    machines = Machine.objects.order_by('-created_on').filter(is_published=True)

    paginator = Paginator(machines, 10)
    page = request.GET.get('page')
    paged_machines = paginator.get_page(page)    
    context = {
        'background_images':'background_images',
        'machines':paged_machines,
        'posts':posts,
        'machine_e':'machine_e',
        'town_choices': town_choices,
        'price_choices': price_choices,
 
    }
    return render(request, 'machines/machines.html', context)



def machine(request, women_id):
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
    machine = get_object_or_404(Machine, pk=msupplier_id)
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    context = {
        'background_images':background_images,
        'machine': machine,
        'posts':posts,
    }
    return render(request, 'machines/machine.html', context)


# Create your views here.
def findit(request):
  background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
  posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
  queryset_list = Machine.objects.order_by('-created_on')

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

#  Machine
  if 'machine_e' in request.GET:
    machine_e = request.GET['machine_e']
    if machine_e:
      queryset_list = queryset_list.filter(machine_e__iexact=machine_e)

  # service charge
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
        'background_images':'background_images',
        'posts':posts,
        'machine_e_choices': machine_e_choices,
        'town_choices': town_choices,
        'price_choices': price_choices,
        'machines': queryset_list,
        'values': request.GET

  }

  return  render(request, 'machines/findit.html', context)