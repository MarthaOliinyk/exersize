import LoggedHeader from "./LoggedHeader"
import Footer from "./Footer"
import { Button, Image } from "react-bootstrap"
import person from "../images/person.png"

export default function Profile() {
    return (
        <div>
            <LoggedHeader/>
            <div className="container">
                <div className="group">
                    <div className="personalInfo">
                        <text className="personalInfoText">PERSONAL INFO</text>
                        <img className="person" src={person}></img>
                        <Button className="buttonGo1">GO</Button>
                    </div>
                    <div className="scheduledClasses">
                        <text className="scheduledClassesText">SCHEDULED CLASSES</text>
                        <img className="calendar" src={calendar}></img>
                        <Button className="buttonGo2">GO</Button>
                    </div>
                    <div className="paymentInfo">
                        <text className="paymentInfoText">PAYMENT INFO</text>
                        <img className="payment" src={payment}></img>
                        <Button className="buttonGo3">GO</Button>
                    </div>
                </div>
                <Footer/>
            </div>
        </div>
    )
}
