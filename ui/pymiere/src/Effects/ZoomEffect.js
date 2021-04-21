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

  updateZoom = (newZoomLvl) => {
    this.setState({ zoomLvl: newZoomLvl });
    const oldTransform = this.props.getCanvas("transform");
    oldTransform[0] = newZoomLvl;
    oldTransform[3] = newZoomLvl;
    this.props.setCanvas("transform", oldTransform);
  }

  zoomIn = () => {
    var newZoomLvl = this.state.zoomLvl + this.zoomStep;
    if (newZoomLvl <= this.maxZoom) {
      this.updateZoom(newZoomLvl);
    }
  }

  zoomOut = () => {
    var newZoomLvl = this.state.zoomLvl - this.zoomStep;
    if (newZoomLvl >= this.minZoom) {
      this.updateZoom(newZoomLvl);
    }
  }

  componentDidMount() {
    this.setState({ zoomLvl: this.props.getCanvas("transform")[0] })
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