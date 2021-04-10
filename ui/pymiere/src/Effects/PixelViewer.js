import React, { Component } from 'react';
import Button from '@material-ui/core/Button';

class PixelViewer extends Component {
  constructor(props) {
    super(props);
    this.state = {
      toggleOn: false,
      savedScale: [1, 1],
      pixelRatio: 20, // Size ratio of 1 real pixel to screen pixels
      text: "Off"
    }
  }

  Toggle = () => {
    const oldTransform = this.props.canvasTransform;
    
    let toggleState = this.state.toggleOn;
    this.setState({ toggleOn: !toggleState });
    this.setState({ text: this.state.toggleOn ? 'On' : 'Off'});
    
    if (this.state.toggleOn) {
      this.setState({ savedScale: [oldTransform[0], oldTransform[3]]});
      oldTransform[0] = this.state.pixelRatio;
      oldTransform[3] = this.state.pixelRatio;
    } else {
      oldTransform[0] = this.state.savedScale[0];
      oldTransform[3] = this.state.savedScale[1];
      oldTransform[4] = oldTransform[5] = 0; // Reset position too since the size reset will displaced the image
    }
    this.props.onTransform(oldTransform);
  }

  render() {
    return (
      <div>
        <Button variant="contained" color="primary" onClick={this.Toggle}>{this.state.text}</Button>
      </div>
    );
  }
}

export default PixelViewer;