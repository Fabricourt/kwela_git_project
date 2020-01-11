from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contact.models import Sema
from django.contrib.admin.views.decorators import staff_member_required
from blog.models import Post
from pages.models import Background_image
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from client_payments.models import Payment



def register(request):
  background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
  posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
  context = {
  'background_images':'background_images',
  'posts':posts,
  }    
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
    return render(request, 'accounts/register.html', context)


def login(request):
  posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
  background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
  context = {
  'background_images':'background_images',
  'posts':posts,
  }
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('accounts/login')
  else:

    return render(request, 'accounts/login.html', context)

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')



def dashboard(request):
    user_contact = Sema.objects.order_by('-contact_date').filter(user_id=request.user.id)
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]

    

    context = {
    'background_images':'background_images',
    'contact': user_contact,
    'posts':posts,
    
    }

    return render(request, 'accounts/dashboard.html', context)
    



class UserPaymentListView(ListView):
    model = Payment
    template_name = 'accounts/dashboard.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'payments'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Payment.objects.filter(user=user).order_by('-date_posted')


class PaymentDetailView(DetailView):
    model = Payment