import React, {Component} from 'react';
import {useState} from 'react';
import {Button} from 'react-bootstrap'
import {TextField, Dialog, DialogActions, DialogTitle, DialogContent, DialogContentText} from '@mui/material'
import SignUp from './SignUp';
import Axios from 'axios';

export default function LogIn() {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => {
        setOpen(true);
    }
    const handleClose = () => {
        setOpen(false);
    }
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const handleSubmit = async (e) => {

        e.preventDefault()
        if (username && password) {
            Axios.post("http://localhost:8080/login",
                {
                    username: username,
                    password: password
                },
                {withCredentials: true}
            ).then(res => {
                if (res.status === 200) {
                    localStorage.setItem("registered", "true");
                    window.location.reload();
                }
                console.log(res)
            })
                .catch(error => {
                    console.log(error);
                    localStorage.setItem("registered", "false")
                })

            setOpen(false);
            setUsername("")
            setPassword("")
        }
        setOpen(false);
    }

    const logout = () => {
        Axios.post("http://localhost:8080/logout", {}, {withCredentials: true})
            .then(res => {
                localStorage.setItem("registered", "false")
                if (res.status === 200) {
                    window.location.reload();
                }
                console.log(res)
            })
            .catch(error => {
                console.log(error);
            })
        setOpen(false);
    };

    return (
        <div>
            <Button className="btn"
                    onClick={() => {
                        if (localStorage.getItem("registered") === "false" || localStorage.getItem("registered") === null) handleOpen(); else logout();
                    }}>{localStorage.getItem("registered") === "true" ? "Log out" : "Log in"}</Button>
            <Dialog open={open} onClose={handleClose} aria-labelledby="Log in" maxWidth="md">
                <form className="logInForm" noValidate autoComplete='off' onSubmit={handleSubmit}>
                    {localStorage.getItem("registered") === null || localStorage.getItem("registered") === "false" ?
                        <>
                            <DialogTitle id="Log in" style={{fontWeight: 'bold', fontSize: 40}}>Log in</DialogTitle>
                            <DialogContent>
                                <DialogContentText>Log in to continue your training journey!</DialogContentText>
                                <DialogContentText>Not a member yet? Click sign up!</DialogContentText>
                                <TextField
                                    className="username"
                                    autoFocus
                                    margin="dense"
                                    id="username"
                                    label="Username"
                                    type="username"
                                    fullWidth
                                    value={username}
                                    onChange={(e) => setUsername(e.target.value)}
                                />
                                <TextField className="password"
                                           margin="dense"
                                           id="password"
                                           label="Password"
                                           type="password"
                                           fullWidth
                                           value={password}
                                           onChange={(e) => setPassword(e.target.value)}
                                />
                            </DialogContent>
                            <DialogActions style={{justifyContent: "space-between", marginRight: 10, marginLeft: 10}}>
                                <SignUp/>
                                <Button type='submit'>Log in</Button>
                            </DialogActions>
                        </> :
                        <Button type='submit' onClickCapture={() => {
                            if (localStorage.getItem("registered") === "false") {
                                handleOpen()
                            } else {
                                logout();
                            }
                        }
                        }>Log out</Button>
                    }
                </form>

            </Dialog>
        </div>
    );
}
