from django.urls import path
from .views import HouseListView, HouseDetailView
urlpatterns = [
path('', HouseListView.as_view(), name='house_list'),
path('<uuid:pk>', HouseDetailView.as_view(), name='house_detail'),
]