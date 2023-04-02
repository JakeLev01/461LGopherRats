import React from 'react';
import { Link } from "react-router-dom";
import { Button, TextField } from '@material-ui/core';


class Hardware extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
    checkedOut: [100, 100],
    available: [100, 100], //get from database
    HWsets: [1,2],
    inputs: new Array(2).fill(0)
    };
  }

  handleCheckIn = (index) => {
    const { available, checkedOut, inputs } = this.state;
    const input = inputs[index];

    fetch(`/checkIn/${this.state.index}/${this.state.inputs[index]}/${this.state.ProjectID}`,{methods: 'GET', mode: "no-cors"})
      .then(response => response.text())    
      .then(data => {
        console.log(data)
        this.setState({available: `${data.available}`});
      alert(`${data.checkedOut}`); //print out if it successfully checkedin or not
      })
    };

  handleCheckOut = (index) => {
    const { available, checkedOut, inputs } = this.state;
    const input = inputs[index];

    fetch(`/checkIn/${this.state.index}/${this.state.inputs[index]}/${this.state.ProjectID}`,{methods: 'GET', mode: "no-cors"})
      .then(response => response.text())    
      .then(data => {
        console.log(data)
        this.setState({available: `${data.available}`});
      alert(`${data.checkedOut}`); //print out if it successfully checkedin or not
      })
    };

  handleInput = (event, index) => {
    const { inputs } = this.state;
    const newInputs = [...inputs];
    newInputs[index] = Number(event.target.value);
    this.setState({
      inputs: newInputs,
    });
  };

  render() {
    const { available, checkedOut, inputs, HWsets} = this.state;
    const projectID= this.props.ProjectID;
    return (
      <div>
        {HWsets.map((set, index) => (
            <div key={set}>
              <span>HWSet {set}: </span>
                <p>Available: {projectID.available[index]}/100</p><br/>
                <TextField
                    type="number"
                    label="Enter Quantity"
                    value={inputs[index]}
                    onChange={(event) => this.handleInput(event, index)}
                />
                <Button variant="contained" color="primary" onClick={() => this.handleCheckOut(index)}>
                    Check Out
                </Button>
                <Button variant="contained" color="secondary" onClick={() => this.handleCheckIn(index)}>
                    Check In
                </Button>
                <button> 
                  <Link to="/project">Leave Project</Link>
                </button>
                <button>
                  <Link to="/welcome">Log-Out</Link>
                </button>
            </div>
        ))}
      </div>
    )
  }
}

export default Hardware;
