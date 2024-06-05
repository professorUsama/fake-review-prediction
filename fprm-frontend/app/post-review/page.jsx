"use client"

import Form from "@components/Form";
import { useState } from "react";
import { useRouter } from "next/navigation";

const PostReview = () => {
  const [reviewText, setReviewText] = useState('')
  const [submitting, setSubmitting] = useState(false);
  const router = useRouter();
  const createReview = async (e) => {
    e.preventDefault();
    setSubmitting(true);
    try {
      const response = await fetch("http://localhost:8000/api/reviews/detect/", {
        method: "POST",
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          review_text: reviewText,
        })
      })
      if (response.ok) {
        router.push("/");
      }
    } catch (error) {
      console.log(error)
    } finally {
      setSubmitting(false);
    }
  }
  return (
    <div className="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
      <Form reviewText={reviewText} setReviewText={setReviewText} submitting={submitting} handleSubmit={createReview} />
    </div>

  )
}

export default PostReview