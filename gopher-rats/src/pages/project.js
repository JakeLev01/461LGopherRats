import React from 'react';
import { Link } from "react-router-dom";

class project extends React.Component
{
    state = {
        Name: '',
        Description: '',
        ExistingID: '',
    }

    handleSubmitExisting= (event) =>
    {
        //checks if valid project
        alert ('Welcome Back', this.state.ExistingID)
        event.preventDefault();
        //shows name of project and description
        //go to resources/hardware with ID prop 
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
          <button type="submit">Enter</button>
          <br></br>
          <button>Log-Out</button>
        </form>
        )
    }
}

export default project;