import React from 'react';
import { Link , Navigate} from "react-router-dom";
import Hardware from './resources';
//import ProjectContext from './projectContext';
//import currentProjectID from "./currentProject";

class project extends React.Component
{
    state = {
        Description: '',
        ExistingID: '',
    }

    handleSubmitExisting= (event) =>
    {
        //const history = useHistory();
        if (this.state.ExistingID && this.state.ExistingID.trim() !== '') {
            fetch(`/joinProject/${this.state.ExistingID}`,{ mode: "no-cors"})
            .then(response => response.text())    
            .then(data => {
                console.log(data)
            alert(`${data}`); //print out if it successfully joined existing one or not.
            if (`${data}` == "Successfully joined project")
            //setProjectID(this.state.ProjectID); // set the project ID to the context
                return <Navigate to = "/resources" />;
                //history.push(`/resources/${ExistingID}`);
            })
        event.preventDefault();
        //shows name of project and description
        //go to resources/hardware with ID prop 
        }else{
            alert("Please enter valid project information")
        }

    
    }

    handleExistingIDChange = event => {
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
            <Link to={'/resources'}>Next page</Link>
            
          </button><br></br>
          <h4>or create a new project:</h4>
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