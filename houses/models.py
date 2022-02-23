from pydoc import describe
import uuid #helps us to acces a particular model
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from numpy import maximum
from numpy import True_
FENCED_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No')
)
ELECTRICITY_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No')
)
SECURITY_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No')
)
BATHROOM_CHOICES = (
    ('Inside', 'Inside'),
    ('Outside', 'Outside')
)
SMOKING_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No')
)
PARTY_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No')
)
SMOKING_CHOICES = (
    ('Allowed', 'Allowed'),
    ('Not Allowed', 'Not Allowed')
)
WATER_CHOICES = (
    ('Well', 'Well'),
    ('Borehole', 'Borehole')
)
WATER_AVAILABILITY_CHOICES = (
    ('24hrs', '24hrs'),
    ('Pomed once per day', 'Pomed once per day')
)
class House(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=200)
    rooms = models.IntegerField( blank=True, null=True)
    bathroom = models.CharField(max_length = 10, choices=BATHROOM_CHOICES, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    description = models.TextField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    security = models.CharField(max_length = 10, choices=SECURITY_CHOICES, blank=True, null=True)
    fenced = models.CharField(max_length = 10, choices=FENCED_CHOICES, blank=True, null=True)
    electricity = models.CharField(max_length = 10, choices=ELECTRICITY_CHOICES,blank=True, null=True)
    water = models.CharField(max_length = 10, choices=WATER_CHOICES, blank=True, null=True)
    water_availability = models.CharField(max_length = 20, choices=WATER_AVAILABILITY_CHOICES, blank=True, null=True)
    party = models.CharField(max_length = 20, choices=PARTY_CHOICES, blank=True, null=True)
    smoking = models.CharField(max_length = 20, choices=SMOKING_CHOICES, blank=True, null=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('house_detail', kwargs={'pk': str(self.pk)})
class Review(models.Model):
    house = models.ForeignKey(House,on_delete=models.CASCADE,related_name='reviews',)
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,)
    def __str__(self):
        return self.review