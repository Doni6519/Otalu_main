from django.contrib import admin
from .models import House, Review
class ReviewInline(admin.TabularInline):
    model = Review
class HouseAdmin(admin.ModelAdmin):
    inlines = [
    ReviewInline,
    ]
    list_display = ("title", "author", "price",)
class ReviewInline(admin.TabularInline):
    model = Review
admin.site.register(House, HouseAdmin)