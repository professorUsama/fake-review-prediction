# Fake Review Detection System

This project is a fake review detection system that leverages machine learning and sentiment analysis to determine whether product reviews are genuine or computer-generated. It provides a user-friendly interface for analyzing reviews and visualizing the results.

## Features

*   **Fake Review Prediction:**  Uses a machine learning model to predict if a review is real or fake.
*   **Sentiment Analysis:**  Provides sentiment scores for each review.
*   **Word Importance Analysis:** Explains the model's predictions using LIME.
*   **Aggregate Statistics:**  Displays overall statistics about analyzed reviews.
*   **Interactive UI:**  Easy-to-use Next.js frontend for submitting reviews and viewing results.

## Technologies Used

*   **Backend:** Python, Django, Django REST Framework
*   **Frontend:** Next.js 14
*   **Database:** MongoDB (Djongo)
*   **Machine Learning:** TensorFlow Hub (Universal Sentence Encoder), Scikit-learn
*   **Sentiment Analysis:** VADER
*   **Explanation:** LIME

## Project Setup

1.  **Clone the Repository:**
    ```bash
    https://github.com/professorUsama/fake-review-prediction.git
    ```

2.  **Backend (Django):**
    *   **Navigate to Backend:** `cd fprm-backend`
    *   **Create a Virtual Environment:** 
        ```bash
        python -m venv fake-review-env
        ```
    *   **Activate Environment:**
        ```bash
        fake-review-env\Scripts\activate  # Windows
        source fake-review-env/bin/activate  # macOS/Linux
        ```
    *   **Install Dependencies:**
        ```bash
        pip install -r requirements.txt
        ```
    *   **Run Migrations:**
        ```bash
        python manage.py migrate
        ```
    *   **Start the Server:**
        ```bash
        python manage.py runserver
        ```
       
3.  **Frontend (Next.js):**
    *   **Navigate to Frontend:** `cd fprm-frontend`
    *   **Install Dependencies:**
        ```bash
        npm install
        ```
    *   **Start Development Server:**
        ```bash
        npm run dev
        ```

## Usage

1.  **Open the Frontend:** Open your web browser and go to `http://localhost:3000`.
2.  **Enter a Review:** Type or paste a review into the input field.
3.  **Submit for Analysis:** Click the "Analyze" button.
4.  **View Results:** See the predicted label, confidence score, sentiment scores, and word importance analysis.

## Future Enhancements

*   **Improved Model:** Experiment with different models or fine-tuning to enhance accuracy.
*   **Enhanced UI:** Add more visualizations and interactive elements to the frontend.
*   **Deployment:** Deploy to a production environment for broader access.
*   **Additional Features:**  Incorporate user feedback, ratings, and more.
