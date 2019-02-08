from django.contrib import admin
from django.contrib import auth
from catalog.models import Property, Buyer, Owner, Propertytype,  Location, Paymenttype
from listings.models import Listing
from realtors.models import Realtor


# admin.site.register(Property)
# admin.site.register(Buyer)
# admin.site.register(Owner)
# admin.site.register(PropertyInstance)
admin.site.register(Propertytype)
# admin.site.register(Location)
admin.site.register(Paymenttype)




@admin.register(Location)
class Location(admin.ModelAdmin):
    list_display = ('name','propertiesno',)
    search_fields = ('name','propertiesno',)
    list_filter = ('name','propertiesno',)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone', 'listingAgreement_date','listing','realtor',)
      
    fields = [
        ('listing', 'realtor'),
        ('first_name', 'last_name','identity_number'),
        ('photo','is_published','date_of_birth', 'date_of_death'),
        ('phone', 'email'),
        ('selling_price', 'commissions'),
        ('listingAgreement_date','Registration_date'),
        'description', 
        
    ]

admin.site.register(Owner, OwnerAdmin)



class BuyerAdmin(admin.ModelAdmin):

    list_display = ('last_name', 'first_name', 'phone', 'listing','owner','realtor',)
    fields = [
        ('listing','owner','realtor'),
        ('first_name', 'last_name','identity_number'),
        ('photo','is_BMVP','date_of_birth', 'date_of_death'),
        ('phone', 'email'),
        ('Registration_date', 'Deposit_date'),
        ('deposit_amount_paid','amount_agreed_on'),
        ('Buying_date', 'installment_date'),
        'description', 
       

        
    ]
  

admin.site.register(Buyer, BuyerAdmin)




# Register the Admin classes for Property using the decorator
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'buyer', 'listing', 'realtor')
    search_fields = ('title',  'buyer', 'owner', 'realtor','listing')
    list_filter = ( 'owner', 'buyer', 'realtor','listing')
    list_per_page = 25
    """Administration object for Property models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of Property instances in property view (inlines)
    """

   