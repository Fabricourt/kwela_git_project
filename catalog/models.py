from django.db import models
from datetime import datetime
from django.urls import reverse # Used to generate URLS by reversing the URL patterns

from listings.models import Listing
from realtors.models import Realtor
from django.contrib.auth.models import User  # Required to assign User as a debtor, buyer orseller
from datetime import date
from ckeditor.fields import RichTextField



class Propertytype(models.Model):
    """Model representing the type of Property."""
    name = models.CharField(max_length=200, help_text='Enter the type of plot (e.g. Commercial Plot, Rent house, e.t.c)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def display_Propertytype(self):
        """Create a string for the Propertytype. This is required to display propertytype in Admin."""
        return ', '.join(Propertytype.name for Propertytype in self.Propertytype.all()[:3])

    display_Propertytype.short_description = 'Propertytype'





class Location(models.Model):
    """Model representing a Location."""
    name = models.CharField(max_length=200, blank=True, null=True, help_text='ignore location if it already exists on listing, Only enter a new Location (e.g. Ruiru, Mwea, e.t.c)')
    propertiesno = models.IntegerField(blank=True, null=True, help_text='number of properties in this specific area')
    description = RichTextField(blank=True, help_text='define how many plots are what size, area history')
   

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def display_Location(self):
        """Create a string for the Location. This is required to display location in Admin."""
        return ', '.join(Location.name for Location in self.Location.all()[:3])


    def get_absolute_url(self):
        """Returns the url to access a particular location instance."""
        return reverse('location-detail', args=[str(self.id)])

class Meta:
    ordering = ['name']

   



class Paymenttype(models.Model):
    """Model representing the type of Payment."""
    name = models.CharField(max_length=200, help_text='Enter the type of payment choosen by the client (e.g. Cash, 3 months installments, 6 months installments e.t.c)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def display_Paymenttype(self):
        """Create a string for the Paymenttype. This is required to display Paymenttype in Admin."""
        return ', '.join(Paymenttype.name for Paymenttype in self.Paymenttype.all()[:3])

    display_Paymenttype.short_description = 'Paymenttype'






class Property(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, null=True, help_text='realtor assigned')
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    """Model representing a property(but not a specific property)."""
    title = models.CharField(max_length=200)
    
 
    # Foreign Key used because property can only have one Owner_buyer, but owner_buyer can have multiple properties
    # Owner_buyer is a string rather than object because it hasn't yet been declared in the file
    buyer = models.ForeignKey('Buyer', on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey('Owner', on_delete=models.SET_NULL, null=True)
    summary = RichTextField(max_length=1000, help_text='Enter a brief description of the property ownership')
    

    # ManyToManyField used because propertytype, location and paymenttype can contain many properties
    # propertytype, location and paymenttype have already been defined so we can specify the objects above.
    propertytype = models.ManyToManyField(Propertytype, help_text='select property type')
    location = models.ManyToManyField(Location, help_text='select location')
    Paymenttype = models.ManyToManyField(Paymenttype, help_text='select payment method')
    

    def get_absolute_url(self):
        """Returns the url to access a particular property instance."""
        return reverse('property-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title
class Meta:
        ordering = ['name']
 






class Owner(models.Model):
    """Model representing an owner."""
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, null=True,  help_text='realtor assigned')
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING, null=True,  help_text='particular listing assigned')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    identity_number = models.CharField(max_length=100, blank=False, null=False)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    description = RichTextField(blank=True, help_text='e.g property history, ownership, development' )
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_published = models.BooleanField(default=False)
    Registration_date = models.DateTimeField(default=datetime.now, blank=True, help_text='Date when buyer registered')
    listingAgreement_date =models.DateTimeField(default=datetime.now, blank=True, help_text='Date when buyer registered')
    selling_price = models.IntegerField(blank=True, null=True, help_text='amount agreed on as selling price')
    commissions = models.IntegerField(blank=True, null=True, help_text='amount agreed on as commisions to realtor')
    class Meta:
        ordering = ['last_name', 'first_name']


    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)

    def get_absolute_url(self):
        """Returns the url to access a particular location instance."""
        return reverse('owner-detail', args=[str(self.id)])





class Buyer(models.Model):
    """Model representing a buyer."""
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, null=True)
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING, null=True)
    owner = models.ForeignKey('Owner', on_delete=models.SET_NULL, null=True,  help_text='Owner Assigned')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    identity_number = models.CharField(max_length=100, blank=False, null=False)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    description = RichTextField(blank=True, help_text='e.g property history, ownership, development' )
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_BMVP = models.BooleanField(default=False)
    Registration_date = models.DateTimeField(default=datetime.now, null=True, blank=True, help_text='Date when buyer registered')
    Deposit_date = models.DateTimeField(default=datetime.now, blank=True, null=True, help_text='Date when buyer paid deposit')
    deposit_amount_paid = models.IntegerField(blank=True, null=True, help_text='amount paid as deposit')
    amount_agreed_on = models.IntegerField(blank=True, null=True, help_text='amount agreed on as buying price')
    installment_date = models.DateTimeField(default=datetime.now, null=True,  blank=True, help_text='Date when buyer agrees to pay next installment')
    Buying_date = models.DateTimeField(default=datetime.now, blank=True, null=True, help_text='Date when buyer bought the property or finished paying for the property')

    class Meta:permissions = (
            ("can_view_buyer",
             "Set book as returned"),
             ) 
    ordering = ['last_name', 'first_name']

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)

    def get_absolute_url(self):
        """Returns the url to access a particular location instance."""
        return reverse('buyer-detail', args=[str(self.id)])
