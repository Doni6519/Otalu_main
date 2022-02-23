from django.forms import ModelForm
from .models import Review
class AdvertForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review']
    