import Header from "./Components/Header";
import HomePage from "./Components/Homepage"
import Hero from "./Components/Hero"
import Why from "./Components/Why"
import Workout from "./Components/Workout"
import Pricing from "./Components/Pricing"
import Benefit from "./Components/Benefit"
import CoursesList from "./Components/CoursesList"
import Footer from "./Components/Footer"
import Gallery from "./Components/Gallery";
import NewCoursePage from "./Components/NewCourse";
import React from 'react';
import {Router} from "react-router-dom";
import "../src/App.scss"
import {BrowserRouter, Routes, Route, Link} from "react-router-dom";

function App() {
    return (
        <div className="App">
            <Header/>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<HomePage/>}/>
                    <Route path="/create" element={<NewCoursePage/>}/>
                    <Route path="/courses" element={<CoursesList/>}/>
                </Routes>
            </BrowserRouter>
            <Footer/>
        </div>
    );
}

export default App;
