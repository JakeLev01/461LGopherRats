import React from 'react';
import { Button, TextField } from '@material-ui/core';


class Hardware extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
    checkedOut: [100, 100],
    available: [100, 100],
    HWsets: [1, 2], 
    inputs: new Array(2).fill(0),
  };
  this.handleCheckIn = this.handleCheckIn.bind(this);
  this.handleCheckOut = this.handleCheckOut.bind(this);
  }

  handleCheckIn = (index) => {
    const { available, checkedOut, inputs } = this.state;
    const input = inputs[index];
    if (input <= checkedOut[index] && available[index] + input <= 100) {
      checkedOut[index] -= input;
      available[index] += input;
      const newInputs = [...inputs];
      newInputs[index] = 0;
      this.setState({
        checkedOut,
        available,
        inputs: newInputs,
      });

      const projectId = this.props.projectid;
      fetch(`/hardware/checkin/${projectId}/${input}`)
        .then(response => response.json())
        .then(data => {
          console.log('Check-in successful:', data);
        })
        .catch(error => {
          console.error('Error checking in:', error);
        });
    }
    else{
      const newInputs = [...inputs];
      newInputs[index] = 0;
      this.setState({
        checkedOut,
        available,
        inputs: newInputs,
      });
    }
    alert(input + ' hardware checked in');
  };

  handleCheckOut = (index) => {
    const { available, checkedOut, inputs } = this.state;
    const input = inputs[index];
    if (input <= available[index] && available[index] - input >= 0) {
      available[index] -= input;
      checkedOut[index] += input;
      const newInputs = [...inputs];
      newInputs[index] = 0;
      this.setState({
        checkedOut,
        available,
        inputs: newInputs,
      });

      const projectId = this.props.projectid;
      fetch(`/hardware/checkout/${projectId}/${input}`)
        .then(response => response.json())
        .then(data => {
          console.log('Check-out successful:', data);
        })
        .catch(error => {
          console.error('Error checking out:', error);
        });
    }
    else{
      const newInputs = [...inputs];
      newInputs[index] = 0;
      this.setState({
        checkedOut,
        available,
        inputs: newInputs,
      });
    }

    alert(input + ' hardware checked out');
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
        {HWsets.map((set, index) => (
            <div key={set}>
              <span>HWSet {set}: </span>
                <p>Available: {available[index]}/100</p><br/>
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
            </div>
        ))}
      </div>
    )
  }
}

export default Hardware;
