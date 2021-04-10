import React, { Component } from 'react';
import "./EditingCanvas.css";

class EditingCanvas extends Component {

  constructor(props) {
    super(props);
    this.img = null;
    this.mouseDown = false
    this.state = {
      canvasRef: this.props.canvasRef,
      canvasTransform: this.props.canvasTransform
    }
  }

  componentDidMount() {
    // Get parent sizes (TODO Fix dom reference)
    const parent = document.getElementById('imageDisplay');
    let width = parent.offsetWidth;
    let height = parent.offsetHeight;
    
    const canvas = this.state.canvasRef.current;
    canvas.width = width;
    canvas.height = height;
    const context = canvas.getContext('2d');
    const img = new Image();
    img.src = "logo512.png";
    img.onload = () => {
      this.img = img;
      context.drawImage(img, 0, 0);
    }
  }

  componentDidUpdate() {
    let width = this.state.canvasRef.current.width;
    let height = this.state.canvasRef.current.height;

    // Update context
    const ctx = this.state.canvasRef.current.getContext('2d');
    ctx.save(); // Store current transform
    ctx.setTransform(1, 0, 0, 1, 0, 0); // Reset transform
    ctx.clearRect(0, 0, width, height); // Clear the canvas
    ctx.restore(); // Restore the current transform
    ctx.setTransform(...this.state.canvasTransform);
    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(this.img, 0, 0);
  }

  handleMouseDown = (e) => {
    this.mouseDown = true;
  }

  handleMouseMove = (e) => {
    if (!this.mouseDown) return;

    var x = e.movementX;
    var y = e.movementY;

    //this.state.canvasRef.current.getContext('2d').translate(x, y);
    var newTransform = this.state.canvasTransform;
    newTransform[4] += x;
    newTransform[5] += y;
    this.setState({ canvasTransform: newTransform })
  }

  handleMouseUp = (e) => {
    this.mouseDown = false;
  }

  handleMouseLeave = (e) => {
    this.mouseDown = false;
  }

  render() {
    return (
      <canvas 
        id="EditingCanvas"
        ref={this.state.canvasRef}
        onMouseDown={this.handleMouseDown}
        onMouseMove={this.handleMouseMove}
        onMouseUp={this.handleMouseUp}
        onMouseLeave={this.handleMouseLeave}
      />
    );
  }
  
}

export default EditingCanvas;