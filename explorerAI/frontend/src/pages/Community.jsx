import { useEffect, useState } from "react";

import { apiFetch } from "../api/api";

import PostCard from "../components/PostCard";
import ReviewCard from "../components/ReviewCard";

import "../style/Community.css";


function Community() {

    const [posts, setPosts] = useState([]);
    const [reviews, setReviews] = useState([]);

    useEffect(() => {

        async function loadCommunity(){

            const postsData = await apiFetch("/posts/");
            const reviewsData = await apiFetch("/reviews/");

            setPosts(postsData);
            setReviews(reviewsData);

        }

        loadCommunity();

    }, []);


    return (

        <main className="community-page">

            <h1>Comunidade Angola Explorer AI</h1>


            <section className="community-section">

                <h2>Experiências dos viajantes</h2>


                <div className="cards-container">

                {
                    posts.map(post => (

                        <PostCard
                            key={post.id}
                            post={post}
                        />

                    ))
                }

                </div>

            </section>



            <section className="community-section">

                <h2>Avaliações dos Guias</h2>


                <div className="cards-container">

                {
                    reviews.map(review => (

                        <ReviewCard
                            key={review.id}
                            review={review}
                        />

                    ))
                }

                </div>


            </section>


        </main>

    );

}


export default Community;