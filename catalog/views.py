from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import generic

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import  Property, Buyer, Owner, Propertytype, Location, Paymenttype
from django.contrib.auth.decorators import login_required

@login_required
@permission_required('catalog.can_view_buyers')
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_propertys = Property.objects.all().count()
 
    
  
    
    # The 'all()' is implied by default.    
    num_buyers = Buyer.objects.count()
    num_owners = Owner.objects.count()
    num_locations = Location.objects.count()

   

    context = {
        'num_propertys': num_propertys,
        'num_buyers': num_buyers,
        'num_owners': num_owners,
        'num_locations': num_locations,     
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)



class PropertyListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    """Generic class-based view for a list of propertys."""
    model = Property
    paginate_by = 5
    permission_required = 'catalog.can_view'
   
    
class PropertyDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    """Generic class-based detail view for a property."""
    model = Property
    permission_required = 'catalog.can_view'
   

class BuyerListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    """Generic class-based view for a list of buyer."""
    model = Buyer
    paginate_by = 5
    permission_required = 'catalog.can_view'
   
class BuyerDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    """Generic class-based detail view for a buyer."""
    model = Buyer
    permission_required = 'catalog.can_view_buyer'
   
  

class OwnerListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    """Generic class-based view for a list of owners."""
    model = Owner
    paginate_by = 5
    permission_required = 'catalog.can_view_buyer'
   
    
class OwnerDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    """Generic class-based detail view for a owner."""
    model = Owner
    permission_required = 'catalog.can_view'
  


class LocationListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    """Generic class-based view for a list of owners."""
    model = Location
    paginate_by = 5
    permission_required = 'catalog.can_view'
    
class LocationDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    """Generic class-based detail view for a owner."""
    model = Location
    permission_required = 'catalog.can_view'



