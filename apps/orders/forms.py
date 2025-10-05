from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ShippingForm(forms.Form):
    city = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your city', 'class': 'form-control'})
    )
    district = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your district', 'class': 'form-control'})
    )
    street = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your street address', 'class': 'form-control'})
    )
    home_number = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your home/apartment number', 'class': 'form-control'})
    )
    additional_info = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Any special delivery instructions', 'rows': 3, 'class': 'form-control'})
    )
