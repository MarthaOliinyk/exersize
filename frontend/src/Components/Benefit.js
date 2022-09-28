import React, { Component }  from 'react';
import { Button, Container, Image } from 'react-bootstrap';
import picture from "../../src/images/benefit.jpg"
export default function BenefitMarkup(){
    return(
        <section className='benefit__wrapper'>
        <div className='main__container benefit__container'>
            <div className='benefit__left'>
                <h2 className='benefit__title'>Who can benefit from a fully custom online fitness workouts?</h2>
                <p className='benefit__text'>Literally everyone. We are currently helping people from 12 to 60+ years old. Everyone is getting an adjusted program and a big variety of exercises.</p>
                <Button className='btn benefit__button'>Try it out</Button>
            </div>
            <img className='benefit__img img-fluid' src={picture} alt="sport"></img>
        </div>
        </section>
    )
}
