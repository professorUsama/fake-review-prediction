# detector/serializers.py

from rest_framework import serializers
from .models import ReviewDetection


class ReviewDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewDetection
        fields = [
            "review_text",
            "prediction",
            "confidence",
            "sentiment_scores",
            "word_importances",
            "created_at",
        ]
