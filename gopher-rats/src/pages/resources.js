import React from 'react';
import { Link, useLocation} from "react-router-dom";
//import ProjectContext from './projectContext';
//import currentProjectID from "./projectContext";

class resources extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      projectID: localStorage.getItem("projectID"),
      checkedOut: [0, 0],
      available: [100, 100], //get from database
      HWsets : [1,2],
      inputs: new Array(2).fill(0),
    };
  }

  componentDidMount() {
    this.fetchAvailability();
  }

  fetchAvailability = () => {
    const { projectID, HWsets, available, checkedOut } = this.state;
    HWsets.forEach((set, index) => {
    fetch(`/check_out/${projectID}/${0}/${set}`)
      .then(response => response.json())    
      .then(data => {
        console.log(data);
        if(data === "Invalid Quantity"){
          alert(data)
        }
        else{
          this.setState({ available: [...available.slice(0, index), data.availability, ...available.slice(index + 1)] });
          this.setState({ checkedOut: [...checkedOut.slice(0, index), data.checkedout, ...checkedOut.slice(index + 1)] });
        }
        
        
      })
    });
  }

  handleCheckIn = (index) => {
    const { available, inputs, checkedOut, projectID, HWsets } = this.state;
    const input = inputs[index];
    if(input >= 0){
      fetch(`/check_in/${projectID}/${input}/${HWsets[index]}`)
      .then(response => response.json())    
      .then(data => {
        console.log(data);
        if(data === "Invalid Quantity"){
          alert(data)
        }
        else{
        this.setState({ available: [...available.slice(0, index), data.availability, ...available.slice(index + 1)] });
        this.setState({ checkedOut: [...checkedOut.slice(0, index), data.checkedout, ...checkedOut.slice(index + 1)] });
        }
        
      })
    }
    
  }

  handleCheckOut = (index) => {
    const { available, inputs, checkedOut, projectID, HWsets } = this.state;
    const input = inputs[index];
    if(input >= 0){
      fetch(`/check_out/${projectID}/${input}/${HWsets[index]}`)
      .then(response => response.json())    
      .then(data => {
        console.log(data);
        if(data === "Invalid Quantity"){
          alert(data)
        }
        else{
          this.setState({ available: [...available.slice(0, index), data.availability, ...available.slice(index + 1)] });
          this.setState({ checkedOut: [...checkedOut.slice(0, index), data.checkedout, ...checkedOut.slice(index + 1)] });
        }
        
        
      })
    }
    
  }

  handleInput = (event, index) => {
    const { inputs } = this.state;
    const newInputs = [...inputs];
    newInputs[index] = Number(event.target.value);
    this.setState({
      inputs: newInputs,
    });
  }

  render() {
    const { available, checkedOut, inputs, HWsets, projectID } = this.state;
    
    return (
      <div>
        <h2>Project ID: {projectID}</h2><br/>
        {HWsets.map((set, index) => (
          <div key={set}>
            <span>HWSet {set}: </span>
            <p>Available: {available[index]}/100</p>
            <p>Checked Out: {checkedOut[index]}</p><br/>
            <input
              type="number"
              label="Enter Quantity"
              value={inputs[index]}
              onChange={(event) => this.handleInput(event, index)}
            />
            <button onClick={() => this.handleCheckOut(index)}>
              Check Out
            </button>
            <button  onClick={() => this.handleCheckIn(index)}>
              Check In
            </button>
            <p></p>
            </div>
        ))}
        <button> 
              <Link to="/project">Leave Project</Link>
            </button>
            <button>
              <Link to="/welcome">Log-Out</Link>
            </button>
      </div>
    )
  }
}

export default resources;
