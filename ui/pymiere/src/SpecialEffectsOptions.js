import React, { Component } from 'react'
import FormControl from '@material-ui/core/FormControl'
import FormControlLabel from '@material-ui/core/FormControlLabel'
import FormLabel from '@material-ui/core/FormLabel'
import RadioGroup from '@material-ui/core/RadioGroup'
import Radio from '@material-ui/core/Radio'
import Button from '@material-ui/core/Button'

export function SpecialEffectsOptions () {

  const [effectChoice, setEffectChoice] = React.useState("None");

  const handleChangeEffectChoice = (event, newValue) => {
    setEffectChoice(newValue);
  };

  return (
      <div>
        <FormControl component="fieldset">
        <h3>Special Effects</h3>
        <RadioGroup aria-label="Special Effects" name="Special Effects" value={effectChoice} onChange={handleChangeEffectChoice}>
          <FormControlLabel value="mosaic" control={<Radio />} label="Mosaic Filter" />
          <FormControlLabel value="solarize" control={<Radio />} label="Solarize" />
          <FormControlLabel value="autocontrast" control={<Radio />} label="Autocontrast" />
        </RadioGroup>
      </FormControl>
      <br></br>
      <Button variant="contained" color="primary">Add Special Effect</Button>

      </div>
  )
}

export default SpecialEffectsOptions
