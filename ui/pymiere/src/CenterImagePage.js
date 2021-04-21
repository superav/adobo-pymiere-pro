import React, { Component } from 'react';
import "./CenterImagePage.css"
import VerticalTabs from './EffectsOptionsMenu'
import EditingCanvas from "./EditingCanvas.js"

class CenterImagePage extends Component {
  constructor(props) {
    super(props);
  }

  // Methods for interacting with canvas. All interactions should be happend through these calls
  handleSetCanvas = (property, value) => {
    this.canvas.setCanvasState(property, value);
  }

  handleGetCanvas = (property, value) => {
    return this.canvas.getCanvasState(property, value);
  }

  render(){
    return (
      //three horizontal boxes taking up the entire vertical space 
      //List of different effects
      //UI for view of current effect options
      //View Image
      <div id="mainImageUIandEffectsBar">
        <VerticalTabs getCanvas={this.handleGetCanvas} setCanvas={this.handleSetCanvas}/>
        <div id="imageDisplay">
          <EditingCanvas ref={ref => (this.canvas = ref)}/>
        </div>
      </div>
    );
  }
}

export default CenterImagePage;