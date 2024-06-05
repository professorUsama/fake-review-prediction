import Feed from "@components/Feed"
import { apiClient } from "@lib/apiService";

const Home = async () => {
  const reviews = await apiClient("/reviews/get/");
  return (
    <div className="max-w-screen-xl mx-auto p-4">
      {
        reviews.map((review, index) => (
          <Feed key={index} review={review}/>
        ))
      }
    </div>
  )
}

export const revalidate = 60;

export default Home