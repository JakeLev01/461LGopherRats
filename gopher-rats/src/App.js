import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom';
import Welcome from './pages/welcome';
import NewUser from './pages/newUser';
import Greeting from './Conditional_rendering';
import NewProject from './pages/newProject';
import Project from './pages/project';
import Resources from './pages/resources';
import React from 'react';

export const UserContext = React.createContext(null);


class App extends React.Component {
  render () {
    return (
      <div className="App">
        <BrowserRouter>
          <Routes>
            <Route exact path="/" element={<Welcome />} />
            <Route path="/newUser" element={<NewUser />} />
            
            <Route path="/welcome" element={<Welcome />} />
            <Route path="/newProject" element={<NewProject />} />

            <Route path="/project" element={<Project />} />
            <Route path="/resources" element={<Resources />} />
          </Routes>
        </BrowserRouter>
      </div>
    );
  }
}

export default App;

