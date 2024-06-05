# detector/utils.py

import pandas as pd
import tensorflow_hub as hub
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
import numpy as np
from lime.lime_text import LimeTextExplainer

import os
from pathlib import Path

# Global variables to load model only once
data = None
embed = None
scaler = None
classifier = None


def load_model_and_data():
    global data, embed, scaler, classifier
    if data is None:  # Load the dataset and model only if not already loaded
        DATA_PATH = (
            Path(__file__).resolve().parent.parent / "data" / "fake_reviews_dataset.csv"
        )
        print(f"DATA_PATH: {DATA_PATH}")
        data = pd.read_csv(DATA_PATH)  # Make sure the path is correct
        data["label"] = data["label"].map({"CG": 0, "OR": 1})
        data["text_"] = data["text_"].apply(clean_text)
        train_reviews, test_reviews, train_labels, test_labels = train_test_split(
            data["text_"], data["label"], test_size=0.2, random_state=42
        )

        embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
        train_embeddings = get_embeddings(train_reviews)
        test_embeddings = get_embeddings(test_reviews)

        scaler = StandardScaler()
        train_embeddings_scaled = scaler.fit_transform(train_embeddings)
        test_embeddings_scaled = scaler.transform(test_embeddings)

        classifier = LogisticRegression(max_iter=1000)
        classifier.fit(train_embeddings_scaled, train_labels)


# Function to clean the text (same as before)
def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = text.lower()
    return text


# Function to embed reviews (same as before)
def get_embeddings(reviews):
    try:
        reviews = reviews.tolist()
        embeddings = embed(reviews).numpy()
        return embeddings
    except Exception as e:
        print(f"Error embedding reviews: {e}")
        return None


# Sentiment analysis function (same as before)
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    return scores


# Prediction function with explanation
def predict_review(review_text):
    load_model_and_data()  # Load data and model before prediction

    review_text_clean = clean_text(review_text)
    review_embedding = embed([review_text_clean]).numpy()
    review_embedding_scaled = scaler.transform(review_embedding)
    prediction = classifier.predict(review_embedding_scaled)
    prediction_prob = classifier.predict_proba(review_embedding_scaled)
    label = "Original" if prediction[0] == 1 else "Computer Generated"
    confidence = prediction_prob[0][prediction[0]]
    sentiment_scores = analyze_sentiment(review_text)

    def predict_proba_for_lime(texts):
        embeddings = embed(texts).numpy()
        embeddings_scaled = scaler.transform(embeddings)
        return classifier.predict_proba(embeddings_scaled)

    explainer = LimeTextExplainer(class_names=["Computer Generated", "Original"])
    explanation = explainer.explain_instance(
        review_text_clean, predict_proba_for_lime, num_features=6
    )

    word_importances = explanation.as_list()

    return label, confidence, sentiment_scores, word_importances
