import React, { useState} from 'react';
import Button from '@material-ui/core/Button';
import Slider from '@material-ui/core/Slider';
import Typography from '@material-ui/core/Typography';

export default function FrameMenu(props) {
  
  const [red, setRed] = useState(0);
  const [green, setGreen] = useState(0);
  const [blue, setBlue] = useState(0);

  function handleRChange(e, v) {
    setRed(v);
  }
  
  function handleGChange (e, v) {
    setGreen(v);
  }
  
  function handleBChange(e, v) {
    setBlue(v);
  }

  function confirmFrame() {
    props.applyFilter("frame", [parseInt(red), parseInt(green), parseInt(blue)])
  }

  return (
    <div>
      <Typography id="color" gutterBottom>
      <b>Frame Color</b>
      </Typography>

      <h4>Red</h4>
      <Slider
        value={red}
        onChange={handleRChange}
        aria-labelledby="input-slider"
        valueLabelDisplay="auto"
        min={0}
        max={255}
      />
      
      <h4>Green</h4>
      <Slider
        value={green}
        onChange={handleGChange}
        aria-labelledby="input-slider"
        valueLabelDisplay="auto"
        min={0}
        max={255}
      />

      <h4>Blue</h4>
      <Slider
        value={blue}
        onChange={handleBChange}
        aria-labelledby="input-slider"
        valueLabelDisplay="auto"
        min={0}
        max={255}
      />
      <br></br>
      <Button variant="contained" color="primary" onClick={confirmFrame}>Add Frame</Button>
    </div>
  )
}