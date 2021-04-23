import React, { Component } from "react";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import Slider from "@material-ui/core/Slider";

class TransformationEditingMenu extends Component {
  constructor(props) {
    super(props);
    this.state = {
      rValue: "",
      gValue: "",
      bValue: "",
      watermarkName: "",
      watermarkPosition: "",
      watermarkSize: "",
      watermarkOpacity: "",
      backgroundName: "",
      opacityValue: 1,
      blurValue: 1,
    };
  }

  handleChange = (name) => (event) => {
    this.setState({ [name]: event.target.value });
  };

  applyRecolorationFilter = () => {
    console.log("r value: " + this.state.rValue);
    console.log("g value: " + this.state.gValue);
    console.log("b value: " + this.state.bValue);
  };

  addWatermark = () => {
    console.log("watermark name: " + this.state.watermarkName);
    console.log("watermark position: " + this.state.watermarkPosition);
    console.log("watermark opacity: " + this.state.watermarkOpacity);
    console.log("watermark size: " + this.state.watermarkSize);
  };

  changeBackground = () => {
    console.log("background name: " + this.state.backgroundName);
  };

  applyGaussianBlur = (e, val) => {
    this.setState({
      blurValue: val,
    });
    console.log("Gaussian blur: " + this.state.blurValue);
  };

  changeOpacity = (e, val) => {
    this.setState({
      opacityValue: val,
    });
    console.log("Opacity: " + this.state.opacityValue);
  };

  render() {
    return (
      <div>
        <h4>Change Opacity:</h4>
        <Slider
          value={this.state.opacityValue}
          onChangeCommitted={this.changeOpacity}
          aria-labelledby="discrete-slider-small-steps"
          min={0}
          max={1}
          step={0.1}
          valueLabelDisplay="auto"
        ></Slider>
        <h4>Gaussian Blur:</h4>
        <Slider
          value={this.state.blurValue}
          onChangeCommitted={this.applyGaussianBlur}
          aria-labelledby="discrete-slider-small-steps"
          min={0}
          max={1}
          step={0.1}
          valueLabelDisplay="auto"
        ></Slider>
        <h4>Change Background:</h4>
        <TextField
          id="outlined-basic"
          value={this.state.backgroundName}
          onChange={this.handleChange('backgroundName')}
          label="Background Name"
          variant="outlined"
        />
        <br />
        <br />
        <Button
          variant="contained"
          color="primary"
          onClick={this.changeBackground}
        >
          Select Background
        </Button>
        <h4>Add Watermark:</h4>
        <TextField
          id="outlined-basic"
          value={this.state.watermarkName}
          onChange={this.handleChange('watermarkName')}
          label="Image Name"
          variant="outlined"
        />
        <br />
        <TextField
          id="outlined-basic"
          value={this.state.watermarkPosition}
          onChange={this.handleChange('watermarkPosition')}
          label="Position"
          variant="outlined"
        />
        <br />
        <TextField
          id="outlined-basic"
          value={this.state.watermarkSize}
          onChange={this.handleChange('watermarkSize')}
          label="Size"
          variant="outlined"
        />
        <br />
        <TextField
          id="outlined-basic"
          value={this.state.watermarkOpacity}
          onChange={this.handleChange('watermarkOpacity')}
          label="Opacity"
          variant="outlined"
        />
        <br />
        <br />
        <Button variant="contained" color="primary" onClick={this.addWatermark}>
          Add Watermark
        </Button>
        <br />
        <h4>Apply Recoloration Filter:</h4>
        <TextField
          id="outlined-basic"
          value={this.state.rValue}
          onChange={this.handleChange('rValue')}
          label="R Value"
          variant="outlined"
        />
        <br />
        <TextField
          id="outlined-basic"
          value={this.state.gValue}
          onChange={this.handleChange('gValue')}
          label="G Value"
          variant="outlined"
        />
        <br />
        <TextField
          id="outlined-basic"
          value={this.state.bValue}
          onChange={this.handleChange('bValue')}
          label="B Value"
          variant="outlined"
        />
        <br />
        <br />
        <Button
          variant="contained"
          color="primary"
          onClick={this.applyRecolorationFilter}
        >
          Apply Recoloration
        </Button>
      </div>
    );
  }
}

export default TransformationEditingMenu;
