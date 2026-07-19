function DestinationCard({ destination }) {
    return (
        <div>
            <h2>
                {destination.name}
            </h2>

            <p>
                {destination.description}
            </p>

            <hr />
        </div>
    );
}

export default DestinationCard;