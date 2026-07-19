import {
    BrowserRouter,
    Routes,
    Route
} from "react-router-dom";


import Navbar from "./components/Navbar";

import Home from "./pages/Home";
import Register from "./pages/Register";
import GuideRegister from "./pages/GuideRegister";


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
                    path="/register"
                    element={<Register />}
                />


                <Route
                    path="/guide-register"
                    element={<GuideRegister />}
                />

            </Routes>

        </BrowserRouter>

    );
}


export default App;