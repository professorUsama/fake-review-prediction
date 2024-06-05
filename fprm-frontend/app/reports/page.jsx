
import OverallPerformance from '@components/OverallPerformance';
import ReviewDetail from '@components/ReviewDetail';
import { apiClient } from "@lib/apiService";

const Reports = async () => {
  const data = await apiClient("/reviews/");
  console.log(data);
  if (!data) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <div className='border-b-2'>
        <OverallPerformance data={data.overall_summary} />
      </div>
      <div className='border-b-2'>
        {data.detailed_reviews.map((review, index) => (
          <ReviewDetail key={index} review={review} />
        ))}
      </div>
    </div>
  );
};

export const revalidate = 60;

export default Reports;
