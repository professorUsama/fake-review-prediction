// components/ReviewDetail.jsx
"use client"
import { Radar } from 'react-chartjs-2';
import { Chart as ChartJS, RadialLinearScale, PointElement, LineElement, Tooltip, Legend } from 'chart.js';

ChartJS.register(RadialLinearScale, PointElement, LineElement, Tooltip, Legend);

const ReviewDetail = ({ review }) => {
    const sentimentData = {
        labels: ['Negative', 'Neutral', 'Positive', 'Compound'],
        datasets: [
            {
                label: 'Sentiment Scores',
                data: [
                    review.sentiment_scores.neg,
                    review.sentiment_scores.neu,
                    review.sentiment_scores.pos,
                    review.sentiment_scores.compound,
                ],
                backgroundColor: 'rgba(255, 159, 64, 0.2)',
                borderColor: 'rgba(255, 159, 64, 1)',
                borderWidth: 1,
            },
        ],
    };

    const wordImportanceData = {
        labels: review.word_importances.map(item => item[0]),
        datasets: [
            {
                label: 'Word Importances',
                data: review.word_importances.map(item => item[1]),
                backgroundColor: review.word_importances.map(item => 
                    item[1] > 0 ? 'rgba(75, 192, 192, 0.2)' : 'rgba(255, 99, 132, 0.2)'
                ),
                borderColor: review.word_importances.map(item => 
                    item[1] > 0 ? 'rgba(75, 192, 192, 1)' : 'rgba(255, 99, 132, 1)'
                ),
                borderWidth: 1,
            },
        ],
    };

    return (
        <div className='border-b-2' style={{ padding: '20px', maxWidth: '800px', margin: '0 auto' }}>
            <h3>Review: {review.review_text}</h3>
            <p>Prediction: {review.prediction}</p>
            <p>Confidence: {review.confidence.toFixed(2)}</p>
            <div style={{ marginBottom: '20px' }}>
                <h4>Sentiment Scores</h4>
                <Radar data={sentimentData} />
            </div>
            <div style={{ marginBottom: '20px' }}>
                <h4>Word Importances</h4>
                <Radar data={wordImportanceData} />
            </div>
        </div>
    );
};

export default ReviewDetail;
