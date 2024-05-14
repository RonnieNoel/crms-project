from django import forms
from login.models import Crime

class CrimeForm(forms.ModelForm):
    class Meta:
        model = Crime
        fields = ['name', 'description', 'location', 'date_reported', 'time_reported','email']
    

