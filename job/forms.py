from django import forms
from .models import Job

class JobEkleForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'location',
            'destination',
            'name',
            'surname',
            'passenger_count',
            'phone',
            'email',
            'date',
            'time',
            'flight_code',
            # 'price',
            # 'currency'
        ]