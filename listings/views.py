from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, lot_size_choices, state_choices
from django.contrib.auth.decorators import login_required
from.models import Listing, Logo 

@login_required
def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  
  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'logo': Logo.objects.all(),
    'listings': paged_listings
    
  }

  return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
  

  listing = get_object_or_404(Listing, pk=listing_id)

  context = {
        'logo': Logo.objects.all(),
        'listing': listing
  }


  return render(request, 'listings/listing.html', context)


 
def search(request):
  queryset_list = Listing.objects.order_by('-list_date')

  #keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  
  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)
 
  # lot_size
  if 'lot_size' in request.GET:
    lot_size = request.GET['lot_size']
    if lot_size:
      queryset_list = queryset_list.filter(lot_size__lte=lot_size)

  # price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
        'logo': Logo.objects.all(),
        'state_choices': state_choices,
        'lot_size_choices': lot_size_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET

  }

  return  render(request, 'listings/search.html', context)