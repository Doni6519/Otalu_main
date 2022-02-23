from django.urls import path
from .views import HomePageView, DetailPageView,AccountPageView
urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('detail/', DetailPageView.as_view(), name='detail'),
path('account/', AccountPageView.as_view(), name='account')

]