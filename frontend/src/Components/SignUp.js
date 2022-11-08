import React, {Component} from 'react';
import {useState} from 'react';
import {Button} from 'react-bootstrap'
import {TextField, Dialog, DialogActions, DialogTitle, DialogContent, DialogContentText} from '@mui/material'
import Axios from 'axios';

export default function SignUp() {
    const [open, setOpen] = React.useState(false);

    const handleOpen = () => {
        setOpen(true);
    }
    const handleClose = () => {
        setOpen(false);
    }
    const data = {}
    const [email, setEmail] = useState("")
    const [password, setPass] = useState("")
    const [username, setUsername] = useState("")
    const [fname, setFname] = useState("")
    const [lname, setLname] = useState("")
    const handleSubmit = (e) => {
        e.preventDefault()

        if (email && password && username && fname && lname) {
            data["First name"] = fname
            data["Last name"] = lname
            data["Username"] = username
            data["Email"] = email
            data["Password"] = password
            Axios.post('https://localhost:8080', {
                fname,
                lname,
                username,
                email,
                password
              })
              .then((response) => {
                console.log(response);
              }, (error) => {
                console.log(error);
              });
        }
    }


    return (
        <div>
            <Button onClick={handleOpen}>Sign up</Button>
            <Dialog open={open} onClose={handleClose} aria-labelledby="Log in" maxWidth="md">
                <form className="logInForm" noValidate autoComplete='off' onSubmit={handleSubmit}>
                    <DialogTitle id="Sign up" style={{fontWeight: 'bold', fontSize: 40}}>Sign Up</DialogTitle>
                    <DialogContent>
                        <DialogContentText>Start your training journey right now!</DialogContentText>
                        <TextField
                            autoFocus
                            margin="dense"
                            id="first name"
                            label="First name"
                            type="firstName"
                            fullWidth
                            value={fname}
                            onChange={(e) => setFname(e.target.value)}
                        />
                        <TextField
                            
                            margin="dense"
                            id="last name"
                            label="Last name"
                            type="lastName"
                            fullWidth
                            value={lname}
                            onChange={(e) => setLname(e.target.value)}
                        />
                        <TextField
                            
                            margin="dense"
                            id="username"
                            label="Username"
                            type="username"
                            fullWidth
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                        />
                        <TextField
                            
                            margin="dense"
                            id="email"
                            label="Email"
                            type="email"
                            fullWidth
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                        />
                        <TextField
                            
                            margin="dense"
                            id="password"
                            label="Password"
                            type="password"
                            fullWidth
                            value={password}
                            onChange={(e) => setPass(e.target.value)}
                        />
                    </DialogContent>
                    <DialogActions style={{justifycontent: "center"}}>
                        <Button type="submit" onClick={handleSubmit}>Continue</Button>
                    </DialogActions>
                </form>
            </Dialog>
        </div>
    );
}