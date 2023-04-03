import React from 'react';
import { Link } from "react-router-dom";
import { Button, TextField } from '@material-ui/core';
import currentProjectID from "/Users/lk/461LGopherRats/gopher-rats/src/currentProject";

class resources extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      checkedOut: [0, 0],
      available: [100, 100], //get from database
      HWsets : [1,2],
      inputs: new Array(2).fill(0),
    };
  }

  handleCheckIn = (index) => {
    const { available, inputs, checkedOut } = this.state;
    const input = inputs[index];

    fetch(`/checkIn/${currentProjectID}/${input}/${index}`, { method: 'GET', mode: "no-cors" })
      .then(response => response.json())    
      .then(data => {
        console.log(data);
        if(data !== "Invalid Quantity"){
          this.setState({ available: [...available.slice(0, index), data.available, ...available.slice(index + 1)] });
          this.setState({ checkedOut: [...checkedOut.slice(0, index), data.checkedout, ...checkedOut.slice(index + 1)] });
        }
      })
  };

  handleCheckOut = (index) => {
    const { available, inputs, checkedOut } = this.state;
    const input = inputs[index];

    fetch(`/checkOut/${currentProjectID}/${input}/${index}`, { method: 'GET', mode: "no-cors" })
      .then(response => response.json())    
      .then(data => {
        console.log(data);
        if(data !== "Invalid Quantity"){
          this.setState({ available: [...available.slice(0, index), data.available, ...available.slice(index + 1)] });
          this.setState({ checkedOut: [...checkedOut.slice(0, index), data.checkedout, ...checkedOut.slice(index + 1)] });
        }
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
    const { available, checkedOut, inputs, HWsets } = this.state;

    return (
      <div>
        <h2>Project ID: {currentProjectID}</h2><br/>
        {HWsets.map((set, index) => (
          <div key={set}>
            <span>HWSet {set}: </span>
            <p>Available: {available[index]}/100</p><br/>
            <p>Checked Out: {checkedOut[index]}</p><br/>
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

export default resources;
