import React from 'react';
import logo from "../images/big-logo.png"
import {Button, Container, Image} from 'react-bootstrap';

export default function FooterMarkup() {
    return (
        <section className="footer">
            <Container>
                <img className='footer__img' src={logo} alt="logo"></img>
            </Container>
        </section>
    )
}
