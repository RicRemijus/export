from django import forms
from .models import Product, ProductImage, Subscriber
from django.forms.models import inlineformset_factory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'slug']

ProductImageFormSet = inlineformset_factory(Product, ProductImage, fields=('image', 'alt_text'), extra=1, can_delete=True)

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),}