function ReviewCard({ review }) {

    return (
        <article>

            <h3>
                Avaliação
            </h3>


            <p>
                {review.comment}
            </p>


            <p>
                Nota: {review.rating}/5
            </p>

        </article>
    );
}


export default ReviewCard;