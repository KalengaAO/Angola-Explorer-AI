import { useEffect, useState } from "react";
import { apiFetch } from "../api/api";
import DestinationCard from "../components/DestinationCard";

function Destinations() {
    const [destinations, setDestinations] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {
        async function loadDestinations() {
            try {
                const data = await apiFetch("/destinations/");
                setDestinations(data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        }

        loadDestinations();
    }, []);

    if (loading) {
        return <h2>A carregar destinos...</h2>;
    }

    if (error) {
        return <h2>Erro: {error}</h2>;
    }

    return (
        <div>
            <h1>Destinos de Angola</h1>

            {destinations.length === 0 ? (
                <p>Nenhum destino encontrado.</p>
            ) : (
                destinations.map((destination) => (
                    <DestinationCard
                        key={destination.id}
                        destination={destination}
                    />
                ))
            )}
        </div>
    );
}

export default Destinations;