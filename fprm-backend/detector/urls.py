# detector/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("api/reviews/", views.review_list, name="review-list"),
    path("api/reviews/detect/", views.review_detect, name="review-detect"),
    path("api/reviews/get/", views.get_reviews, name="get_reviews"),
]
