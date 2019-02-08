from django.db import models

# Create your models here.
from django.db import models
from django.db import models
from datetime import datetime
from django.urls import reverse # Used to generate URLS by reversing the URL patterns
import uuid # required for unique instances
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from listings.models import Listing
from catalog.models import Buyer,Owner
from realtors.models import Realtor



class Malipo (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)

#Plot Information
    buying_price = models.IntegerField(blank=True, null=True)
    listing = models.ForeignKey(Listing, blank=False, null=True,on_delete=models.DO_NOTHING)
    Plot_no = models.CharField(max_length=200, blank=True, null=True)
    Buyer = models.ForeignKey(Buyer, blank=False, null=True, on_delete=models.DO_NOTHING)
    Owner = models.ForeignKey(Owner, blank=False, null=True, on_delete=models.DO_NOTHING)
    Realtor = models.ForeignKey(Realtor, blank=False, null=True, on_delete=models.DO_NOTHING)
    
  #payment
    account_date =models.DateField(blank=False, null=True)
    reciept_no = models.CharField(max_length=200, blank=True, null=True)
    bankreciept_date = models.DateField(blank=True, null=True)
    bank =  models.CharField(max_length=200, blank=True, null=True)
    bank_branch =  models.CharField(max_length=200, blank=True, null=True)
    bank_agent_no =  models.CharField(max_length=200, blank=True, null=True)
    Amount = models.IntegerField(blank=False, null=True)
    Balance = models.IntegerField(blank=False, null=True)
    description = RichTextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.account_date} {self.Buyer}'

    def get_absolute_url(self):
        """Returns the url to access a particular location instance."""
        return reverse('malipo-detail', args=[str(self.id)])

          
class Malipo_two (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)

#Plot Information
    buying_price = models.IntegerField(blank=True, null=True)
    listing = models.ForeignKey(Listing, blank=False, null=True,on_delete=models.DO_NOTHING)
    Plot_no = models.CharField(max_length=200, blank=True, null=True)
    Buyer = models.ForeignKey(Buyer, blank=False, null=True, on_delete=models.DO_NOTHING)
    Owner = models.ForeignKey(Owner, blank=False, null=True, on_delete=models.DO_NOTHING)
    Realtor = models.ForeignKey(Realtor, blank=False, null=True, on_delete=models.DO_NOTHING)
    
  #payment
    account_date =models.DateField(blank=False, null=True)
    reciept_no = models.CharField(max_length=200, blank=True, null=True)
    bankreciept_date = models.DateField(blank=True, null=True)
    bank =  models.CharField(max_length=200, blank=True, null=True)
    bank_branch =  models.CharField(max_length=200, blank=True, null=True)
    bank_agent_no =  models.CharField(max_length=200, blank=True, null=True)
    Amount = models.IntegerField(blank=False, null=True)
    Balance = models.IntegerField(blank=False, null=True)
    description = RichTextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.account_date} {self.Buyer}'

    def get_absolute_url(self):
        """Returns the url to access a particular location instance."""
        return reverse('malipo-detail', args=[str(self.id)])

          
class Malipo_three (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)

#Plot Information
    buying_price = models.IntegerField(blank=True, null=True)
    listing = models.ForeignKey(Listing, blank=False, null=True,on_delete=models.DO_NOTHING)
    Plot_no = models.CharField(max_length=200, blank=True, null=True)
    Buyer = models.ForeignKey(Buyer, blank=False, null=True, on_delete=models.DO_NOTHING)
    Owner = models.ForeignKey(Owner, blank=False, null=True, on_delete=models.DO_NOTHING)
    Realtor = models.ForeignKey(Realtor, blank=False, null=True, on_delete=models.DO_NOTHING)
    
  #payment
    account_date =models.DateField(blank=False, null=True)
    reciept_no = models.CharField(max_length=200, blank=True, null=True)
    bankreciept_date = models.DateField(blank=True, null=True)
    bank =  models.CharField(max_length=200, blank=True, null=True)
    bank_branch =  models.CharField(max_length=200, blank=True, null=True)
    bank_agent_no =  models.CharField(max_length=200, blank=True, null=True)
    Amount = models.IntegerField(blank=False, null=True)
    Balance = models.IntegerField(blank=False, null=True)
    description = RichTextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.account_date} {self.Buyer}'

    def get_absolute_url(self):
        """Returns the url to access a particular location instance."""
        return reverse('malipo-detail', args=[str(self.id)])

          
