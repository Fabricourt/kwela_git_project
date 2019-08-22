from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .choices import cost_of_ballast_choices,  town_choices
from django.contrib.auth.models import User
from blog.models import Post
from .models import Women


def womens(request):
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    womens = Women.objects.order_by('-created_on').filter(is_published=True)

    paginator = Paginator(womens, 10)
    page = request.GET.get('page')
    paged_womens = paginator.get_page(page)    
    context = {
        'womens':paged_womens,
        'posts':posts,
        'town_choices': town_choices,
        'cost_of_ballast_choices': cost_of_ballast_choices,
 
    }
    return render(request, 'womens/womens.html', context)



def women(request, women_id):
    women = get_object_or_404(Women, pk=women_id)
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    context = {
        'women': women,
        'posts':posts,
    }
    return render(request, 'womens/women.html', context)


# Create your views here.
def find(request):
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
  if 'cost_of_ballast' in request.GET:
    cost_of_ballast = request.GET['cost_of_ballast']
    if cost_of_ballast:
      queryset_list = queryset_list.filter(cost_of_ballast__lte=cost_of_ballast)

  context = {
        'posts':posts,
        'town_choices': town_choices,
        'cost_of_ballast_choices': cost_of_ballast_choices,
        'womens': queryset_list,
        'values': request.GET

  }

  return  render(request, 'womens/find.html', context)