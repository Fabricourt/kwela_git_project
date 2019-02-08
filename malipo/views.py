from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Malipo
from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required


   
def Malipo(request):
     #  Check if user has made inquiry already
      user_malipo = Malipo.objects.all()
      
     
      return redirect('/accounts/payments/')
      Malipo.save()
  




"""
    # Send email
    send_mail(
       'Property Listing Inquiry',
       'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
       'mfalme2030@gmail.com',
       [realtor_email, 'mfalme2030@gmail.com'],
       fail_silently=False
     )

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/listings/'+listing_id)

"""

def index(request):
  malipos = Malipo.objects.order_by('-list_date').filter(is_published=True)
  return render(request, 'malipo/malipos.html')


 
   
class MalipoDetailView(LoginRequiredMixin, generic.DetailView):
    """Generic class-based detail view for a buyer."""
    model = Malipo
