import React, { Component } from 'react';
import Button from '@material-ui/core/Button';

class ZoomEffect extends Component {
  constructor(props) {
    super(props);
    this.zoomStep = 0.25;
    this.minZoom = 0.25;
    this.maxZoom = 10;
    this.state = {
      zoomLvl: 1
    };
  }

  zoomIn = () => {
    var newZoomLvl = this.state.zoomLvl + this.zoomStep;
    if (newZoomLvl <= this.maxZoom) {
      this.setState({ zoomLvl: newZoomLvl });
      const oldTransform = this.props.canvasTransform;
      oldTransform[0] = newZoomLvl;
      oldTransform[3] = newZoomLvl;
      this.props.onTransform(oldTransform);
    }
  }

  zoomOut = () => {
    var newZoomLvl = this.state.zoomLvl - this.zoomStep;
    if (newZoomLvl >= this.minZoom) {
      this.setState({ zoomLvl: newZoomLvl });
      const oldTransform = this.props.canvasTransform;
      oldTransform[0] = newZoomLvl;
      oldTransform[3] = newZoomLvl;
      this.props.onTransform(oldTransform);
    }
  }

  render() {
    return (
      <div>
         <h4>Zoom Percentage {this.state.zoomLvl * 100} %</h4>
            <Button variant="contained" color="primary" onClick={this.zoomIn}>In</Button>
            <Button variant="contained" color="primary" onClick={this.zoomOut}>Out</Button>
      </div>
    );
  }
}

export default ZoomEffect;