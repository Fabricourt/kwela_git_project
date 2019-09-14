from django.shortcuts import render
from home.models import Footer, Topbar
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from home.models import Topbar, Footer
from.models import Photo

def index(request):
  photos = Photo.objects.order_by('-reload').filter(is_published=True)
  topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
  footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
  paginator = Paginator(photos, 6)
  page = request.GET.get('page')
  paged_photos = paginator.get_page(page)

  context = {
    'photos': paged_photos,
    'topbars': topbars,
    'footers': footers
  }

  return render(request, 'gallerys/photos.html', context)



def photo(request, photo_id):
  photo = get_object_or_404(Photo, pk=photo_id)
  topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
  footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
 
  context = {
    'photo': photo,
    'topbars': topbars,
    'footers': footers
    
  }

  return render(request, 'gallerys/photo.html', context)