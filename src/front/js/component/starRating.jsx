import React, { useState } from "react";
import { FaStar } from "react-icons/fa";
import "../../styles/index.css";
const StarRating = () => {
  const [rating, setrating] = useState(null);
  const [hover, setHover] = useState(null);
  return (
    <div>
      {[...Array(5)].map((star, i) => {
        const ratingValue = i + 1;
        return (
          <div key={i}>
            <label>
              <form>
                <input
                  type="radio"
                  name="rating"
                  value={ratingValue}
                  onClick={() => actions.starRating(ratingValue)}
                />
              </form>
              <FaStar
                className="star"
                color={ratingValue <= (hover || rating) ? "#ffc107" : "#e4e5e9"}
                size={20}
                onMouseEnter={() => setHover(ratingValue)}
                onMouseLeave={() => setHover(null)}
              />
            </label>
          </div>
        );
      })}
    </div>
  );
};

export default StarRating;
