"use client"

const Feed = ({review}) => {
const date = new Date(review.created_at);
const monthName = date.toLocaleString('default', { month: 'long' });
const year = date.getFullYear();
const formatedDate = `${monthName} ${year}`

  return (

    <ol className="relative border-s border-gray-200">
      <li className="mb-10 ms-4">
        <div className="absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -start-1.5 border border-white"></div>
        <time className="mb-1 text-sm font-normal leading-none text-gray-400">{formatedDate}</time>
        <h3 className="text-lg font-semibold text-gray-900 dark:text-white">{review.prediction}</h3>
        <p className="text-base font-normal text-gray-500">{review.review_text}</p>
      </li>
    </ol>
  )
}

export default Feed