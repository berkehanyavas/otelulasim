from django import forms
from .models import Vehicle

class AracEkleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'plate',
            'driver',
            'model',
            'max_passenger'
        ]