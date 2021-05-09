import './App.css';
import ImageUIPage from './ImageUIPage'
import ProjectSelectPage from './ProjectSelectPage'
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";

import React, { Component } from 'react';

class App extends Component {

  constructor(props) {
    super(props)
    this.handleImageSelect = this.handleImageSelect.bind(this)
    this.state = { selectedImage: "https://upload.wikimedia.org/wikipedia/commons/c/c9/-Insert_image_here-.svg"}
  }

  handleImageSelect(image, event) {
    if (!image.includes("/images/new.svg")) {
      this.setState({ selectedImage: image })
    } else {
      this.setState({ selectedImage: "https://upload.wikimedia.org/wikipedia/commons/c/c9/-Insert_image_here-.svg"})
    }
  }

  render() {
    return (
      <Router>
        <Switch>
          <Route path="/image">
            <ImageUIPage selectedImage={this.state.selectedImage}/>
          </Route>
          <Route path="/">
            <ProjectSelectPage imageSelectHandler={this.handleImageSelect}/>
          </Route>
        </Switch>
      </Router>

    );
  }

  
}

export default App;
