import React, { Component } from 'react';
import Slider from '@material-ui/core/Slider';

export default class ViewNSTOutputMenu extends Component {
  constructor(props) {
    super(props);
    this.state = {
      generation: this.props.defaultGeneration
    }
  }

  handleChange = (e, v) => {
    this.setState({ generation: v });
  }

  render() {
    return (<div width="auto">
      <h4>View NST outputs</h4><br/>
      <Slider
        width="auto"
        value={this.state.generation}
        onChange={this.handleChange}
        aria-labelledby="slider"
        valueLabelDisplay="on"
        step={this.props.step}
        min={this.props.min}
        max={this.props.max}
        marks={this.props.marks}
      />
    </div>);
  }
}