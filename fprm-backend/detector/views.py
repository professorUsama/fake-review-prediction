# detector/views.py (using functional views)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import ReviewDetection
from .serializers import ReviewDetectionSerializer
from .utils import predict_review
import statistics  # to calulate avg and standard deviation
import numpy as np


@api_view(["GET"])
def get_reviews(request):
    """
    Fetch all ReviewDetection instances.
    """
    reviews = ReviewDetection.objects.all()
    serializer = ReviewDetectionSerializer(reviews, many=True)
    return Response(serializer.data)



@api_view(["GET"])
def review_list(request):
    reviews = ReviewDetection.objects.all()
    results = []

    # Data for aggregate statistics
    total_reviews = len(reviews)
    original_reviews = 0
    computer_generated_reviews = 0
    all_confidences = []
    all_sentiment_compounds = []
    all_word_importances = {}

    # First Loop:  Collect per-review data and aggregate stats
    for review in reviews:
        # Convert data types
        sentiment_scores = dict(review.sentiment_scores)
        word_importances = review.word_importances

        # Update aggregate data
        if review.prediction == "Original":
            original_reviews += 1
        else:
            computer_generated_reviews += 1
        all_confidences.append(review.confidence)
        all_sentiment_compounds.append(sentiment_scores["compound"])
        for word, importance in word_importances:
            all_word_importances[word] = all_word_importances.get(word, 0) + importance

        results.append(
            {  # Add individual review data in the results list
                "review_text": review.review_text,
                "prediction": review.prediction,
                "confidence": review.confidence,
                "sentiment_scores": sentiment_scores,
                "word_importances": word_importances,
                "created_at": review.created_at,
            }
        )

    # Calculate averages
    avg_confidence = statistics.mean(all_confidences) if all_confidences else 0
    avg_sentiment_compound = (
        statistics.mean(all_sentiment_compounds) if all_sentiment_compounds else 0
    )

    # Aggregate statistics
    aggregate_stats = {
        "total_reviews": total_reviews,
        "original_reviews": original_reviews,
        "computer_generated_reviews": computer_generated_reviews,
        "average_confidence": avg_confidence,
        "average_sentiment": avg_sentiment_compound,
        "overall_word_importances": all_word_importances,
        "std_dev_confidence": np.std(all_confidences) if all_confidences else 0,
        "std_dev_sentiment": (
            np.std(all_sentiment_compounds) if all_sentiment_compounds else 0
        ),
    }

    # results.append(aggregate_stats)
    response_data = {
        "overall_summary": aggregate_stats,
        "detailed_reviews": results
    }

    return Response(response_data)


@api_view(["POST"])
def review_detect(request):
    """
    Analyze a new review and save the results.
    """
    serializer = ReviewDetectionSerializer(data=request.data)
    if serializer.is_valid():
        review_text = serializer.validated_data["review_text"]

        # Prediction logic (Replace with your actual implementation)
        prediction, confidence, sentiment, explanation = predict_review(review_text)

        serializer.save(
            review_text=review_text,
            prediction=prediction,
            confidence=confidence,
            sentiment_scores=sentiment,
            word_importances=explanation,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
