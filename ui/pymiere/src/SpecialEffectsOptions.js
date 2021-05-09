import React, { Component, useState } from 'react'
import FormControl from '@material-ui/core/FormControl'
import FormControlLabel from '@material-ui/core/FormControlLabel'
import FormLabel from '@material-ui/core/FormLabel'
import RadioGroup from '@material-ui/core/RadioGroup'
import Radio from '@material-ui/core/Radio'
import Button from '@material-ui/core/Button'
import TextField from '@material-ui/core/TextField'

export function SpecialEffectsOptions (props) {

  const [effectChoice, setEffectChoice] = useState("None");
  const [solarizeValue, setSolarizeValue] = useState(0);
  const [topLeftX, setTopLeftX] = useState(0);
  const [topLeftY, setTopLeftY] = useState(0);
  const [bottomRightX, setBottomRightX] = useState(0);
  const [bottomRightY, setBottomRightY] = useState(0);

  const handleTopLeftX = (e) => {
    setTopLeftX(e.target.value);
  }

  const handleTopLeftY = (e) => {
    setTopLeftY(e.target.value);
  }

  const handleBottomRightX = (e) => {
    setBottomRightX(e.target.value);
  }

  const handleBottomRightY = (e) => {
    setBottomRightY(e.target.value);
  }

  const handleChangeEffectChoice = (event, newValue) => {
    setEffectChoice(newValue);
    console.log(newValue);
  };

  const handleSolarizeChange = (e) => {
    setSolarizeValue(e.target.value);
    console.log(e.target.value);
  };

  function confirmSpecialEffects() {
    console.log(effectChoice);
    console.log(solarizeValue);
    if (effectChoice === "mosaic") {
      props.applyFilter("mosaic");
    }
    else if (effectChoice === "solarize") {
      props.applyFilter("solarize", parseInt(solarizeValue));
    }
    else if (effectChoice == "red-eye-remover") {
      props.applyFilter("red-eye-remover", [parseInt(topLeftX), parseInt(topLeftY), parseInt(bottomRightX), parseInt(bottomRightY)]);
    }
    else if (effectChoice == "autocontrast") {
      props.applyFilter("autocontrast");
    }
    else if (effectChoice == "vignette") {
      props.applyFilter("vignette");
    }
  }

  return (
      <div>
        <FormControl component="fieldset">
        <h3>Special Effects</h3>
        <RadioGroup aria-label="Special Effects" name="Special Effects" value={effectChoice} onChange={handleChangeEffectChoice}>
          <FormControlLabel value="mosaic" control={<Radio />} label="Mosaic Filter" />
          <FormControlLabel value="solarize" control={<Radio />} label="Solarize" />
          <TextField id="outlined-basic" label="Solarize Threshold (0-255)" variant="outlined" value={solarizeValue} onChange={handleSolarizeChange}/>
          <FormControlLabel value="red-eye-remover" control={<Radio />} label="Redeye Removal" />
          <TextField id="outlined-basic" label="Top Left X Coordinate" variant="outlined" size="small" value={topLeftX} onChange={handleTopLeftX}/>
          <br></br>
          <TextField id="outlined-basic" label="Top Left Y Coordinate" variant="outlined" size="small" value={topLeftY} onChange={handleTopLeftY}/>
          <br></br>
          <TextField id="outlined-basic" label="Bottom Right X Coordinate" variant="outlined" size="small" value={bottomRightX} onChange={handleBottomRightX}/>
          <br></br>
          <TextField id="outlined-basic" label="Bottom Right Y Coordinate" variant="outlined" size="small" value={bottomRightY} onChange={handleBottomRightY}/>
          <br></br>
          <FormControlLabel value="autocontrast" control={<Radio /> } label="Autocontrast" />
          <FormControlLabel value="vignette" control={<Radio /> } label="Vignette" />
        </RadioGroup>
      </FormControl>
      <br></br>
      <Button variant="contained" color="primary" onClick={confirmSpecialEffects}>Add Special Effect</Button>

      </div>
  )
}

export default SpecialEffectsOptions
