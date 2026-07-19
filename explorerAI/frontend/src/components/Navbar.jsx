import { Link } from "react-router-dom";


function Navbar() {
    return (
        <nav>

            <Link to="/">
                Home
            </Link>

            {" | "}

            <Link to="/destinations">
                Destinos
            </Link>
            {" | "}

            <Link to="/guides">
                Guias
            </Link>
        </nav>
    );
}


export default Navbar;