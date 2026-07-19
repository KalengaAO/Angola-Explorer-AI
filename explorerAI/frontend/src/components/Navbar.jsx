import { Link } from "react-router-dom";
import "../style/Navbar.css";

function Navbar() {
    return (
        <nav>

            <Link to="/">
                Angola Explorer AI
            </Link>

            {" | "}

            <Link to="/register">
                Registar
            </Link>

            {" | "}

            <Link to="/guide-register">
                Sou Guia
            </Link>

        </nav>
    );
}


export default Navbar;