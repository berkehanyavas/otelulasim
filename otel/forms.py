from django import forms
from .models import Otel, Pricing

class OtelEkleForm(forms.ModelForm):
    class Meta:
        model = Otel
        fields = [
            'name',
            'phone'
        ]
        
        
class PricingForm(forms.ModelForm):
    class Meta:
        model = Pricing
        fields=[
            'min_people',
            'max_people',
            'price',
            'currency'
        ]