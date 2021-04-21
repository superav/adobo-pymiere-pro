import React, { Component } from 'react';
import "./EditingCanvas.css";

class EditingCanvas extends Component {

  constructor(props) {
    super(props);
    this.img = null;
    this.mouseDown = false;
    this.canvasRef = React.createRef();
    this.canvasState = {
      transform: [1, 0, 0, 1, 0, 0],
      image: null,
      activeFunction: null,
      functions: {
        crop: {
          resize: -1,
          boundingBox: [100, 100, 100, 150] // Default location and size of cropping box
        }
      }
    }
    this.mousePos = [0, 0];
  }

  getCanvasState = (property) => {
    return this.canvasState[property];
  }

  setCanvasState = (property, value) => {
    this.canvasState[property] = value;
    this.draw();
  }

  insertImage = (src) => {
    const img = new Image();
    img.onload = () => {this.draw()};
    img.src = src;
    // Center the image in the canvas
    this.canvasState.transform[4] += (this.canvas.width - img.width) / 2;
    this.canvasState.transform[5] += (this.canvas.height - img.height) / 2;
    this.canvasState.image = [img, 0, 0, img.width, img.height, 0, 0, img.width, img.height];
  }

  componentDidMount() {
    // Set up references for canvas and context
    this.canvas = this.canvasRef.current;
    this.rect = this.canvas.getBoundingClientRect(); // bounding box of canvas
    this.context = this.canvas.getContext('2d');

    let width = this.canvas.parentElement.offsetWidth;
    let height = this.canvas.parentElement.offsetHeight;
    
    this.canvas.width = width;
    this.canvas.height = height;
    this.insertImage("logo512.png"); // TODO remove this when there's ability to import image
  }

  draw = () => {
    let width = this.canvas.width;
    let height = this.canvas.height;

    // Update context
    this.context.setTransform(1, 0, 0, 1, 0, 0); // Reset transform
    this.context.clearRect(0, 0, width, height); // Clear the canvas
    this.context.setTransform(...this.canvasState.transform);
    this.context.imageSmoothingEnabled = false;
    // Repopulate the canvas
    this.context.drawImage(...this.canvasState.image);
    // Update functions
    switch (this.canvasState.activeFunction) {
      case "crop":
        this.drawCropTool();
        break;
      default:
        break;
    }
  }

  cropHandlePositions = (box) => {
    return [
      [box[0] + box[2] / 2, box[1]],
      [box[0]             , box[1] + box[3] / 2],
      [box[0] + box[2] / 2, box[1] + box[3]],
      [box[0] + box[2]    , box[1] + box[3] / 2]
    ];
  }

  drawCropTool = () => {
    const box = this.canvasState.functions.crop.boundingBox;
    // Draw crop box and bounding gizmos
    this.context.strokeStyle = 'black';
    this.context.strokeRect(...box);
    this.cropHandlePositions(box).forEach((p, i) => {
      if (i === this.canvasState.functions.crop.resize)
        this.context.fillStyle = 'white';
      else
        this.context.fillStyle = 'black';
      this.context.fillRect(p[0]-2, p[1]-2, 4, 4);
    })
  }

  handleMouseMove = (e) => {
    // Update actual mouse position in canvas
    const canvasTransform = this.canvasState.transform
    this.mousePos = [
      (e.clientX - this.rect.left - canvasTransform[4]) / canvasTransform[0],
      (e.clientY - this.rect.top  - canvasTransform[5]) / canvasTransform[3]
    ];
    
    if (this.mouseDown) {
      if (this.canvasState.activeFunction) {
        switch (this.canvasState.activeFunction) {
          case "crop":
            const crop = this.canvasState.functions.crop;
            const dX = e.movementX / canvasTransform[0];
            const dY = e.movementY / canvasTransform[3];
            switch (crop.resize) {
              case 0:
                crop.boundingBox[1] += dY;
                crop.boundingBox[3] -= dY;
                break;
              case 1:
                crop.boundingBox[0] += dX;
                crop.boundingBox[2] -= dX;
                break;
              case 2:
                crop.boundingBox[3] += dY;
                break;
              case 3:
                crop.boundingBox[2] += dX;
                break;
              default:
                crop.boundingBox[0] += dX;
                crop.boundingBox[1] += dY;
                break;
            }
            break;
          default:
            break;
        }
      } else {
        this.canvasState.transform[4] += e.movementX;
        this.canvasState.transform[5] += e.movementY;
      }
    } else {
      switch (this.canvasState.activeFunction) {
        case "crop":
          const crop = this.canvasState.functions.crop;
          let highlightIdx = -1;
          this.cropHandlePositions(crop.boundingBox).forEach((p, i) => {
            const dist2 = Math.pow(p[0] - this.mousePos[0], 2) + Math.pow(p[1] - this.mousePos[1], 2);
            if (dist2 <= 16) {
              highlightIdx = i;
            }
          });
          this.canvasState.functions.crop.resize = highlightIdx;
          this.draw();
          break;
        default:
          break;
      }
    }
    this.draw();
  }

  handleMouseDown = (e) => {
    this.mouseDown = true;
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
        ref={this.canvasRef}
        onMouseDown={this.handleMouseDown}
        onMouseMove={this.handleMouseMove}
        onMouseUp={this.handleMouseUp}
        onMouseLeave={this.handleMouseLeave}
      />
    );
  }
  
}

export default EditingCanvas;