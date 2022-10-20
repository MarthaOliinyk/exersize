import React  from 'react';
import sprite from "../sprite.svg";
import pic1 from "../images/gallery1.jpg"
import pic2 from "../images/gallery2.jpg"
import pic3 from "../images/gallery3.jpg"
import pic4 from "../images/gallery4.jpg"
import pic5 from "../images/gallery5.jpg"
import pic6 from "../images/gallery6.jpg"
import pic7 from "../images/gallery7.jpg"
import pic8 from "../images/gallery8.jpg"

export default function GallerryMarkup()
{
    return(
        <section >
            <div className="gallery__top">
                <ul className="gallery__list">
                    <li className="gallery__item">
                        <img className="gallery__img img-fluid" src={pic7} alt="gallery"></img>
                    </li>
                    <li className="gallery__item">
                        <img className="gallery__img img-fluid" src={pic1} alt="gallery"></img>
                    </li>
                    <li className="gallery__item">
                        <img className="gallery__img img-fluid" src={pic2} alt="gallery"></img>
                    </li>
                    <li className="gallery__item">
                        <img className="gallery__img img-fluid" src={pic3} alt="gallery"></img>
                    </li>
                </ul>
            </div>
            <div className="gallery__middle">
            <ul className="gallery__links">
                    <li className="gallery__link">
                        <svg className="gallery__svg">
                            <use href={sprite + "#icon-facebook"}></use>
                        </svg>
                        <p className='gallery__social'>@exersize</p>
                    </li>
                    <li className="gallery__link">
                        <svg className="gallery__svg">
                            <use href={sprite + "#icon-instagram"}></use>
                        </svg>
                        <p className='gallery__social'>@exersize</p>
                    </li>
                    <li className="gallery__link">
                        <svg className="gallery__svg">
                            <use href={sprite + "#icon-telegram"}></use>
                        </svg>
                        <p className='gallery__social'>ExerSize</p>
                    </li>
                    <li className="gallery__link">
                        <svg className="gallery__svg">
                            <use href={sprite + "#icon-twitter"}></use>
                        </svg>
                        <p className='gallery__social'>ExerSize</p>
                    </li>
                </ul>
            </div>
            <div className="gallery__bottom">
            <ul className="gallery__list">
                    <li className="gallery__item">
                        <img className="gallery__img img-fluid" src={pic4} alt="gallery"></img>
                    </li>
                    <li className="gallery__item">
                        <img className="gallery__img img-fluid" src={pic5} alt="gallery"></img>
                    </li>
                    <li className="gallery__item">
                        <img className="gallery__img img-fluid" src={pic6} alt="gallery"></img>
                    </li>
                    <li className="gallery__item">
                        <img className="gallery__img img-fluid" src={pic8} alt="gallery"></img>
                    </li>
                </ul>
            </div>
        </section>
    )
}
