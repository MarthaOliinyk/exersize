import React, {Component} from 'react';
import {useState} from 'react';
import {Button} from 'react-bootstrap'
import {TextField, Dialog, DialogActions, DialogTitle, DialogContent, DialogContentText} from '@mui/material'
import SignUp from './SignUp';


export default function LogIn() {

    const data = {}
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => {
        setOpen(true);
    }
    const handleClose = () => {
        setOpen(false);
    }
    const [email, setEmail] = useState("")
    const [pass, setPass] = useState("")
    const handleSubmit = (e) => {
        e.preventDefault()

        if (email && pass) {
            data["logInEmail"] = email
            data["logInPassword"] = pass
            console.log(data)
        }
    }


    return (
        <div className='A'>
            <Button className="btn" onClick={handleOpen}>Log in</Button>
            <Dialog open={open} onClose={handleClose} aria-labelledby="Log in" maxWidth="md">
                <form className="logInForm" noValidate autoComplete='off' onSubmit={handleSubmit}>
                    <DialogTitle id="Log in" style={{fontWeight: 'bold', fontSize: 40}}>Log in</DialogTitle>
                    <DialogContent>
                        <DialogContentText>Log in to continue your training journey!</DialogContentText>
                        <DialogContentText>Not a member yet? Click sign up!</DialogContentText>
                        <TextField
                            className="email"
                            autoFocus
                            margin="dense"
                            id="email"
                            label="Email address"
                            type="email"
                            fullWidth
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                        />
                        <TextField className="pass"
                                   autoFocus
                                   margin="dense"
                                   id="pass"
                                   label="Password"
                                   type="password"
                                   fullWidth
                                   value={pass}
                                   onChange={(e) => setPass(e.target.value)}
                        />
                    </DialogContent>
                    <DialogActions style={{justifyContent: "space-between", marginRight: 10, marginLeft: 10}}>
                        <SignUp/>
                        <Button type='submit'>Log in</Button>
                    </DialogActions>
                </form>

            </Dialog>
        </div>
    );
}

