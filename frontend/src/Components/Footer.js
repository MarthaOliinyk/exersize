import React from 'react';
import logo from "../images/big-logo.png"
import {Button, Container, Image} from 'react-bootstrap';

export default function FooterMarkup() {
    return (
        <section className="footer">
            <Container className='footer__container'>
                <img className='footer__img' src={logo} alt="logo"></img>
                <div className='footer__left'>
                    <h2 className='footer__header'>Contact</h2>
                    <p className='footer__gmail'>contact@exersize.com</p>
                    <p className='footer__field'>Licencing</p>
                    <p className='footer__field'>Support</p>
                </div>
                <div className='footer__right'>
                    <h2 className='footer__header'>Explore</h2>
                    <p className='footer__field' >
                        <a href="#why">About</a>
                    </p>
                    <p className='footer__field' >
                        <a href="#workout">Workout classes</a>
                    </p>
                    <p className='footer__field'>Subscription plans</p>
                    <p className='footer__field' >
                        <a href="#gallery">Social networks</a>
                    </p>
                </div>
            </Container>
        </section>
    )
}
