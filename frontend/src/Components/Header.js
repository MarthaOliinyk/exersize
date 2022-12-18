import React, {Component} from 'react';
import {useEffect, useState} from 'react';
import {Container, Navbar, NavDropdown, Form, FormControl, Button, Nav, Modal, NavLink} from 'react-bootstrap'
import logo from "../images/logo-small.png"
import LogIn from './LogIn';
import axios from 'axios';

function BasicExample() {
    const [role, setRole] = useState("");

    async function getData() {
        axios.get("http://localhost:8080/users/roles", {withCredentials: true})
            .then((data) => setRole(() => getRoles(data)))
            .catch(console.log);
    }

    function getRoles(roles) {
        const arrOfRoles = [];
        roles.data.roles.map((role) => arrOfRoles.push(role.role))
        if (arrOfRoles.includes("coach")) {
            return "coach"
        } else if (arrOfRoles.includes("user")) {
            return "user"
        } else if (arrOfRoles.includes("admin")) {
            return "admin"
        }
    }

    getData().then(r => console.log(r))

    return (
        <Navbar bg="white" expand="md" fixed="top">
            <div className='container main__container'>
                <Navbar.Brand href="/"><img src={logo} alt="Logo" width="140px"></img></Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav"/>
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="header__nav">
                        {role === "coach" ? <Nav.Link href='/create'>Create</Nav.Link> : null}
                        <Nav.Link href='/'>About</Nav.Link>
                        <Nav.Link href='/courses'>Courses</Nav.Link>
                    </Nav>
                    <LogIn/>
                </Navbar.Collapse>
            </div>
        </Navbar>
    );
}

export default BasicExample;
