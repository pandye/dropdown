from django import forms
from dropdown.models import Country, State, City

class DropDownForm(forms.Form):
    country = forms.ModelChoiceField(queryset=Country.objects.all())
    state = forms.ModelChoiceField(queryset=State.objects.all())
    city = forms.ModelChoiceField(queryset=City.objects.all())

  
   
    
