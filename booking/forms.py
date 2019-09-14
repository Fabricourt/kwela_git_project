from django import forms
from .models import Bookspot

class BookspotForm(forms.ModelForm):
    class Meta:
        model = Bookspot
        fields = (
            'user_id', 
            'first_name',
            'last_name',          
            'email',
            'phone_number',
            'id_number',
           
            )
    
  