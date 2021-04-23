import React, { Component } from 'react';
import Button from '@material-ui/core/Button';

class CropEffect extends Component {
  constructor(props) {
    super(props);
    this.cropFrame = false;
    this.state = {
      cropFrameText: "Show"
    }
  }

  ToggleCropFrame = () => {
    this.cropFrame = !this.cropFrame;
    this.setState({ cropFrameText: this.cropFrame ? "Hide" : "Show" });

    let setFunction = null;
    if (this.cropFrame) {
      setFunction = "crop";
      const image = this.props.getCanvas("image");
      const functions = this.props.getCanvas("functions");
      let crop = functions.crop.boundingBox;
      crop[0] = image[5];
      crop[1] = image[6];
      crop[2] = image[3];
      crop[3] = image[4];
      this.props.setCanvas("functions", functions);
    }
    this.props.setCanvas("activeFunction", setFunction);
  }

  updateCropBackend = () => {
    let right = crop[0] + crop[2];
    let bottom = crop[1] + crop[3];
    this.props.applyFilter("crop", [crop[2], crop[3], crop[0], crop[1], right, bottom]);
  }

  Crop = () => {
    if (this.props.getCanvas("activeFunction")) {
      const crop = this.props.getCanvas("functions").crop.boundingBox;
      const image = this.props.getCanvas("image");

      image[1] = crop[0];
      image[2] = crop[1];
      image[3] = crop[2];
      image[4] = crop[3];
      image[5] = crop[0];
      image[6] = crop[1];
      image[7] = crop[2];
      image[8] = crop[3];

      this.props.setCanvas("image", image);
      this.ToggleCropFrame();
      this.updateCropBackend();
    }
  }

  componentWillUnmount() {
    if (this.cropFrame) {
      this.ToggleCropFrame();
    }
  }

  render() {
    return (
      <div>
        <Button variant="contained" color="primary" onClick={this.ToggleCropFrame}>{this.state.cropFrameText}</Button><br/>
        <Button variant="contained" color="primary" onClick={this.Crop}>Crop</Button>
      </div>
    );
  }
}

export default CropEffect;