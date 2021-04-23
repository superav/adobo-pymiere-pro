import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Slider from '@material-ui/core/Slider';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button'

const useStyles = makeStyles({
  root: {
    width: 200,
  },
});

export default function ColorMenu() {
  const classes = useStyles();
  const [saturation, setSaturation] = React.useState(50);
  const [hue, setHue] = React.useState(50);
  const [alpha, setAlpha] = React.useState(50);
  const [colorInit1, setColorInit1] = React.useState(50);
  const [colorInit2, setColorInit2] = React.useState(50);
  const [colorInit3, setColorInit3] = React.useState(50);
  const [colorSecondary1, setColorSecondary1] = React.useState(50);
  const [colorSecondary2, setColorSecondary2] = React.useState(50);
  const [colorSecondary3, setColorSecondary3] = React.useState(50);

  const handleChangeSaturation = (event, newValue) => {
    setSaturation(newValue);
  };

  const handleChangeHue = (event, newValue) => {
    setHue(newValue);
  };

  const handleChangeAlpha = (e) => {
    setAlpha(e.target.value);
  };

  const handleChangeColorInit1 = (e) => {
    setColorInit1(e.target.value);
  };

  const handleChangeColorInit2 = (e) => {
    setColorInit2(e.target.value);
  };

  const handleChangeColorInit3 = (e) => {
    setColorInit3(e.target.value);
  };

  const handleChangeColorSecondary1 = (e) => {
    setColorSecondary1(e.target.value);
  };

  const handleChangeColorSecondary2 = (e) => {
    setColorSecondary2(e.target.value);
  };

  const handleChangeColorSecondary3 = (e) => {
    setColorSecondary3(e.target.value);
  };

  function confirmColorEffects() {
    console.log(saturation);
    console.log(hue);
    console.log(alpha);
    console.log(colorInit1);
    console.log(colorInit2);
    console.log(colorInit3);
    console.log(colorSecondary1);
    console.log(colorSecondary2);
    console.log(colorSecondary3);
  }


  return (
    <div className={classes.root}>
      <Typography id="continuous-slider" gutterBottom>
        Saturation
      </Typography>
      <Grid container spacing={2}>
        <Grid item xs>
          <Slider
            value={saturation}
            onChangeCommitted={handleChangeSaturation}
            aria-labelledby="discrete-slider-small-steps"
            min={0}
            max={255}
            step={1}
            valueLabelDisplay="auto"
          ></Slider>
          <br></br>
        </Grid>
      </Grid>

      <Typography id="continuous-slider" gutterBottom>
        Hue
      </Typography>
      <Grid container spacing={2}>
        <Grid item xs>
        <Slider
            value={hue}
            onChangeCommitted={handleChangeHue}
            aria-labelledby="discrete-slider-small-steps"
            min={0}
            max={255}
            step={1}
            valueLabelDisplay="auto"
          ></Slider>
        </Grid>
      </Grid>

      <h4>Gradient Selection</h4>
      <br></br>
      <Grid container spacing={1}>
            <TextField id="outlined-basic" label="Alpha Value" variant="outlined" onChange={handleChangeAlpha}/>
            <br />
            <br />
            <br />
            <br />
            <TextField id="outlined-basic" label="Color initial 1" variant="outlined" onChange={handleChangeColorInit1}/>
            <br />
            <br />
            <TextField id="outlined-basic" label="Color initial 2" variant="outlined" onChange={handleChangeColorInit2}/>
            <br />
            <br />
            <TextField id="outlined-basic" label="Color initial 3" variant="outlined" onChange={handleChangeColorInit3}/>
            <br />
            <br />
            <br />
            <br />
            <TextField id="outlined-basic" label="Color secondary 1" variant="outlined" onChange={handleChangeColorSecondary1}/>
            <br />
            <br />
            <TextField id="outlined-basic" label="Color secondary 2" variant="outlined" onChange={handleChangeColorSecondary2}/>
            <br />
            <br />
            <TextField id="outlined-basic" label="Color secondary 3" variant="outlined" onChange={handleChangeColorSecondary3}/>
      </Grid>
      <br></br>
      <br></br>
      <Button variant="contained" color="primary" onClick={confirmColorEffects}>Apply Color Effects</Button>
      
    </div>
  );
}


