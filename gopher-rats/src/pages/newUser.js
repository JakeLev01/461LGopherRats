import React from 'react';
import { Link } from "react-router-dom";
import { Navigate } from "react-router-dom";

//new user page 
class newUser extends React.Component {
    state = {
        Username: '',
        UserID: '',
        Password: '',
        ConfirmPassword: ''
    }


    handleUsernameChange = (event) => {
        this.setState({Username: event.target.value});
    }

    handleUserIDChange = event => {
        this.setState({ UserID: event.target.value });
        //check if ID exists already
    }

    handlePasswordChange = event => {
        this.setState({ Password: event.target.value });
    }

    handleConfirmPasswordChange = event => {
        this.setState({ ConfirmPassword: event.target.value });
    }

    handleNewUserSubmit = event => {
        if (this.state.Password !== this.state.ConfirmPassword) {
            alert('Passwords do not match');
            event.preventDefault();
        } else {
            fetch(`/createNewUser/${this.state.UserID}/${this.state.Password}/${this.state.Username}`,{methods: 'GET', mode: "no-cors"})
            .then(response => response.text())    
            .then(data => {
                console.log(data)
            alert(`${data}`); //print out if it successfully made new user or not
            if (`${data}` == "Account Successfully created")
                return <Navigate to = "/project" />;
            })
        }
    }

    render() {
        const { Username, UserID, Password, ConfirmPassword } = this.state;

        return (
            <form onSubmit={this.handleNewUserSubmit}>
                <div>
                    <h1>Sign-Up:</h1>
                    <h3>Username:</h3>
                    <input
                        type="text"
                        value={Username}
                        onChange={this.handleUsernameChange}
                        placeholder=""
                    />
                    <h3>New UserID:</h3>
                    <input
                        type="text"
                        value={UserID}
                        onChange={this.handleUserIDChange}
                        placeholder=""
                    />
                    <h3>New Password:</h3>
                    <input
                        type="password"
                        value={Password}
                        onChange={this.handlePasswordChange}
                        placeholder=""
                    />
                    <h4>Confirm Password:</h4>
                    <input
                        type="password"
                        value={ConfirmPassword}
                        onChange={this.handleConfirmPasswordChange}
                        placeholder=""
                    />
                </div>
                <button style={{ marginBottom: '30px' }} type="submit">Submit</button> <br></br>
                <button>
                    <Link to="/welcome">Go back</Link>
                </button>
            </form>
        )
    }
}

export default newUser;
