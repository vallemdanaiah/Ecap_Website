from django import forms
from .models import StdDetailes
#create the your views
class StdDetailesForm(forms.ModelForm):
    class Meta():
        model = StdDetailes
        fields = '__all__'
