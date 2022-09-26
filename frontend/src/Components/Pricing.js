import React, { Component }  from 'react';
import { Container } from 'react-bootstrap';
export default function PricingMarkup()
{
    return(
        <section className='main__container pricing__container'>
            <h3 className='pricing__pre_title'>OUR PRICING</h3>
            <h2 className='pricing__title'>PRICING & PACKAGES</h2>
            <ul className='pricing__list'>
                <li className='pricing__item'>
                    <h4 className='plan__title'>BASIC PLAN</h4>
                </li>
                <li className='pricing__item plan'>
                    <h4 className='plan__title'>BASIC PLAN</h4>
                </li>
                <li className='pricing__item plan'>
                    <h4 className='plan__title'>BASIC PLAN</h4>
                </li>
            </ul>
        </section>
    )
}
