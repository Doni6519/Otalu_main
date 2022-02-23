from operator import index
from django.urls import path
from .views import (
    AdvertCreateView,
    # AdvertListView,
    # AdvertUpdateView,
    # AdvertDeleteView,
)
urlpatterns = [
path('', AdvertCreateView.as_view(), name='advert'),
]