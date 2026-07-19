function GuideCard({ guide }) {
    return (
        <div>

            <h2>
                {guide.name}
            </h2>

            <p>
                {guide.biography}
            </p>

            <p>
                Cidade: {guide.city}
            </p>

            <p>
                Experiência: {guide.experience_years} anos
            </p>

            <hr />

        </div>
    );
}

export default GuideCard;