import React, { Component } from "react";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import Slider from "@material-ui/core/Slider";
import CropEffect from "./Effects/CropEffect";

class ChangeContrast extends Component {
  constructor(props) {
    super(props);
    this.state = {
      contrastValue: 50,
    };
  }

  handleContrastValueChange = (e, val) => {
    this.setState({
      contrastValue: val,
    });
  };

  contrastImage = () => {
    console.log("contrast by: " + this.state.contrastValue);
    // this.props.applyFilter("contrast", parseFloat(this.state.contrastValue))
  };

  render() {
    return (
      <div>
        <h4>Change Contrast:</h4>
        <Slider
          value={this.state.contrastValue}
          onChange={this.handleContrastValueChange}
          aria-labelledby="discrete-slider-small-steps"
          min={0}
          max={100}
          step={5}
          valueLabelDisplay="auto"
        ></Slider>
        <br />
        <br />
        <Button variant="contained" color="primary" onClick={this.contrastImage}>
          Apply
        </Button>
      </div>
    );
  }
}

export default ChangeContrast;
