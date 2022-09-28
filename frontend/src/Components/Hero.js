import React, { Component }  from 'react';
import { Container } from 'react-bootstrap';
import img from "../images/hero.jpg"
import { Button} from 'react-bootstrap'
//import "../../scss/hero.css"
export default function HeroMarkup()
{
    return(
        <div className="wrapper">
        <div id="#hero" className="hero__container main__container">
            
                <img src={img}  className='hero__img'></img>
                <div className="hero__right">
                    <p className="hero__pre_title">Exercise Platform</p>
                    <h1 className="hero__title">Unleash your inner strength</h1>
                    <p className="hero__description">ExerSize+ lets you stay fit and healthy everywhere in the world. With the help of our highly experienced proffesional trainers it is dead-easy to continue workouts outside of your gym.</p>
                    <Button className="btn hero__btn">Online cosching</Button>
                </div>

         </div>
         </div>
       
    )
}
