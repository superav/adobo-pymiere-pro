import React, { Component } from 'react';
import "./EditingCanvas.css";

class EditingCanvas extends Component {

  image_name = "";
  version = 0;
  usingWorkingCopy = false;
  imageResolution = [0,0];
  
  constructor(props) {
    super(props);
    this.img = null;
    this.canvasRef = React.createRef();
    this.canvasState = {
      transform: [1, 0, 0, 1, 0, 0],
      image: null,
      activeFunction: null,
      functions: {
        crop: {
          resize: -1,
          boundingBox: [100, 100, 100, 150] // Default location and size of cropping box
        },
        pencil: {
          strokes: [],
          currentStroke: {
            points: [],
            fill: [0, 0, 0],
            width: 4
          },
          fill: [0, 0, 0],
          width: 4
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

  getImageResolution = () => {
    return this.imageResolution;
  }

  updateImage = (effect, parameters) => {
    this.usingWorkingCopy = true;

    const body = {
      "effect" : effect,
      "specifications" : parameters,
      "is_working_copy" : this.usingWorkingCopy,
      "file_extension": "png",
      "image_name" : this.image_name,
     };

    const init = {
      method: 'POST',
      headers : {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
      },
      body : JSON.stringify(body)
    };

    const url = 'http://localhost:5000/logic/image_editor'
    fetch(url, init)
    .then((response) => {
      return response.json(); // or .text() or .blob() ...
    })
    .then((text) => {
      this.insertImage(text.url);
    })
    .catch((e) => {
      console.log(e);
    });
  }
  
  insertImage = (src) => {
    console.log(src);
    let splitUrl = src.split('/');
    let imgName = splitUrl[splitUrl.length - 1];
    let imgNameSplit =  imgName.split('.');
    let imgNamewithoutURL = imgNameSplit[0];
    this.image_name = imgNamewithoutURL;
   
    const img = new Image();
    img.onload = () => {
      this.canvasState.image = [img, 0, 0, img.width, img.height, 0, 0, img.width, img.height];
      this.draw();
      this.imageResolution = [img.naturalHeight, img.naturalWidth];
    };
    img.id = "mainImage";
    img.src = src + "?version=" + this.version;
    this.version++;
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
    
    this.insertImage("https://upload.wikimedia.org/wikipedia/commons/c/c9/-Insert_image_here-.svg");
  }

  // This is the core of this class. all updates to the canvas has to be followed up by a draw call
  // The order is:
  //        1 - Clear the canvas
  //        2 - Redraw the image and the border around it
  //        3 - Redraw all edits the user made
  //        4 - Update the UI for any tool currently in use
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
    this.drawOutline();

    // Redraw all edits the user made
    this.drawPencil();
    
    // Update functions tool draw
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
    this.context.strokeStyle = '#FF0000';
    this.context.lineWidth = 2;
    this.context.strokeRect(...box);
    this.cropHandlePositions(box).forEach((p, i) => {
      if (i === this.canvasState.functions.crop.resize)
        this.context.fillStyle = 'white';
      else
        this.context.fillStyle = 'black';
      this.context.fillRect(p[0]-2, p[1]-2, 4, 4);
    })
  }

  drawPencil = () => {
    const pencil = this.canvasState.functions.pencil;
    // Draw all previous strokes
    pencil.strokes.forEach(s => {
      this.context.strokeStyle = `rgb(
        ${s.fill[0]},
        ${s.fill[1]},
        ${s.fill[2]})`;
      this.context.lineWidth = s.width;
      this.context.beginPath();
      this.context.moveTo(s.points[0][0], s.points[0][1]);
      s.points.forEach(p => {
        this.context.lineTo(p[0], p[1]);
      });
      this.context.stroke();
    });

    // Draw current stroke
    const stroke = pencil.currentStroke;
    if (stroke.points.length !== 0) {
      this.context.strokeStyle = `rgb(
        ${stroke.fill[0]},
        ${stroke.fill[1]},
        ${stroke.fill[2]})`;
      this.context.lineWidth = stroke.width;
      this.context.beginPath();
      this.context.moveTo(stroke.points[0][0], stroke.points[0][1]);
      stroke.points.forEach(p => {
        this.context.lineTo(p[0], p[1]);
      });
      this.context.stroke();
    }
  }
  
  drawOutline = () => {
    const img = this.canvasState.image;
    // Draw crop box and bounding gizmos
    this.context.strokeStyle = 'black';
    this.context.lineWidth = 4;
    this.context.strokeRect(img[5], img[6], img[7], img[8]);
  }
  
  clamp = (n, min, max) => { // Inclusive
    if (n >= min) {
      if (n <= max)
        return n;
      return max;
    }
    return min;
  }

  handleMouseMove = (e) => {
    // Update actual mouse position in canvas
    const canvasTransform = this.canvasState.transform
    this.mousePos = [
      (e.clientX - this.rect.left - canvasTransform[4]) / canvasTransform[0],
      (e.clientY - this.rect.top  - canvasTransform[5]) / canvasTransform[3]
    ];

    if (e.buttons === 1) {
      switch (this.canvasState.activeFunction) {
        case "crop":
          const crop = this.canvasState.functions.crop;
          const dX = e.movementX / canvasTransform[0];
          const dY = e.movementY / canvasTransform[3];
          switch (crop.resize) {
            case 0:
              crop.boundingBox[3] = this.clamp(crop.boundingBox[3] - dY, 0, this.canvasState.image[0].height);
              crop.boundingBox[1] = this.clamp(crop.boundingBox[1] + dY, 0, this.canvasState.image[0].height - crop.boundingBox[3]);
              break;
            case 1:
              crop.boundingBox[2] = this.clamp(crop.boundingBox[2] - dX, 0, this.canvasState.image[0].width);
              crop.boundingBox[0] = this.clamp(crop.boundingBox[0] + dX, 0, this.canvasState.image[0].width - crop.boundingBox[2]);
              break;
            case 2:
              crop.boundingBox[3] = this.clamp(crop.boundingBox[3] + dY, 0, this.canvasState.image[0].height - crop.boundingBox[1]);
              break;
            case 3:
              crop.boundingBox[2] = this.clamp(crop.boundingBox[2] + dX, 0, this.canvasState.image[0].width - crop.boundingBox[0]);
              break;
            default:
              // Case for moving cropping box
              crop.boundingBox[0] = this.clamp(crop.boundingBox[0] + dX, 0, this.canvasState.image[0].width - crop.boundingBox[2]);
              crop.boundingBox[1] = this.clamp(crop.boundingBox[1] + dY, 0, this.canvasState.image[0].height - crop.boundingBox[3]);
              break;
          }
          break;
        case "pencil":
          this.canvasState.functions.pencil.currentStroke.points.push(this.mousePos);
          break;
        default:
          this.canvasState.transform[4] += e.movementX;
          this.canvasState.transform[5] += e.movementY;
          break;
      }
    } else {
      switch (this.canvasState.activeFunction) {
        case "crop":
          const crop = this.canvasState.functions.crop;
          let highlightIdx = -1;
          this.cropHandlePositions(crop.boundingBox).forEach((p, i) => {
            const dist2 = Math.pow(p[0] - this.mousePos[0], 2) + Math.pow(p[1] - this.mousePos[1], 2);
            if (dist2 <= 100) {
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

  handleMouseUp = () => {
    switch (this.canvasState.activeFunction) {
      case "pencil":
        const pencil = this.canvasState.functions.pencil;
        pencil.strokes.push(pencil.currentStroke);
        pencil.currentStroke = {
          points: [],
          fill: pencil.fill,
          width: pencil.width
        };
        break;
      default:
        break;
    }
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