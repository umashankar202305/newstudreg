from django import forms
from regapp.models import suserreg
class studentform(forms.ModelForm):
    class Meta:
        model=suserreg
        fields="__all__"
        
    