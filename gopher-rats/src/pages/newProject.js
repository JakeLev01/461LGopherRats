import React from 'react';
import { Link } from "react-router-dom";
import { Navigate } from "react-router-dom";
import Hardware from "./resources";
//import ProjectContext from './projectContext';
//import {currentProjectID} from "./currentProject";

class newProject extends React.Component {
  state = {
    Name: '',
    Description: '',
    ProjectID: '',
  }

  handleSubmitProject = (event) => {
    if(this.state.ProjectID.trim() && this.state.Name.trim() && this.state.Description.trim() != null){
        fetch(`/addNewProject/${this.state.ProjectID}/${this.state.Name}/${this.state.Description}`,{methods: 'GET', mode: "no-cors"})
      .then(response => response.text())    
      .then(data => {
        console.log(data)
      alert(`${data}`); //print out if it successfully signed in or not.
      if (`${data}` == "Successfully added new project") {
        //setProjectID(this.state.ProjectID); // set the project ID to the context
        window.location.href = "/resources";
      }
      })
    event.preventDefault();
    //go to resources/hardware with ID prop 
    }
    else{
      alert("Please enter valid project information")
    }
  }

  handleNameChange = (event) => {
    this.setState({ Name: event.target.value });
  }

  handleDescriptionChange = (event) => {
    this.setState({ Description: event.target.value });
  }

  handleProjectIDChange = (event) => {
    this.setState({ ProjectID: event.target.value });
  }


  render() {
    const { Name, Description, ProjectID } = this.state;

    return (
      <div>
        <form onSubmit={this.handleSubmitProject}>
          <div>
            <h1>Create a New Project</h1>
            <h3>Name:</h3>
            <input
              type="text"
              value={Name}
              onChange={this.handleNameChange}
              placeholder=""
            />
            <h3>Description:</h3>
            <input
              type="text"
              value={Description}
              onChange={this.handleDescriptionChange}
              placeholder=""
            />
            <h4>Project ID:</h4>
            <input
              type="text"
              value={ProjectID}
              onChange={this.handleProjectIDChange}
              placeholder=""
            />
          </div>
          <button type="submit">Create Project</button><br></br>
        </form>
        <h4>Or use an existing project:</h4>
        <button>
          <Link to="/project">use existing project</Link>
        </button><br></br>
        <button>
            <Link to="/welcome">Log-Out</Link>
          </button>
      </div>
    )
  }
}

export default newProject;
