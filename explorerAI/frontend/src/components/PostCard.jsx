function PostCard({ post }) {

    return (
        <article>
            <h3>{post.title}</h3>

            <p>
                {post.content}
            </p>

            {
                post.photo &&
                <img
                    src={post.photo}
                    alt={post.title}
                />
            }

        </article>
    );
}


export default PostCard;