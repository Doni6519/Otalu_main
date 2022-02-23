from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .forms import AdvertForm
class AdvertCreateView(LoginRequiredMixin, CreateView):
    form_class = AdvertForm
    success_url = reverse_lazy('home')
    template_name = 'advert/advert.html'
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)
'''class AdvertUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AdvertForm
    success_url = reverse_lazy('home')
    template_name = 'advert_update.html'
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)
class AdvertDeleteView(LoginRequiredMixin, DeleteView):
    form_class = AdvertForm
    success_url = reverse_lazy('home')
    template_name = 'advert_delete.html'
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)
class AdvertListView(LoginRequiredMixin, ListView):
    form_class = AdvertForm
    success_url = reverse_lazy('home')
    template_name = 'advert_list.html'
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)'''