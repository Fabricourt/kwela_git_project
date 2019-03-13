from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contact.models import Sema
from malipo.models import (Malipo, 
                          Malipo_two,
                          Malipo_two, 
                          Malipo_three,
                          Malipo_four,
                          Malipo_five,
                          Malipo_six,
                          Malipo_seven,
                          Malipo_eight,
                          Malipo_nine,
                          Malipo_ten,
                          Malipo_eleven,
                          Malipo_twelve
)



def register(request):
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
    return render(request, 'accounts/register.html')


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('listings')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('accounts/login')
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')



def dashboard(request):
  user_contact = Sema.objects.order_by('-contact_date').filter(user_id=request.user.id)
  user_malipo = Malipo.objects.order_by('-account_date').filter(user=request.user, is_published=True)
  user_malipo_two = Malipo_two.objects.order_by('-account_date').filter(user=request.user, is_published=True)
  user_malipo_three = Malipo_three.objects.order_by('-account_date').filter(user=request.user, is_published=True)
  user_malipo_four = Malipo_four.objects.order_by('-account_date').filter(user=request.user, is_published=True)
  user_malipo_five = Malipo_five.objects.order_by('-account_date').filter(user=request.user, is_published=True)
  user_malipo_six = Malipo_six.objects.order_by('-account_date').filter(user=request.user, is_published=True)
  user_malipo_seven = Malipo_seven.objects.order_by('-account_date').filter(user=request.user, is_published=True)
  user_malipo_eight = Malipo_eight.objects.order_by('-account_date').filter(user=request.user, is_published=True)
  user_malipo_nine = Malipo_nine.objects.order_by('-account_date').filter(user=request.user, is_published=True)
  user_malipo_ten = Malipo_ten.objects.order_by('-account_date').filter(user=request.user, is_published=True)
  user_malipo_eleven = Malipo_eleven.objects.order_by('-account_date').filter(user=request.user, is_published=True)
  user_malipo_twelve = Malipo_twelve.objects.order_by('-account_date').filter(user=request.user, is_published=True)


  context = {
  'contact': user_contact,
  'malipo': user_malipo,
  'malipo_two': user_malipo_two,
  'malipo_three': user_malipo_three,
  'malipo_four': user_malipo_four,
  'malipo_five': user_malipo_five,
  'malipo_six': user_malipo_six,
  'malipo_seven': user_malipo_seven,
  'malipo_eight': user_malipo_eight,
  'malipo_nine': user_malipo_nine,
  'malipo_ten': user_malipo_ten,
  'malipo_eleven': user_malipo_eleven,
  'malipo_twelve': user_malipo_twelve

 
}
  return render(request, 'accounts/dashboard.html', context)
  


