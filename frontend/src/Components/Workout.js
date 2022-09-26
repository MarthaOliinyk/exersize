import React, { Component }  from 'react';
import { Container,CardDeck, CardImg,Button} from 'react-bootstrap';

import Card from 'react-bootstrap/Card';

import pic1 from "../images/workout1.png"
import pic2 from "../images/workout2.jpg"
import pic3 from "../images/workout3.jpg"
export default function WorkoutMarkup() {
  return (
    <div className='workout__wrapper'>
        <div className='main__container workout__container'>
            <h2 className='workout__title'>WORKOUT CLASSES</h2>
            <ul className='workout__list'>
                <li className='workout__item'>
                    <img className='workout__img' src={pic1} alt="Fitness"></img>
                    <div className='workout__content'>
                        <p className='workout__time'>1 Hour</p>
                        <h3 className='workout__text'>Fitness</h3>
                    </div>
                </li>
                <li className='workout__item'>
                    <img className='workout__img' src={pic2} alt="Weight Lifting"></img>
                    <div className='workout__content'>
                        <p className='workout__time'>1 Hour</p>
                        <h3 className='workout__text'>Weight Lifting</h3>
                    </div>
                </li>
                <li className='workout__item'>
                    <img className='workout__img' src={pic3} alt="Cardio"></img>
                    <div className='workout__content'>
                        <p className='workout__time'>1 Hour</p>
                        <h3 className='workout__text'>Cardio</h3>
                    </div>
                </li>
                <li className='workout__item'>
                    <img className='workout__img' src={pic1} alt="Yoga"></img>
                    <div className='workout__content'>
                        <p className='workout__time'>1 Hour</p>
                        <h3 className='workout__text'>Yoga</h3>
                    </div>
                </li>
            </ul>
            <Button className={`button workout__button`}>View all</Button>
        </div>
    </div>
  );
}
