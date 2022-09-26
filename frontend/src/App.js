import Header from "./Components/Header";
import Hero from "./Components/Hero"
import Why from "./Components/Why"
import Workout from "./Components/Workout"
import Pricing from "./Components/Pricing"
import Benefit from "./Components/Benefit"
import Footer from "./Components/Footer"
import React, { Component }  from 'react';
import "../src/App.scss"
function App() {
  return (
    <div className="App">
      <Header/>
      <Hero/>
      <Why/>
      <Workout/>
      <Pricing/>
      <Benefit/>
      <Footer/>
    </div>
  );
}

export default App;
