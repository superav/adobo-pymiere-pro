import React, { Component } from "react";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import Slider from "@material-ui/core/Slider";
import CropEffect from "./Effects/CropEffect";

class SizeEditingMenu extends Component {
  constructor(props) {
    super(props);
    this.state = {
      shrinkValue: 1,
    };
  }

  handleShrinkValueChange = (e, val) => {
    this.setState({
      shrinkValue: val,
    });
  };

  shrinkImage = () => {
    console.log("shrink by: " + this.state.shrinkValue);
    this.props.applyFilter("downscale-resolution", [this.state.shrinkValue])
  };

  render() {
    return (
      <div>
        <h4>Crop:</h4>
        <CropEffect
          getCanvas={this.props.getCanvas}
          setCanvas={this.props.setCanvas}
          applyFilter={this.props.applyFilter}
        ></CropEffect>
        <h4>Shrink:</h4>
        <Slider
          value={this.state.shrinkValue}
          onChangeCommitted={this.handleShrinkValueChange}
          aria-labelledby="discrete-slider-small-steps"
          min={0}
          max={1}
          step={0.1}
          valueLabelDisplay="auto"
        ></Slider>
        <br />
        <br />
        <Button variant="contained" color="primary" onClick={this.shrinkImage}>
          Shrink
        </Button>
      </div>
    );
  }
}

export default SizeEditingMenu;
