from django.views.generic import ListView, DetailView
from .models import House
class HouseListView(ListView):
    model = House
    context_object_name = 'house_list'
    template_name = 'house/house_list.html'
class HouseDetailView(DetailView):
    model = House
    context_object_name = 'house'
    template_name = 'house/house_detail.html'