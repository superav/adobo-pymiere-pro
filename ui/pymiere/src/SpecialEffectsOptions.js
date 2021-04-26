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
      props.applyfilter("mosaic");
    }
    else if (effectChoice === "solarize") {
      props.applyfilter("solarize", parseInt(solarizeValue));
    }
    else if (effectChoice == "autocontrast") {
      props.applyfilter("autocontrast", [0.5]);
    }
  }

  return (
      <div>
        <FormControl component="fieldset">
        <h3>Special Effects</h3>
        <RadioGroup aria-label="Special Effects" name="Special Effects" value={effectChoice} onChange={handleChangeEffectChoice}>
          <FormControlLabel value="mosaic" control={<Radio />} label="Mosaic Filter" />
          <FormControlLabel value="solarize" control={<Radio />} label="Solarize" />
          <TextField id="outlined-basic" label="Input" variant="outlined" value={solarizeValue} onChange={handleSolarizeChange}/>
          <FormControlLabel value="autocontrast" disabled="true" control={<Radio /> } label="Autocontrast" />
        </RadioGroup>
      </FormControl>
      <br></br>
      <Button variant="contained" color="primary" onClick={confirmSpecialEffects}>Add Special Effect</Button>

      </div>
  )
}

export default SpecialEffectsOptions
