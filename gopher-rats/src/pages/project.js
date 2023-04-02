import React from 'react';
import { Link } from "react-router-dom";
import Hardware from './resources';

class project extends React.Component
{
    state = {
        Description: '',
        ExistingID: '',
    }

    handleSubmitExisting= (event) =>
    {
        //<Hardware ProjectID = {this.props.project.id}></Hardware>
        fetch(`/joinProject/${this.state.ExistingID}`,{ mode: "no-cors"})
            .then(response => response.text())    
            .then(data => {
                console.log(data)
            alert(`${data}`); //print out if it successfully joined existing one or not.
        })
        //checks if valid project
        //alert ('Welcome Back', this.state.ExistingID)
        event.preventDefault();
        //shows name of project and description
        //go to resources/hardware with ID prop 
        //<Hardware projectid={this.props.project.id}/>
    }

    handleExistingIDChange = event => {
        //check if ID exists already
        this.setState({ ExistingID: event.target.value });
      }

    render()
    {
        const{ExistingID} = this.state;

        return(
        <form onSubmit={this.handleSubmitExisting}>
            <div>
                <h1>Existing Projects:</h1>
                <h4>Enter Project ID:</h4>
                <input
                    type="text"
                    value={ExistingID}
                    onChange={this.handleExistingIDChange}
                    placeholder=""
                />
            </div>
          <button type="submit">Enter</button> <br></br>
          <button>
            <Link to="/newProject">Create new project</Link>
          </button>
          <br></br>
          <button>
            <Link to="/welcome">Log-Out</Link>
          </button>
        </form>
        
        )
    }
}

export default project;