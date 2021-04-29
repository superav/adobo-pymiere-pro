import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import Slider from '@material-ui/core/Slider';
import Typography from '@material-ui/core/Typography';

class PencilTool extends Component {
  constructor(props) {
    super(props);
    this.pencilTool = false;
    this.canvas = React.createRef();
    this.state = {
      buttonText: "Show Pencil",
      R: 0,
      G: 0,
      B: 0,
      size: 4
    }
  }
  
  componentDidMount() {
    const pencil = this.props.getCanvas("functions").pencil;
    this.setState({
      R: pencil.fill[0],
      G: pencil.fill[1],
      B: pencil.fill[2],
      size: pencil.width
    });
    this.updateCanvas();
  }

  componentWillUnmount() {
    if (this.pencilTool)
      this.TogglePencilTool();
  }

  TogglePencilTool = () => {
    this.pencilTool = !this.pencilTool;
    this.setState({ buttonText: this.pencilTool ? "Hide Pencil" : "Show Pencil" });

    let setFunction = null;
    if (this.pencilTool) {
      setFunction = "pencil";
      const functions = this.props.getCanvas("functions");
      this.props.setCanvas("functions", functions);
    }
    this.props.setCanvas("activeFunction", setFunction);
  }

  handleRChange = (e, v) => {
    this.setState({ R: v });
    this.setColor();
  }
  
  handleGChange = (e, v) => {
    this.setState({ G: v });
    this.setColor();
  }
  
  handleBChange = (e, v) => {
    this.setState({ B: v });
    this.setColor();
  }

  setColor = () => {
    const functions = this.props.getCanvas("functions");
    functions.pencil.fill = [this.state.R, this.state.G, this.state.B];
    functions.pencil.currentStroke.fill = functions.pencil.fill;
    this.props.setCanvas("functions", functions);
    this.updateCanvas();
  }

  handleSizeChange = (e, v) => {
    this.setState({ size: v });
    const functions = this.props.getCanvas("functions");
    functions.pencil.width = v;
    functions.pencil.currentStroke.width = functions.pencil.width;
    this.props.setCanvas("functions", functions);
    this.updateCanvas();
  }

  updateCanvas = () => {
    const ctx = this.canvas.current.getContext('2d');
    ctx.clearRect(0, 0, 100, 100);
    ctx.beginPath();
    ctx.arc(50, 50, this.state.size/2, 0, 2*Math.PI);
    ctx.fillStyle = `rgb(
      ${this.state.R},
      ${this.state.G},
      ${this.state.B})`;
    ctx.fill();
  }

  confirmPencilChanges = () => {
    const strokes = this.props.getCanvas("functions").pencil.strokes;
    strokes.forEach(stroke => {
      stroke.points.map((point) => {
        point[0] = parseFloat(point[0]);
        point[1] = parseFloat(point[1]);
        return point;
      });
      stroke.fill.map((num) => {return parseInt(num)});
      this.props.applyFilter("draw-line", [stroke.points, parseInt(stroke.width), stroke.fill]);
      // TODO create a way to wait for response for each stroke before sending the next stroke. Maybe create progress bar?
    });
  }

  render() {
    return <div>
      <Button
        variant="contained"
        color="primary"
        onClick={this.TogglePencilTool}>
          {this.state.buttonText}
      </Button>
      
      <Typography id="color" gutterBottom>
      <b>Color</b>
      </Typography>
      
      <Typography id="input-slider" gutterBottom>
      {this.state.R}
      </Typography>
      <Slider
      value={this.state.R}
        onChange={this.handleRChange}
        aria-labelledby="input-slider"
        valueLabelDisplay="auto"
        min={0}
        max={255}
      />
      
      <Typography id="input-slider" gutterBottom>
      {this.state.G}
      </Typography>
      <Slider
      value={this.state.G}
        onChange={this.handleGChange}
        aria-labelledby="input-slider"
        valueLabelDisplay="auto"
        min={0}
        max={255}
      />

      <Typography id="input-slider" gutterBottom>
      {this.state.B}
      </Typography>
      <Slider
      value={this.state.B}
        onChange={this.handleBChange}
        aria-labelledby="input-slider"
        valueLabelDisplay="auto"
        min={0}
        max={255}
      />

      <Typography id="Size" gutterBottom>
      <b>Size: {this.state.size}</b>
      </Typography>
      <Slider
      value={this.state.size}
        onChange={this.handleSizeChange}
        aria-labelledby="input-slider"
        valueLabelDisplay="auto"
        min={1}
        max={50}
      />

      <canvas ref={this.canvas} width={100} height={100}/>
      <br></br>
      <Button variant="contained" color="primary" onClick={this.confirmPencilChanges}>Save Drawing</Button>
    </div>
  }
}

export default PencilTool;