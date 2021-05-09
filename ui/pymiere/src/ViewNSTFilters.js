import React, { Component } from "react";
import Slider from "@material-ui/core/Slider";
import Button from "@material-ui/core/Button";
import Paper from "@material-ui/core/Paper";

export default class ViewNSTFilters extends Component {
  constructor(props) {
    super(props);
    this.state = {
      nstType: true,
      generation: 1,
      baseURL: "https://adobo-pymiere.s3.amazonaws.com/",
      filterArray: [
        "styles/",
        "styles/test_style_1.jpg",
        "styles/test_style_2.jpg",
        "styles/wave.jpg",
        "styles/wave.png",
      ],
      newURL: "https://adobo-pymiere.s3.amazonaws.com/styles/test_style_1.jpg"
    };
  }

  handleChange = (e, v) => {
    this.setState({ generation: v }, () => {
      this.setState({newURL: this.state.baseURL + this.state.filterArray[this.state.generation]});
    });
    
    console.log("Test URL " + this.state.newURL);
  };

  confirmNSTFilter = () => {
    console.log("Filter number: " + this.state.generation);
    console.log("Filter type: " + this.state.nstType);
    this.props.applyFilter("nst-filter", [this.state.newURL]);
  };

  changeNSTType = (event) => {
    this.setState({
      nstType: event.target.checked
    });
  }

  getFilterArray = () => {
      // Get filter array instead of hardcoding
  }

  render() {
    return (
      <div width="auto">
        <h4>View NST Filters:</h4>
        <br />
        <Paper variant="outlined">
          <img src={this.state.newURL} style={{"max-width": "600px", "max-height": "600px"}}/>
        </Paper>
        <Slider
          value={this.state.generation}
          onChange={this.handleChange}
          aria-labelledby="discrete-slider-small-steps"
          min={1}
          max={this.state.filterArray.length}
          step={1}
          valueLabelDisplay="auto"
        ></Slider>
        <p>{this.state.generation}</p>
        <br />
        <Button
          variant="contained"
          color="primary"
          onClick={this.confirmNSTFilter}
        >
          Run NST
        </Button>

        <br />
      </div>
    );
  }
}