class Malipo_four (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)

#Plot Information
    buying_price = models.IntegerField(blank=True, null=True)
    listing = models.ForeignKey(Listing, blank=False, null=True,on_delete=models.DO_NOTHING)
    Plot_no = models.CharField(max_length=200, blank=True, null=True)
    Buyer = models.ForeignKey(Buyer, blank=False, null=True, on_delete=models.DO_NOTHING)
    Owner = models.ForeignKey(Owner, blank=False, null=True, on_delete=models.DO_NOTHING)
    Realtor = models.ForeignKey(Realtor, blank=False, null=True, on_delete=models.DO_NOTHING)
    
  #payment
    account_date =models.DateField(blank=False, null=True)
    reciept_no = models.CharField(max_length=200, blank=True, null=True)
    bankreciept_date = models.DateField(blank=True, null=True)
    bank =  models.CharField(max_length=200, blank=True, null=True)
    bank_branch =  models.CharField(max_length=200, blank=True, null=True)
    bank_agent_no =  models.CharField(max_length=200, blank=True, null=True)
    Amount = models.IntegerField(blank=False, null=True)
    Balance = models.IntegerField(blank=False, null=True)
    description = RichTextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.account_date} {self.Buyer}'

    def get_absolute_url(self):
        """Returns the url to access a particular location instance."""
        return reverse('malipo-detail', args=[str(self.id)])

          
class Malipo_five (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)

#Plot Information
    buying_price = models.IntegerField(blank=True, null=True)
    listing = models.ForeignKey(Listing, blank=False, null=True,on_delete=models.DO_NOTHING)
    Plot_no = models.CharField(max_length=200, blank=True, null=True)
    Buyer = models.ForeignKey(Buyer, blank=False, null=True, on_delete=models.DO_NOTHING)
    Owner = models.ForeignKey(Owner, blank=False, null=True, on_delete=models.DO_NOTHING)
    Realtor = models.ForeignKey(Realtor, blank=False, null=True, on_delete=models.DO_NOTHING)
    
  #payment
    account_date =models.DateField(blank=False, null=True)
    reciept_no = models.CharField(max_length=200, blank=True, null=True)
    bankreciept_date = models.DateField(blank=True, null=True)
    bank =  models.CharField(max_length=200, blank=True, null=True)
    bank_branch =  models.CharField(max_length=200, blank=True, null=True)
    bank_agent_no =  models.CharField(max_length=200, blank=True, null=True)
    Amount = models.IntegerField(blank=False, null=True)
    Balance = models.IntegerField(blank=False, null=True)
    description = RichTextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.account_date} {self.Buyer}'

    def get_absolute_url(self):
        """Returns the url to access a particular location instance."""
        return reverse('malipo-detail', args=[str(self.id)])

              
class Malipo_six (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)

#Plot Information
    buying_price = models.IntegerField(blank=True, null=True)
    listing = models.ForeignKey(Listing, blank=False, null=True,on_delete=models.DO_NOTHING)
    Plot_no = models.CharField(max_length=200, blank=True, null=True)
    Buyer = models.ForeignKey(Buyer, blank=False, null=True, on_delete=models.DO_NOTHING)
    Owner = models.ForeignKey(Owner, blank=False, null=True, on_delete=models.DO_NOTHING)
    Realtor = models.ForeignKey(Realtor, blank=False, null=True, on_delete=models.DO_NOTHING)
    
  #payment
    account_date =models.DateField(blank=False, null=True)
    reciept_no = models.CharField(max_length=200, blank=True, null=True)
    bankreciept_date = models.DateField(blank=True, null=True)
    bank =  models.CharField(max_length=200, blank=True, null=True)
    bank_branch =  models.CharField(max_length=200, blank=True, null=True)
    bank_agent_no =  models.CharField(max_length=200, blank=True, null=True)
    Amount = models.IntegerField(blank=False, null=True)
    Balance = models.IntegerField(blank=False, null=True)
    description = RichTextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.account_date} {self.Buyer}'

    def get_absolute_url(self):
        """Returns the url to access a particular location instance."""
        return reverse('malipo-detail', args=[str(self.id)])
 
          
