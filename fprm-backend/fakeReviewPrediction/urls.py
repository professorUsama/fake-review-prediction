# fakeReviewPrediction/urls.py
from django.contrib import admin
from django.urls import path, include  # Use 'path' and 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('detector.urls')),  # Use 'path' for inclusion
]
