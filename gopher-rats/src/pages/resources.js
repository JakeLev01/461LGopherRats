import React from 'react';
import { Button, TextField } from '@material-ui/core';


class Hardware extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
    checkedOut: [100, 100],
<<<<<<< HEAD
    available: [100, 100],
    HWsets: [1, 2], 
    inputs: new Array(2).fill(0),
  };
  this.handleCheckIn = this.handleCheckIn.bind(this);
  this.handleCheckOut = this.handleCheckOut.bind(this);
=======
    available: [100, 100], //get from database
    inputs: new Array(2).fill(0)
    };
>>>>>>> a0e33693a36d368cdbb30556ec442fdfb4f901af
  }

  handleCheckIn = (index) => {
    const { available, checkedOut, inputs } = this.state;
    const input = inputs[index];
<<<<<<< HEAD
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
=======

    fetch(`/checkIn/${this.state.index}/${this.state.inputs[index]}/${this.state.ProjectID}`,{methods: 'GET', mode: "no-cors"})
      .then(response => response.text())    
      .then(data => {
        console.log(data)
        this.setState({available: `${data.available}`});
      alert(`${data.checkedOut}`); //print out if it successfully checkedin or not
      })
    };
>>>>>>> a0e33693a36d368cdbb30556ec442fdfb4f901af

  handleCheckOut = (index) => {
    const { available, checkedOut, inputs } = this.state;
    const input = inputs[index];
<<<<<<< HEAD
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
=======

    fetch(`/checkIn/${this.state.index}/${this.state.inputs[index]}/${this.state.ProjectID}`,{methods: 'GET', mode: "no-cors"})
      .then(response => response.text())    
      .then(data => {
        console.log(data)
        this.setState({available: `${data.available}`});
      alert(`${data.checkedOut}`); //print out if it successfully checkedin or not
      })
    };
>>>>>>> a0e33693a36d368cdbb30556ec442fdfb4f901af

  handleInput = (event, index) => {
    const { inputs } = this.state;
    const newInputs = [...inputs];
    newInputs[index] = Number(event.target.value);
    this.setState({
      inputs: newInputs,
    });
  };

  render() {
<<<<<<< HEAD
    const { available, checkedOut, inputs, HWsets } = this.state;
=======
    const { available, checkedOut, inputs } = this.state;
    const projectID= this.props.ProjectID;
>>>>>>> a0e33693a36d368cdbb30556ec442fdfb4f901af
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
<<<<<<< HEAD
                </Button>
=======
                </button>
                <button>
                  <Link to="/welcome">Log-Out</Link>
                </button>
>>>>>>> a0e33693a36d368cdbb30556ec442fdfb4f901af
            </div>
        ))}
      </div>
    )
  }
}

export default Hardware;
