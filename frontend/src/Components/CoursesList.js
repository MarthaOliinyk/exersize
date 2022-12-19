import React, {useEffect, useState} from 'react';
import fetchPayment from './Payment';
import axios from "axios";

export default function CourseList() {
    const [data, setData] = useState(null);
    const getData = async () => {
        const dataAxios = await axios.get('http://localhost:8080/courses', {withCredentials: true});
        setData(dataAxios.data["courses"])
    }

    useEffect(() => {
        getData();
    }, []);

    useEffect(() => {
        if (data) {
            const list = document.querySelector(".courses__list")

            //cтворення курсів відповідно до запиту
            function createMarkup(data) {
                list.innerHTML = data.map(item => {
                    return `<li class="courses__item">
                    <p class="courses__line courses__line--name">
                    ${item.name}
                  </p>
                    <p class="courses__line"><b class="courses__title">Category : </b>${item.tag}</p>
                    <p class="courses__line"><b class="courses__title">Description : </b>${item.description} <span id="dots">...</span></p>
                    <div class="more">
                        <h2 class="courses__subs">Subscriptions</h2>
                        ${(item.sub_type).map(one => {
                        const id = one.id;

                        return `
                            <div class="courses__subscription">
                            <p class="courses__line courses__line--big ">
                            <input id="${id}" class="custom-checkbox" type="radio" data-course="${item.name}" name="subs" value="${one.name}" />
                            <label for="${id}">
                            
                            ${one.name}
                          </label> </p>
                            <p class="courses__line"><b class="courses__title">Classes number : </b>${one.session_count} </p>
                            <p class="courses__line"><b class="courses__title">Duration : </b>${one.duration} </p>
                            <p class="courses__line"><b class="courses__title">Price : </b>${one.price}₴ </p>
                            </div>
                            `
                    }).join("")}
                        </div>
                        <div class="courses__buttons">
                        <Button class=" courses__btn courses__btn--more "  >Read more</Button>
                        <Button disabled class=" courses__btn courses__btn--subs ">Subscribe</Button>
                        </div>
                        </li>
                       
                    `

                }).join("")

            }

            createMarkup(data);

            const btnMore = document.querySelectorAll(".courses__btn--more")
            const btnSunbscribe = document.querySelectorAll(".courses__btn--subs")
            const dots = document.querySelectorAll("#dots")
            const more = document.querySelectorAll(".more")

            //логіка кнопки 'Відкрити і скрити детальну інформацію'
            for (let i = 0; i < btnMore.length; i++) {
                btnMore[i].addEventListener("click", () => {
                    if (dots[i].style.display === "none") {
                        dots[i].style.display = "inline";
                        more[i].style.display = "none";
                        btnMore[i].innerHTML = "Read more"
                    } else {
                        dots[i].style.display = "none"
                        more[i].style.display = "inline";
                        btnMore[i].innerHTML = "Hide"
                    }
                });
            }

            //логіка обирання типу підписки, disabled кнопки і збирання даних
            for (let i = 0; i < btnSunbscribe.length; i++) {
                const checkbox = document.querySelectorAll(".custom-checkbox")
                for (let j = 0; j < checkbox.length; j++) {
                    checkbox[j].addEventListener("click", () => btnSunbscribe[i].removeAttribute("disabled"))
                }

                const selectedType = {}
                btnSunbscribe[i].addEventListener("click", () => {
                    const selected = document.querySelector("input:checked")
                    selectedType["tag"] = selected.value;
                    selectedType["name"] = selected.dataset.course;
                    console.log(selected.id)
                    fetchPayment(selected.id)
                });
            }

            //логіка search
            const searchForm = document.querySelector(".search")
            const searchInput = document.querySelector(".input")
            searchForm.addEventListener("submit", (evt) => {
                evt.preventDefault();
                console.log(searchInput.value)
                for (let i = 0; i < data.length; i++) {
                    if (data[i].name.includes(searchInput.value)) {
                        createMarkup([data[i]])
                    }
                }
                searchForm.reset();
            });
        }
    }, [data])

    return (<section className='main__container courses__container'>
            <h1 className='courses__header'>All courses</h1>
            <form action="" className="search">
                <input type="search" name="" placeholder="Search" className="input"/>
                <input type="submit" name="" value="" className="submit"/>
            </form>
            <ul className='courses__list'>
            </ul>
        </section>
    )
}
