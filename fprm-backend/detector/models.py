# detector/models.py

from djongo import models


class ReviewDetection(models.Model):
    review_text = models.TextField(help_text="The original review text")

    prediction = models.CharField(
        max_length=20,
        default="Pending",  # Default prediction is 'Pending'
        help_text="Predicted label (Original or Computer Generated)",
    )

    confidence = models.FloatField(
        default=0.0,  # Default confidence is 0.0
        help_text="Confidence score for the prediction",
    )

    sentiment_scores = models.JSONField(
        default=dict,  # Default is an empty dictionary
        help_text="Sentiment analysis scores",
    )

    word_importances = models.JSONField(
        default=list,  # Default is an empty list
        help_text="Word importances from LIME explanation",
    )

    created_at = models.DateTimeField(
        auto_now_add=True, help_text="Timestamp of when the detection was performed"
    )

    class Meta:
        verbose_name_plural = "Review Detections"
