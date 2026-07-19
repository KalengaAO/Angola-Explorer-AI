import {
    BrowserRouter,
    Routes,
    Route
} from "react-router-dom";

import Home from "./pages/Home";
import Destinations from "./pages/Destinations";
import Navbar from "./components/Navbar";
import Guides from "./pages/Guides";

function App() {
    return (
        <BrowserRouter>

            <Navbar />

            <Routes>

                <Route
                    path="/"
                    element={<Home />}
                />

                <Route
                    path="/destinations"
                    element={<Destinations />}
                />

                <Route
                    path="/guides"
                    element={<Guides />}
                />

            </Routes>

        </BrowserRouter>
    );
}


export default App;