class Malipo_seven (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)

#Plot Information
    buying_price = models.IntegerField(blank=True, null=True)
    listing = models.ForeignKey(Listing, blank=False, null=True,on_delete=models.DO_NOTHING)
    Plot_no = models.CharField(max_length=200, blank=True, null=True)
    Buyer = models.ForeignKey(Buyer, blank=False, null=True, on_delete=models.DO_NOTHING)
    Owner = models.ForeignKey(Owner, blank=False, null=True, on_delete=models.DO_NOTHING)
    Realtor = models.ForeignKey(Realtor, blank=False, null=True, on_delete=models.DO_NOTHING)
    
  #payment
    account_date =models.DateField(blank=False, null=True)
    reciept_no = models.CharField(max_length=200, blank=True, null=True)
    bankreciept_date = models.DateField(blank=True, null=True)
    bank =  models.CharField(max_length=200, blank=True, null=True)
    bank_branch =  models.CharField(max_length=200, blank=True, null=True)
    bank_agent_no =  models.CharField(max_length=200, blank=True, null=True)
    Amount = models.IntegerField(blank=False, null=True)
    Balance = models.IntegerField(blank=False, null=True)
    description = RichTextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.account_date} {self.Buyer}'

    def get_absolute_url(self):
        """Returns the url to access a particular location instance."""
        return reverse('malipo-detail', args=[str(self.id)])
 
          
class Malipo_eight (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)

#Plot Information
    buying_price = models.IntegerField(blank=True, null=True)
    listing = models.ForeignKey(Listing, blank=False, null=True,on_delete=models.DO_NOTHING)
    Plot_no = models.CharField(max_length=200, blank=True, null=True)
    Buyer = models.ForeignKey(Buyer, blank=False, null=True, on_delete=models.DO_NOTHING)
    Owner = models.ForeignKey(Owner, blank=False, null=True, on_delete=models.DO_NOTHING)
    Realtor = models.ForeignKey(Realtor, blank=False, null=True, on_delete=models.DO_NOTHING)
    
  #payment
    account_date =models.DateField(blank=False, null=True)
    reciept_no = models.CharField(max_length=200, blank=True, null=True)
    bankreciept_date = models.DateField(blank=True, null=True)
    bank =  models.CharField(max_length=200, blank=True, null=True)
    bank_branch =  models.CharField(max_length=200, blank=True, null=True)
    bank_agent_no =  models.CharField(max_length=200, blank=True, null=True)
    Amount = models.IntegerField(blank=False, null=True)
    Balance = models.IntegerField(blank=False, null=True)
    description = RichTextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.account_date} {self.Buyer}'

    def get_absolute_url(self):
        """Returns the url to access a particular location instance."""
        return reverse('malipo-detail', args=[str(self.id)])

          
class Malipo_nine (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)

#Plot Information
    buying_price = models.IntegerField(blank=True, null=True)
    listing = models.ForeignKey(Listing, blank=False, null=True,on_delete=models.DO_NOTHING)
    Plot_no = models.CharField(max_length=200, blank=True, null=True)
    Buyer = models.ForeignKey(Buyer, blank=False, null=True, on_delete=models.DO_NOTHING)
    Owner = models.ForeignKey(Owner, blank=False, null=True, on_delete=models.DO_NOTHING)
    Realtor = models.ForeignKey(Realtor, blank=False, null=True, on_delete=models.DO_NOTHING)
    
  #payment
    account_date =models.DateField(blank=False, null=True)
    reciept_no = models.CharField(max_length=200, blank=True, null=True)
    bankreciept_date = models.DateField(blank=True, null=True)
    bank =  models.CharField(max_length=200, blank=True, null=True)
    bank_branch =  models.CharField(max_length=200, blank=True, null=True)
    bank_agent_no =  models.CharField(max_length=200, blank=True, null=True)
    Amount = models.IntegerField(blank=False, null=True)
    Balance = models.IntegerField(blank=False, null=True)
    description = RichTextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.account_date} {self.Buyer}'

    def get_absolute_url(self):
        """Returns the url to access a particular location instance."""
        return reverse('malipo-detail', args=[str(self.id)])

          
