import React, { Component } from 'react';
import "./CenterImagePage.css"
import VerticalTabs from './EffectsOptionsMenu'
import EditingCanvas from "./EditingCanvas.js"

class CenterImagePage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      canvasTransform: [1, 0, 0, 1, 0, 0],
      canvasRef: React.createRef()
    }
  }

  handleCanvasTransform = (newTransform) => {
    this.setState({ canvasTransform: newTransform });
    this.child.setState({ canvasTransform: newTransform })
  }

  render(){
    return (
      //three horizontal boxes taking up the entire vertical space 
      //List of different effects
      //UI for view of current effect options
      //View Image
      <div id="mainImageUIandEffectsBar">
        <VerticalTabs canvasTransform={this.state.canvasTransform} onTransform={this.handleCanvasTransform}/>
        <div id="imageDisplay">
          <EditingCanvas ref={ref => (this.child = ref)} canvasRef={this.state.canvasRef} canvasTransform={this.state.canvasTransform}/>
        </div>
      </div>
    );
  }
}

export default CenterImagePage;