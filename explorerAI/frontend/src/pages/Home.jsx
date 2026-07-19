import "../style/home.css";

function Home() {
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
                    placeholder="Ex: Quero conhecer praias em Angola..."
                />


                <button>
                    Perguntar
                </button>

            </div>

        </div>
    );
}


export default Home;