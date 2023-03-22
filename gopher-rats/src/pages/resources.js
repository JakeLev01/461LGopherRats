import React from 'react';
import { TextField, Button } from '@material-ui/core';

class Hardware extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
    checkedOut: [100, 100],
    available: [100, 100],
    inputs: new Array(props.HWsets.length).fill(0),
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
    const { available, checkedOut, inputs } = this.state;
    return (
      <div>
        {this.props.HWsets.map((set, index) => (
            <div key={set}>
              <span>HWSet {set}: </span>
                <p>Available: {available[index]}/100</p><br/>
                <TextField
                    type="number"
                    label="Enter Quantity"
                    value={inputs[index]}
                    onChange={(event) => this.handleInput(event, index)}
                />
                <button onClick={() => this.handleCheckOut(index)}>
                    Check Out
                </button>
                <button onClick={() => this.handleCheckIn(index)}>
                    Check In
                </button>
            </div>
        ))}
      </div>
    )
  }
}

export default Hardware;