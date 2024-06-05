// components/OverallPerformance.jsx
"use client"
import { Bar, Pie } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, BarElement, CategoryScale, LinearScale, Tooltip, Legend } from 'chart.js';
import { useEffect, useState } from 'react';

ChartJS.register(ArcElement, BarElement, CategoryScale, LinearScale, Tooltip, Legend);

const OverallPerformance = ({ data }) => {
    const [sentimentData, setSentimentData] = useState({});
    const [wordImportanceData, setWordImportanceData] = useState({});

    useEffect(() => {
        if (data) {
            setSentimentData({
                labels: ['Average Sentiment'],
                datasets: [
                    {
                        label: 'Sentiment Scores',
                        data: [data.average_sentiment || 0],
                        backgroundColor: ['rgba(54, 162, 235, 0.2)'],
                        borderColor: ['rgba(54, 162, 235, 1)'],
                        borderWidth: 1,
                    },
                ],
            });

            setWordImportanceData({
                labels: Object.keys(data.overall_word_importances || {}),
                datasets: [
                    {
                        label: 'Word Importances',
                        data: Object.values(data.overall_word_importances || {}),
                        backgroundColor: Object.values(data.overall_word_importances || {}).map(value =>
                            value > 0 ? 'rgba(75, 192, 192, 0.2)' : 'rgba(255, 99, 132, 0.2)'
                        ),
                        borderColor: Object.values(data.overall_word_importances || {}).map(value =>
                            value > 0 ? 'rgba(75, 192, 192, 1)' : 'rgba(255, 99, 132, 1)'
                        ),
                        borderWidth: 1,
                    },
                ],
            });
        }
    }, [data]);

    return (
        <div style={{ padding: '20px', maxWidth: '800px', margin: '0 auto' }}>
            <h2>Overall Performance</h2>
            <div style={{ marginBottom: '20px' }}>
                <h3>Sentiment Summary</h3>
                {sentimentData.labels ? <Bar data={sentimentData} /> : <p>No sentiment data available</p>}
            </div>
            <div style={{ marginBottom: '20px' }}>
                <h3>Word Importances</h3>
                {wordImportanceData.labels ? <Pie data={wordImportanceData} /> : <p>No word importance data available</p>}
            </div>
            <div>
                <p>Total Reviews: {data.total_reviews}</p>
                <p>Computer Generated: {data.computer_generated_reviews}</p>
                <p>Original: {data.original_reviews}</p>
                <p>Average Confidence: {data.average_confidence?.toFixed(2)}</p>
                <p>Standard Deviation of Confidence: {data.std_dev_confidence?.toFixed(2)}</p>
                <p>Standard Deviation of Sentiment: {data.std_dev_sentiment?.toFixed(2)}</p>
            </div>
        </div>
    );
};

export default OverallPerformance;
