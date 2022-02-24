from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from houses.models import House
class HomePageView(TemplateView):
    template_name = 'home.html'
class DetailPageView(TemplateView):
    template_name = 'detail.html'
class AccountPageView(ListView):
    model = House
    context_object_name = 'house_list'
    template_name = 'account/profile.html'