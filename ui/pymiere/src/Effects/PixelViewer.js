import React, { Component } from 'react';
import Button from '@material-ui/core/Button';

class PixelViewer extends Component {
  constructor(props) {
    super(props);
    this.state = {
      canvas: <canvas id="Pixel Canvas"/>,
      savedScale: [1, 1],
    }
    this.pixelRatio = 20; // Size ratio of 1 real pixel to screen pixels
    this.toggleOn = false;
    this.text = "Off";
  }

  Toggle = () => {
    const oldTransform = this.props.canvasTransform;
    
    this.toggleOn = !this.toggleOn;
    this.text = this.toggleOn ? "On" : "Off";
    
    if (this.toggleOn) {
      this.setState({ savedScale: [oldTransform[0], oldTransform[3]]});
      oldTransform[0] = this.pixelRatio;
      oldTransform[3] = this.pixelRatio;
    } else {
      oldTransform[0] = this.state.savedScale[0];
      oldTransform[3] = this.state.savedScale[1];
      oldTransform[4] = oldTransform[5] = 0; // Reset position too since the size reset will displaced the image
    }
    this.props.onTransform(oldTransform);
  }

  componentWillUnmount() {
    if (this.toggleOn) {
      this.Toggle();
    }
  }

  render() {
    return (
      <div>
        <Button variant="contained" color="primary" onClick={this.Toggle}>{this.text}</Button><br/>
        <canvas />
      </div>
    );
  }
}

export default PixelViewer;