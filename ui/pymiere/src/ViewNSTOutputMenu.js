import React, { Component } from 'react';
import Slider from '@material-ui/core/Slider';
import Button from '@material-ui/core/Button'

export default class ViewNSTOutputMenu extends Component {
  constructor(props) {
    super(props);
    this.state = {
      generation: 1
    }
  }

  handleChange = (e, v) => {
    this.setState({ generation: v });
  }

  confirmNSTOutput = () => {
    console.log(this.state.generation);
    this.props.applyFilter("nst-view", [this.state.generation]);
  }

  render() {
    return (<div width="auto">
      <h4>View NST outputs</h4><br/>
      <Slider
            value={this.state.generation}
            onChange={this.handleChange}
            aria-labelledby="discrete-slider-small-steps"
            min={1}
            max={10}
            step={1}
            valueLabelDisplay="auto"
          ></Slider>
        <p>{this.state.generation}</p>
        <Button variant="contained" color="primary" disabled="true" onClick={this.confirmNSTOutput}>Select NST View</Button>

    </div>);
  }
}