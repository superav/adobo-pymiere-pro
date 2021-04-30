import React, { Component } from "react";
import Button from "@material-ui/core/Button";
import Slider from "@material-ui/core/Slider";

class RotateImage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      rotateValue: 180
    };
  }

  handleRotateValueChange = (e, val) => {
    this.setState({
      rotateValue: val,
    });
  };

  rotateImage = () => {
    console.log("rotate by: " + this.state.rotateValue);
    this.props.applyFilter("rotate", parseInt(this.state.rotateValue));
  };

  render() {
    return (
      <div>
        <h4>Rotate:</h4>
        <Slider
          value={this.state.rotateValue}
          onChange={this.handleRotateValueChange}
          aria-labelledby="discrete-slider-small-steps"
          min={0}
          max={360}
          step={10}
          valueLabelDisplay="auto"
        ></Slider>
        <br />
        <br />
        <Button variant="contained" color="primary" onClick={this.rotateImage}>
          Rotate
        </Button>
      </div>
    );
  }
}

export default RotateImage;
