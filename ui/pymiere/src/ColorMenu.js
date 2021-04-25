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

export default function ColorMenu(props) {
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

  function confirmGradient() {
    console.log(alpha);
    console.log(colorInit1);
    console.log(colorInit2);
    console.log(colorInit3);
    console.log(colorSecondary1);
    console.log(colorSecondary2);
    console.log(colorSecondary3);
    props.applyfilter("color-gradient", [parseInt(alpha), [parseInt(colorInit1), parseInt(colorInit2), parseInt(colorInit3)], [parseInt(colorSecondary1), parseInt(colorSecondary2), parseInt(colorSecondary3)]])
  }

  function confirmSaturation() {
    console.log(saturation);
    props.applyfilter("saturation", [parseFloat(saturation/255)]);
  }

  function confirmHue() {
    console.log(hue);
    props.applyfilter("hue", [parseInt(hue)]);
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
            onChange={handleChangeSaturation}
            aria-labelledby="discrete-slider-small-steps"
            min={0}
            max={255}
            step={1}
            valueLabelDisplay="auto"
          ></Slider>
          <Button variant="contained" color="primary" onClick={confirmSaturation}>Apply Saturation</Button>
          <br></br>
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
            onChange={handleChangeHue}
            aria-labelledby="discrete-slider-small-steps"
            min={0}
            max={360}
            step={1}
            valueLabelDisplay="auto"
          ></Slider>
          <Button variant="contained" color="primary" onClick={confirmHue}>Apply Hue</Button>

        </Grid>
      </Grid>

      <h4>Gradient Selection</h4>
      <br></br>
      <Grid container spacing={1}>
            <TextField id="outlined-basic" label="Alpha Value (0 - 255)" variant="outlined" onChange={handleChangeAlpha}/>
            <br />
            <br />
            <br />
            <br />
            <TextField id="outlined-basic" label="Color initial 1 (0 - 255)" variant="outlined" onChange={handleChangeColorInit1}/>
            <br />
            <br />
            <TextField id="outlined-basic" label="Color initial 2 (0 - 255)" variant="outlined" onChange={handleChangeColorInit2}/>
            <br />
            <br />
            <TextField id="outlined-basic" label="Color initial 3 (0 - 255)" variant="outlined" onChange={handleChangeColorInit3}/>
            <br />
            <br />
            <br />
            <br />
            <TextField id="outlined-basic" label="Color secondary 1 (0 - 255)" variant="outlined" onChange={handleChangeColorSecondary1}/>
            <br />
            <br />
            <TextField id="outlined-basic" label="Color secondary 2 (0 - 255)" variant="outlined" onChange={handleChangeColorSecondary2}/>
            <br />
            <br />
            <TextField id="outlined-basic" label="Color secondary 3 (0 - 255)" variant="outlined" onChange={handleChangeColorSecondary3}/>
      </Grid>
      <br></br>
      <br></br>
      <Button variant="contained" color="primary" onClick={confirmGradient}>Apply Gradient</Button>
      
    </div>
  );
}


