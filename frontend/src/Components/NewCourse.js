import React from 'react';
import {Button} from 'react-bootstrap';
import {useEffect} from 'react';
import axios from "axios";

function CreateMarkup() {
    useEffect(() => {
            let counter = 1;
            const renderPart = document.querySelector(".addcourse__render");
            const form = document.querySelector("form")
            const buttonAdd = document.querySelector(".addcourse__add");
            const buttonCreate = document.querySelector(".addcourse__create");
            form.addEventListener('submit', (evt) => {
                evt.preventDefault();
                let fd = new FormData(form);
                let data = {};
                let temp = {};
                let t = 0;
                data["sub_type"] = [];
                for (let [key, prop] of fd) {
                    if (key === "name" && t !== 0) {
                        data["sub_type"].push(temp);
                        temp = {};
                        temp[key] = prop;
                    } else if (key === "name" || key === "count" || key === "duration" || key === "price") {
                        temp[key] = prop;

                        if (key === "count" || key === "duration") {
                            temp[key] = parseInt(prop)
                        }

                        if (key === "price") {
                            temp[key] = parseFloat(prop)
                        }

                        t = 1;

                    } else {
                        data[key] = prop;
                    }
                }
                data["sub_type"].push(temp);
                // data = JSON.stringify(data, null, 2);

                axios.post('http://localhost:8080/courses', data
                    , {withCredentials: true})
                    .then(res => {
                            window.location = 'http://localhost:8080/courses';
                        }
                    )

                console.log(data);
                form.reset();
            })


            buttonAdd.addEventListener("click", (evt) => {
                counter += 1;
                evt.preventDefault();
                const markup = `<h2 class='addcourse__option'>Option ${counter}</h2>
                    <div class='form__field'>
                    <label for="name" class='form__label' >Name of subscription </label>
                    <input id='name' required minlength="3" maxlength="45" class='form__input' name="name"></input>
                </div>
                <div class='form__field'>
                    <label for="count" class='form__label' >Number of classes </label>
                    <input id='count' required type="number" class='form__input' name="count"></input>
                </div>
                <div className='form__field'>
                    <label htmlFor="duration" className='form__label'>Duration (days)</label>
                    <select id="duration" name="duration" className='form__select'>
                        <option value="30">30</option>
                        <option value="60">60</option>
                        <option value="90">90</option>
                    </select>
                </div>
                <div class='form__field'>
                    <label for="price" class='form__label' >Price</label>
                    <input id='price' required type="number" class='form__input' name="price"></input>
                </div>`
                renderPart.insertAdjacentHTML("beforeend", markup)
            })


        }
    )
    ;


    return (
        <section className='main__container addcourse__container'>
            <h1 className='addcourse__title'>Add new course</h1>
            <form className='form__addcourse'>
                <div className='form__field'>
                    <label htmlFor="course_name" className='form__label'>Name of the course</label>
                    <input id='course_name' required minLength={3} maxLength={45} name='course_name'
                           className='form__input'></input>
                </div>
                <div className='form__field'>
                    <label htmlFor="description" className='form__label'>Description of the course</label>
                    <textarea id='description' required minLength={10} maxLength={2000} name='description'
                              className='form__textarea'></textarea>
                </div>
                <div className='form__field'>
                    <label htmlFor="tag" className='form__label'>Tag of the course</label>
                    <select id="tag" name="tag" className='form__select'>
                        <option value="fitness">fitness</option>
                        <option value="box">box</option>
                        <option value="karate">karate</option>
                        <option value="yoga">yoga</option>
                        <option value="pilates">pilates</option>
                        <option value="strength">strength training</option>
                        <option value="aerobics">aerobics</option>
                        <option value="stretching">stretching</option>
                    </select>
                </div>
                <h2 className='addcourse__option'>Option 1</h2>
                <div className='form__field'>
                    <label htmlFor="name" className='form__label'>Name of subscription </label>
                    <input id='name' required minLength={3} maxLength={45} className='form__input'
                           name="name"></input>
                </div>
                <div className='form__field'>
                    <label htmlFor="count" className='form__label'>Number of classes </label>
                    <input id='count' required type={"number"} className='form__input'
                           name="count"></input>
                </div>
                <div className='form__field'>
                    <label htmlFor="price" className='form__label'>Price</label>
                    <input id='price' required type={"number"} className='form__input' name="price"></input>
                </div>
                <div className='form__field'>
                    <label htmlFor="duration" className='form__label'>Duration (days)</label>
                    <select id="duration" name="duration" className='form__select'>
                        <option value="30">30</option>
                        <option value="60">60</option>
                        <option value="90">90</option>
                    </select>
                </div>
                <div className='addcourse__render'>

                </div>
                <div className='form__buttons'>
                    <Button className='button addcourse__add' id="b">Add subscription</Button>
                    <Button className='button addcourse__create' type='submit'> Create course</Button>
                </div>
            </form>
        </section>
    )
}

export default CreateMarkup
