import React, { Component } from "react";
import Slider from "@material-ui/core/Slider";
import Button from "@material-ui/core/Button";
import Paper from "@material-ui/core/Paper";
import CheckNSTFilters from "./CheckNSTFilters";

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
      newURL: ""
    };
  }

  handleChange = (e, v) => {
    this.setState({ generation: v }, () => {
      this.setState({newURL: this.state.baseURL + this.state.filterArray[this.state.generation]});
    });
    
    console.log("Test URL " + this.state.newURL);
  };

  handleIncrement = (event) => {
    let maxLen = this.state.filterArray.length - 1;
    if (this.state.generation < maxLen) {
      this.setState({generation: this.state.generation + 1}, () => {
        this.setState({newURL: this.state.baseURL + this.state.filterArray[this.state.generation]});
      });
    }
    console.log("generation: " + this.state.generation);
    console.log("Test URL " + this.state.newURL);
  }

  handleDecrement = (event) => {
    if (this.state.generation > 1) {
      this.setState({generation: this.state.generation - 1}, () => {
        this.setState({newURL: this.state.baseURL + this.state.filterArray[this.state.generation]});
      });
    }
    console.log("generation: " + this.state.generation);
    console.log("Test URL " + this.state.newURL);
  }

  confirmNSTFilter = () => {
    console.log("Filter number: " + this.state.generation);
    console.log("Filter type: " + this.state.nstType);
    //let params = {"filter_url": this.state.newURL}
    this.props.applyFilter("nst-filter", [this.state.newURL]);
  };

  changeNSTType = (event) => {
    this.setState({
      nstType: event.target.checked
    });
  }

  getFilterArray = () => {
    CheckNSTFilters().then((response) => {
      this.setState({filterArray: response.list}, () => {
        this.setState({newURL: this.state.baseURL + this.state.filterArray[1]})
      })
    })
  }

  componentDidMount() {
    this.getFilterArray()
    console.log("here");
    console.log(this.state.filterArray);
  }

  render() {
    return (
      <div width="auto">
        <h4>View NST Filters:</h4>
        <br />
        <Paper variant="outlined">
          <img src={this.state.newURL} style={{"max-width": "600px", "max-height": "600px"}}/>
        </Paper>
        <br />
        <br />
        <Button
          variant="contained"
          color="primary"
          onClick={this.handleDecrement}
        >
          Prev
        </Button>
        <Button
          variant="contained"
          color="primary"
          onClick={this.handleIncrement}
        >
          Next
        </Button>
        <br /><br />
        <Button
          variant="contained"
          color="primary"
          onClick={this.confirmNSTFilter}
        >
          Run NST
        </Button>
        <h3>Your image will be displayed once the algorithm finishes</h3>

        <br />
      </div>
    );
  }
}
