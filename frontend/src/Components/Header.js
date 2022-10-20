import React, { Component }  from 'react';
import { useState } from 'react';
import { Container,Navbar, NavDropdown, Form, FormControl, Button, Nav, Modal, NavLink } from 'react-bootstrap'
import Anchor from 'react-bootstrap';
import logo from "../images/logo-small.png"
import { TextField, Dialog, DialogActions, DialogTitle, DialogContent, DialogContentText } from '@mui/material'
import LogIn from './LogIn';
//import "../../scss/header.css"
function BasicExample() {

  return (
    <Navbar bg="white" expand="md" fixed="top" >
      <div className='container main__container'>
        <Navbar.Brand href="#home"><img src={logo} alt="Logo" width="140px"></img></Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="header__nav" allignitems="center" justifycontent="center">
            <Nav.Link href="#hero" >About</Nav.Link>
            <Nav.Link href="#why" >Classes</Nav.Link>
            <Nav.Link href="#link" >Subscription plans</Nav.Link>
          </Nav>
          <LogIn/>
        </Navbar.Collapse>
      </div>
    </Navbar>
  );
}

export default BasicExample;

