import React, {Component} from 'react';
import {Container} from 'react-bootstrap';
import {Button} from 'react-bootstrap'

export default function WhyMarkup() {
    return (
        <section className="main__container why__container">
            <div className="why__left_part">
                <div className="why__sq">
                    <h3 className="why__number">20+</h3>
                    <p className="why__number_text">FITNESS TRAINERS</p>
                </div>
                <div className="why__sq">
                    <h3 className="why__number">200+</h3>
                    <p className="why__number_text">BEST EQUIPMENTS</p>
                </div>
                <div className="why__sq">
                    <h3 className="why__number">1000+</h3>
                    <p className="why__number_text">SATISFIED CLIENTS</p>
                </div>
                <div className="why__sq">
                    <h3 className="why__number">10+</h3>
                    <p className="why__number_text">YEARS OF EXPERIENCE</p>
                </div>
            </div>
            <div className="why__right_part">
                <h2 className="why__title">Why us?</h2>
                <p className="why__text">Only good things are said about us. But it is better to see and feel 1 time
                    than to read 10 times. We are working with the world-class equipment and proven-by-time
                    specialists.</p>
            </div>
        </section>
    )
}
