//welcome page
//sign-in for returning user

import React from "react";
import { Link, Navigate } from "react-router-dom";

class welcome extends React.Component{
  state = {
    Username: '',
    UserID: '',
    Password: ''
  }
  
    handleUsernameChange = (event) => {
      this.setState({
        Username: event.target.value
      });
    }

    handleUserIDChange = event => {
      this.setState({ UserID: event.target.value });
      //check if ID exists already
    }

    handlePasswordChange = event => {
      this.setState({ Password: event.target.value });
      //check if correct password for this userID
    }
  
    handleUserSubmit = (event) => {
      fetch(`/checkSignIn/${this.state.UserID}, ${this.state.Password}`,{methods: 'GET', mode: "no-cors"})
        .then(response => response.text())    
        .then(data => {
            console.log(data)
          alert(`${data.projectId}`); //print out if it successfully signed in or not.
        })
 
      //alert(`Username: ${this.state.Username}`);
      //go to projects page
      //<Navigate to="/newProject" />;
      event.preventDefault();
    }


  render() {
    return (
      <div>
        <h1>Welcome to the GopherRats Hardware Site!</h1>
        <h4>Please sign in to continue:</h4>
        <form onSubmit={this.handleUserSubmit}>
            <label>
              UserName: 
              <input type="text"
                     value={this.state.Username} 
                     onChange={this.handleUsernameChange} 
                     placeholder=""
              />
            </label>
            <br />
            <label>
              UserID: 
              <input type="text" 
                     value={this.state.UserID} 
                     onChange={this.handleUserIDChange} 
                     placeholder=""
              />
            </label>
            <br />
            <label>
              password: 
              <input type="password" 
                     value={this.state.Password} 
                     onChange={this.handlePasswordChange} 
                     placeholder=""
              />
            </label>
            <br />
            <button type="submit">Submit</button>
        </form>
        <h4>If you are a new user please sign-up here:</h4>
        <button>
          <Link to="/newUser">Sign-Up</Link>
        </button>
      </div>
    )
  }
}
export default welcome;