class Malipo_ten (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)

#Plot Information
    buying_price = models.IntegerField(blank=True, null=True)
    listing = models.ForeignKey(Listing, blank=False, null=True,on_delete=models.DO_NOTHING)
    Plot_no = models.CharField(max_length=200, blank=True, null=True)
    Buyer = models.ForeignKey(Buyer, blank=False, null=True, on_delete=models.DO_NOTHING)
    Owner = models.ForeignKey(Owner, blank=False, null=True, on_delete=models.DO_NOTHING)
    Realtor = models.ForeignKey(Realtor, blank=False, null=True, on_delete=models.DO_NOTHING)
    
  #payment
    account_date =models.DateField(blank=False, null=True)
    reciept_no = models.CharField(max_length=200, blank=True, null=True)
    bankreciept_date = models.DateField(blank=True, null=True)
    bank =  models.CharField(max_length=200, blank=True, null=True)
    bank_branch =  models.CharField(max_length=200, blank=True, null=True)
    bank_agent_no =  models.CharField(max_length=200, blank=True, null=True)
    Amount = models.IntegerField(blank=False, null=True)
    Balance = models.IntegerField(blank=False, null=True)
    description = RichTextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.account_date} {self.Buyer}'

    def get_absolute_url(self):
        """Returns the url to access a particular location instance."""
        return reverse('malipo-detail', args=[str(self.id)])

          
class Malipo_eleven (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)

#Plot Information
    buying_price = models.IntegerField(blank=True, null=True)
    listing = models.ForeignKey(Listing, blank=False, null=True,on_delete=models.DO_NOTHING)
    Plot_no = models.CharField(max_length=200, blank=True, null=True)
    Buyer = models.ForeignKey(Buyer, blank=False, null=True, on_delete=models.DO_NOTHING)
    Owner = models.ForeignKey(Owner, blank=False, null=True, on_delete=models.DO_NOTHING)
    Realtor = models.ForeignKey(Realtor, blank=False, null=True, on_delete=models.DO_NOTHING)
    
  #payment
    account_date =models.DateField(blank=False, null=True)
    reciept_no = models.CharField(max_length=200, blank=True, null=True)
    bankreciept_date = models.DateField(blank=True, null=True)
    bank =  models.CharField(max_length=200, blank=True, null=True)
    bank_branch =  models.CharField(max_length=200, blank=True, null=True)
    bank_agent_no =  models.CharField(max_length=200, blank=True, null=True)
    Amount = models.IntegerField(blank=False, null=True)
    Balance = models.IntegerField(blank=False, null=True)
    description = RichTextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.account_date} {self.Buyer}'

    def get_absolute_url(self):
        """Returns the url to access a particular location instance."""
        return reverse('malipo-detail', args=[str(self.id)])

          
class Malipo_twelve (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)

#Plot Information
    buying_price = models.IntegerField(blank=True, null=True)
    listing = models.ForeignKey(Listing, blank=False, null=True,on_delete=models.DO_NOTHING)
    Plot_no = models.CharField(max_length=200, blank=True, null=True)
    Buyer = models.ForeignKey(Buyer, blank=False, null=True, on_delete=models.DO_NOTHING)
    Owner = models.ForeignKey(Owner, blank=False, null=True, on_delete=models.DO_NOTHING)
    Realtor = models.ForeignKey(Realtor, blank=False, null=True, on_delete=models.DO_NOTHING)
    
  #payment
    account_date =models.DateField(blank=False, null=True)
    reciept_no = models.CharField(max_length=200, blank=True, null=True)
    bankreciept_date = models.DateField(blank=True, null=True)
    bank =  models.CharField(max_length=200, blank=True, null=True)
    bank_branch =  models.CharField(max_length=200, blank=True, null=True)
    bank_agent_no =  models.CharField(max_length=200, blank=True, null=True)
    Amount = models.IntegerField(blank=False, null=True)
    Balance = models.IntegerField(blank=False, null=True)
    description = RichTextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.account_date} {self.Buyer}'

    def get_absolute_url(self):
        """Returns the url to access a particular location instance."""
        return reverse('malipo-detail', args=[str(self.id)])
              
