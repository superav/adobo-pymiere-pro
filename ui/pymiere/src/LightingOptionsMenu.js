import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Slider from '@material-ui/core/Slider';
import Button from '@material-ui/core/Button'


const useStyles = makeStyles({
  root: {
    width: 200,
  },
});

export default function LightingOptionsMenu(props) {
  const classes = useStyles();
  const [brightness, setBrightness] = React.useState(1);

  const handleChange = (event, newValue) => {
    setBrightness(newValue);
  };

  function confirmLightingEffects() {
    console.log(brightness);
    props.applyfilter("brightness", [parseFloat(brightness)])
  }

  return (
    <div className={classes.root}>
      <Typography id="continuous-slider" gutterBottom>
        Brightness
      </Typography>
      <Grid container spacing={2}>
        <Grid item xs>
        <Slider
          value={brightness}
          onChange={handleChange}
          aria-labelledby="discrete-slider-small-steps"
          min={0}
          max={1}
          step={0.1}
          valueLabelDisplay="auto"
          disabled="true"
        ></Slider>

        </Grid>
      </Grid>
      <br></br>
      <Button variant="contained" color="primary" disabled="true" onClick={confirmLightingEffects}>Add Lighting Effects</Button>
    </div>
  );
}