import { useEffect, useState } from "react";
import { apiFetch } from "../api/api";


function Guides() {

    const [guides, setGuides] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");


    useEffect(() => {

        async function loadGuides() {

            try {

                const data = await apiFetch("/guides/");
                setGuides(data);

            } catch (err) {

                setError(err.message);

            } finally {

                setLoading(false);

            }
        }


        loadGuides();

    }, []);



    if (loading) {
        return <h2>A carregar guias...</h2>;
    }


    if (error) {
        return <h2>Erro: {error}</h2>;
    }


    return (
        <div>

            <h1>
                Guias de Angola
            </h1>


            {
                guides.length === 0 ? (

                    <p>
                        Nenhum guia encontrado.
                    </p>

                ) : (

                    guides.map((guide) => (

                        <div key={guide.id}>

                            <h2>
                                {guide.name}
                            </h2>

                            <p>
                                {guide.biography}
                            </p>

                            <p>
                                Cidade: {guide.city}
                            </p>

                            <hr />

                        </div>

                    ))

                )
            }


        </div>
    );
}


export default Guides;