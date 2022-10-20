import React, { Component, useEffect }  from 'react';
// import { Button } from 'react-bootstrap'


  
 
export default function CourseList()
{
        
    useEffect(()=>
    {
        
        
        const data=[{
            "subs_type": [
              {
                "subs_name": "Simple",
                "classes_number": "5",
                "duration": "7",
                "price": "1200"
              },
              {
                "subs_name": "Top",
                "classes_number": "6",
                "duration": "10",
                "price": "1997"
              },
              {
                "subs_name": "Premium",
                "classes_number": "20",
                "duration": "60",
                "price": "4000"
              }
            ],
            "course_name": "Sport",
            "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ac elit quam. Ut ornare mauris nisi, vitae vehicula lorem faucibus accumsan. Sed a ornare enim. Curabitur semper nulla vel pretium viverra. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aenean iaculis, quam sed fermentum aliquam, nisl felis tristique magna, pharetra semper tortor risus non purus. Morbi commodo egestas vestibulum. Sed imperdiet eu velit ut accumsan.\nDonec dapibus nibh nibh, facilisis auctor justo bibendum eu. Phasellus erat nibh, volutpat eu sodales et, mollis ac magna. Duis interdum efficitur enim id pulvinar. Maecenas pretium vulputate laoreet. Sed eleifend efficitur enim a placerat. Donec et vestibulum diam. Nullam fringilla dolor justo, quis aliquet turpis congue nec.",
            "type": "fitness"
          },
          {
            "subs_type": [
              {
                "subs_name": "Simple",
                "classes_number": "5",
                "duration": "7",
                "price": "1200"
              },
              {
                "subs_name": "Top",
                "classes_number": "6",
                "duration": "10",
                "price": "1997"
              },
              {
                "subs_name": "Premium",
                "classes_number": "20",
                "duration": "60",
                "price": "4000"
              }
            ],
            "course_name": "Fitnessomania",
            "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ac elit quam. Ut ornare mauris nisi, vitae vehicula lorem faucibus accumsan. Sed a ornare enim. Curabitur semper nulla vel pretium viverra. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aenean iaculis, quam sed fermentum aliquam, nisl felis tristique magna, pharetra semper tortor risus non purus. Morbi commodo egestas vestibulum. Sed imperdiet eu velit ut accumsan.\nDonec dapibus nibh nibh, facilisis auctor justo bibendum eu. Phasellus erat nibh, volutpat eu sodales et, mollis ac magna. Duis interdum efficitur enim id pulvinar. Maecenas pretium vulputate laoreet. Sed eleifend efficitur enim a placerat. Donec et vestibulum diam. Nullam fringilla dolor justo, quis aliquet turpis congue nec.",
            "type": "fitness"
          },
          {
            "subs_type": [
              {
                "subs_name": "First",
                "classes_number": "7",
                "duration": "10",
                "price": "1300"
              },
              {
                "subs_name": "Second",
                "classes_number": "10",
                "duration": "30",
                "price": "1800"
              },
              {
                "subs_name": "Third",
                "classes_number": "30",
                "duration": "70",
                "price": "5000"
              }
            ],
            "course_name": "Yogoman",
            "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ac elit quam. Ut ornare mauris nisi, vitae vehicula lorem faucibus accumsan. Sed a ornare enim. Curabitur semper nulla vel pretium viverra. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aenean iaculis, quam sed fermentum aliquam, nisl felis tristique magna, pharetra semper tortor risus non purus. Morbi commodo egestas vestibulum. Sed imperdiet eu velit ut accumsan.\nDonec dapibus nibh nibh, facilisis auctor justo bibendum eu. Phasellus erat nibh, volutpat eu sodales et, mollis ac magna. Duis interdum efficitur enim id pulvinar. Maecenas pretium vulputate laoreet. Sed eleifend efficitur enim a placerat. Donec et vestibulum diam. Nullam fringilla dolor justo, quis aliquet turpis congue nec. dbchbhdchbchbhbdcbhcbhbchdbhc",
            "type": "yoga"
          }]
        const list=document.querySelector(".courses__list")
          function createMarkup(data)
          {
            const markup= data.map(item=>
                {
                    return `<li class="courses__item">
                    <p class="courses__line courses__line--name">
                    ${item.course_name}
                  </p>
                    <p class="courses__line"><b class="courses__title">Category : </b>${item.type}</p>
                    <p class="courses__line"><b class="courses__title">Description : </b>${item.desc} <span id="dots">...</span></p>
                    <div class="more">
                        <h2 class="courses__subs">Subscriptions</h2>
                        ${(item.subs_type).map(one=> {
                          
                            return `
                            <div class="courses__subscription">
                            <p class="courses__line courses__line--big ">
                            <input id="${item.course_name}_${one.subs_name}" class="custom-checkbox" type="radio" data-course="${item.course_name}" name="subs" value="${one.subs_name}" />
                            <label for="${item.course_name}_${one.subs_name}">
                            
                            ${one.subs_name}
                          </label> </p>
                            <p class="courses__line"><b class="courses__title">Classes number : </b>${one.classes_number} </p>
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
                   
                }).join("");
                
                list.innerHTML=markup 
        
          }
          createMarkup(data)
          const btnMore=document.querySelectorAll(".courses__btn--more")
          const btnSunbscribe=document.querySelectorAll(".courses__btn--subs")
          const dots=document.querySelectorAll("#dots")
          const more=document.querySelectorAll(".more")
        for (let i = 0; i < btnMore.length; i++) {
            btnMore[i].addEventListener("click",()=>{
                if(dots[i].style.display==="none")
                {
                 dots[i].style.display="inline";
                 more[i].style.display="none";
                 btnMore[i].innerHTML="Read more"
                }
                else{
                    dots[i].style.display="none"
                    more[i].style.display="inline";
                    btnMore[i].innerHTML="Hide"
                }
            });
            };

            for (let i = 0; i < btnSunbscribe.length; i++) {
              const checkbox=document.querySelectorAll(".custom-checkbox")
              for(let j=0;j<checkbox.length;j++)
              {
                checkbox[j].addEventListener("click",()=>btnSunbscribe[i].removeAttribute("disabled"))
              }
              
              const selectedType={}
              btnSunbscribe[i].addEventListener("click",()=>{
                const selected=document.querySelector("input:checked")
                  selectedType["type"]=selected.value;
                  selectedType["course_name"]=selected.dataset.course;
                  console.log(selectedType)
              });
              };
        

        })
    
return(<section className='main__container courses__container'>
<h1 className='courses__header'>All courses</h1>
<ul className='courses__list'>
</ul>


</section>
)
}
