import { useState } from "react";
import { apiFetch } from "../api/api";
import "../style/home.css";


function Home() {

    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");
    const [loading, setLoading] = useState(false);


    async function handleSubmit() {

        if (!question.trim()) {
            return;
        }


        try {

            setLoading(true);
            setAnswer("");


            const data = await apiFetch(
                "/agents/recommend",
                {
                    method: "POST",
                    body: JSON.stringify({
                        question: question
                    })
                }
            );


            setAnswer(data.answer);


        } catch (error) {

            setAnswer(
                "Erro ao comunicar com o agente."
            );

            console.error(error);

        } finally {

            setLoading(false);

        }

    }


    return (
        <div className="home">

            <h1>
                Angola Explorer AI
            </h1>


            <p>
                Descubra Angola através de uma experiência
                inteligente baseada em agentes de IA.
            </p>


            <div className="chat-box">

                <input
                    type="text"
                    value={question}
                    onChange={(event) =>
                        setQuestion(event.target.value)
                    }
                    placeholder="Ex: Quero conhecer lugares de natureza em Angola..."
                />


                <button
                    onClick={handleSubmit}
                    disabled={loading}
                >

                    {
                        loading
                            ? "Pensando..."
                            : "Perguntar"
                    }

                </button>

            </div>


            {
                answer && (

                    <div className="response">

                        <h3>
                            Resposta:
                        </h3>

                        <p>
                            {answer}
                        </p>

                    </div>

                )
            }


        </div>
    );
}


export default Home;