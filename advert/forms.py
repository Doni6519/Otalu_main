from django.forms import ModelForm
from houses.models import House
class AdvertForm(ModelForm):
    class Meta:
        model = House
        fields = ['title','rooms','bathroom','description','price','security','fenced','electricity','water','water_availability','party','smoking']
    