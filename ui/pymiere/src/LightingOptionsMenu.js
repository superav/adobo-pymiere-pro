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

export default function LightingOptionsMenu() {
  const classes = useStyles();
  const [value, setValue] = React.useState(50);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <div className={classes.root}>
      <Typography id="continuous-slider" gutterBottom>
        Brightness
      </Typography>
      <Grid container spacing={2}>
        <Grid item xs>
        <Slider
          value={value}
          onChangeCommitted={handleChange}
          aria-labelledby="discrete-slider-small-steps"
          min={0}
          max={1}
          step={0.1}
          valueLabelDisplay="auto"
        ></Slider>

        </Grid>
      </Grid>
      <br></br>
      <Button variant="contained" color="primary">Add Lighting Effects</Button>
    </div>
  );
}