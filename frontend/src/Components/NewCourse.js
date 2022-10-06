import React  from 'react';
import {Button} from 'react-bootstrap';
import {useEffect} from 'react';
function CreateMarkup(){
    useEffect(() => {
                let counter=1;
                const renderPart=document.querySelector(".addcourse__render");
                const form=document.querySelector("form")
                const buttonAdd=document.querySelector(".addcourse__add");
                const buttonCreate=document.querySelector(".addcourse__create");
                form.addEventListener('submit',(evt)=>{
                    evt.preventDefault();
                    // const formData = new FormData(form);
                    // formData.get("course__name")
                    // const values=Object.fromEntries(formData.entries())
                    // console.log(values)
                    let fd = new FormData(form);

                    let data = {};

                    for (let [key, prop] of fd) {
                        if(!data[key])
                        {
                            data[key] = prop;
                        }
                        else{
                            const arr=[];
                            arr.push(...data[key])
                            arr.push(...prop)
                            data[key] =arr;
                        }
                    }

                    data = JSON.stringify(data, null, 2);

                    console.log(data);
                })
                
                



                buttonAdd.addEventListener("click",(evt)=>
                {
                    counter+=1;
                    evt.preventDefault();
                    const markup=`<h2 class='addcourse__option'>Option ${counter}</h2>
                    <div class='form__field'>
                    <label for="subs_name" class='form__label' >Name of subscription </label>
                    <input id='subs_name' class='form__input' name="subs_name"></input>
                </div>
                <div class='form__field'>
                    <label for="classes_number" class='form__label' >Number of classes </label>
                    <input id='classes_number' class='form__input' name="classes_number"></input>
                </div>
                <div class='form__field'>
                    <label for="duration" class='form__label' >Duration (days)</label>
                    <input id='duration' class='form__input' name="duration"></input>
                </div>
                <div class='form__field'>
                    <label for="price" class='form__label' >Price</label>
                    <input id='price' class='form__input' name="price"></input>
                </div>`
                    renderPart.insertAdjacentHTML("beforeend",markup)
                    })
                
                
            });
            

    return (
        <section className='main__container addcourse__container'>
            <h1 className='addcourse__title'>Add new course</h1>
            <form className='form__addcourse'>
                <div className='form__field'>
                    <label htmlFor="course_name" className='form__label'>Name of the course</label>
                    <input id='course_name' name='course_name' className='form__input'></input>
                </div>
                <div className='form__field'>
                    <label htmlFor="desc" className='form__label'>Description of the course</label>
                    <textarea id='desc' name='desc' className='form__textarea'></textarea>
                </div>
                <div className='form__field'>
                    <label htmlFor="type" className='form__label'>Type of the course</label>
                    <select id="type" name="type" className='form__select'>
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
                    <label htmlFor="subs_name" className='form__label' >Name of subscription </label>
                    <input id='subs_name' className='form__input' name="subs_name"></input>
                </div>
                <div className='form__field'>
                    <label htmlFor="classes_number" className='form__label' >Number of classes </label>
                    <input id='classes_number' className='form__input' name="classes_number"></input>
                </div>
                <div className='form__field'>
                    <label htmlFor="duration" className='form__label' >Duration (days)</label>
                    <input id='duration' className='form__input' name="duration"></input>
                </div>
                <div className='form__field'>
                    <label htmlFor="price" className='form__label' >Price</label>
                    <input id='price' className='form__input' name="price"></input>
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

// const App = () => {
//    
// }
// App();

// const form=document.querySelector("form");
// console.log(form);
// if(buttonAdd)
// {
//     buttonAdd.addEventListener("click",onAddClick)
//     console.log(buttonAdd)
// }

// function onAddClick(evt)
// {
// evt.preventDafault();
// const markup=`<h1>Hello<h1/>`
// form.insertAdjacentHTML("beforeend",markup)
// }
