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
      aValue: "",
      watermarkName: "",
      watermarkPosition: "",
      watermarkSize: "",
      watermarkOpacity: "",
      backgroundName: "",
      opacityValue: 100,
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
    this.props.applyFilter("recoloration", [
      parseInt(this.state.rValue),
      parseInt(this.state.gValue),
      parseInt(this.state.bValue),
      parseInt(this.state.aValue),
    ]);
  };

  addWatermark = () => {
    console.log("watermark name: " + this.state.watermarkName);
    console.log("watermark position: " + this.state.watermarkPosition);
    console.log("watermark opacity: " + this.state.watermarkOpacity);
    console.log("watermark size: " + this.state.watermarkSize);
    this.props.applyFilter("watermark", [
      this.state.watermarkName,
      this.state.watermarkPosition,
      this.state.watermarkSize,
      this.state.watermarkOpacity,
    ]);
  };

  applyGaussianBlur = (e, val) => {
    this.setState({
      blurValue: val,
    });

  };

  changeOpacity = (e, val) => {
    this.setState({
      opacityValue: val,
    });
    
  };

  confirmOpacityChange = () => {
    console.log("Opacity: " + this.state.opacityValue);
    this.props.applyFilter("opacity", parseInt(this.state.opacityValue));
  }

  confirmBlurChange = () => {
    console.log("Opacity: " + this.state.blurValue);
    this.props.applyFilter("blur", parseInt(this.state.blurValue));
  }

  render() {
    return (
      <div>
        <h4>Change Opacity:</h4>
        <Slider
          value={this.state.opacityValue}
          onChange={this.changeOpacity}
          aria-labelledby="discrete-slider-small-steps"
          min={0}
          max={100}
          step={1}
          valueLabelDisplay="auto"
        ></Slider>
        <Button variant="contained" color="primary" onClick={this.confirmOpacityChange}>Change Opactiy</Button>

        <h4>Gaussian Blur:</h4>
        <Slider
          value={this.state.blurValue}
          onChange={this.applyGaussianBlur}
          aria-labelledby="discrete-slider-small-steps"
          min={0}
          max={9}
          step={1}
          valueLabelDisplay="auto"
        ></Slider>
        <Button variant="contained" color="primary" onClick={this.confirmBlurChange}>Change Blur</Button>

        <h4>Add Watermark:</h4>
        <TextField
          id="outlined-basic"
          value={this.state.watermarkName}
          onChange={this.handleChange("watermarkName")}
          label="Image Name"
          variant="outlined"
        />
        <br />
        <TextField
          id="outlined-basic"
          value={this.state.watermarkPosition}
          onChange={this.handleChange("watermarkPosition")}
          label="Position"
          variant="outlined"
        />
        <br />
        <TextField
          id="outlined-basic"
          value={this.state.watermarkSize}
          onChange={this.handleChange("watermarkSize")}
          label="Size"
          variant="outlined"
        />
        <br />
        <TextField
          id="outlined-basic"
          value={this.state.watermarkOpacity}
          onChange={this.handleChange("watermarkOpacity")}
          label="Opacity"
          variant="outlined"
        />
        <br />
        <br />
        <Button variant="contained" color="primary" disabled="true" onClick={this.addWatermark}>
          Add Watermark
        </Button>
        <br />
        <h4>Apply Recoloration Filter:</h4>
        <TextField
          id="outlined-basic"
          value={this.state.rValue}
          onChange={this.handleChange("rValue")}
          label="R Value (0 - 255)"
          variant="outlined"
        />
        <br />
        <TextField
          id="outlined-basic"
          value={this.state.gValue}
          onChange={this.handleChange("gValue")}
          label="G Value (0 - 255)"
          variant="outlined"
        />
        <br />
        <TextField
          id="outlined-basic"
          value={this.state.bValue}
          onChange={this.handleChange("bValue")}
          label="B Value (0 - 255)"
          variant="outlined"
        />
        <br />
        <TextField
          id="outlined-basic"
          value={this.state.aValue}
          onChange={this.handleChange("aValue")}
          label="A Value (0 - 255)"
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
