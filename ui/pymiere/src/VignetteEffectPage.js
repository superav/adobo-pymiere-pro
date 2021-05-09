import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Slider from '@material-ui/core/Slider';
import Input from '@material-ui/core/Input';
import PhotoSizeSelectSmallRoundedIcon from '@material-ui/icons/PhotoSizeSelectSmallRounded';
import BlurOnIcon from '@material-ui/icons/BlurOn';
import GradientIcon from '@material-ui/icons/Gradient';
import Brightness3Icon from '@material-ui/icons/Brightness3';
import Button from '@material-ui/core/Button'

const useStyles = makeStyles({
    root: {
        width: 250,
    },
    input: {
        width: 42,
    },
});

export default function VignetteEffectPage(props) {
    const classes = useStyles();
    const [size, setSize] = React.useState(30);
    const [falloff, setFalloff] = React.useState(30);
    const [blur, setBlur] = React.useState(30);
    const [darken, setDarken] = React.useState(30);

    const handleSliderChange = (event, newValue, setValue) => {
        setValue(newValue);
    };

    const handleInputChange = (event, setValue) => {
        setValue(event.target.value === '' ? '' : Number(event.target.value));
    };

    const handleBlur = (value, setValue) => {
        if (value < 0) {
            setValue(0);
        } else if (value > 100) {
            setValue(100);
        }
    };

    function confirmVignetteEffects() {
        props.applyFilter("vignette")
    }

    return (
        <div className={classes.root}>
            <Typography id="input-slider" gutterBottom>
                Size
            </Typography>
            <Grid container spacing={2} alignItems="center">
                <Grid item>
                    <PhotoSizeSelectSmallRoundedIcon />
                </Grid>
                <Grid item xs>
                    <Slider
                        value={typeof size === 'number' ? size : 0}
                        onChange={(event, newValue) => handleSliderChange(event, newValue, setSize)}
                        aria-labelledby="input-slider"
                    />
                </Grid>
                <Grid item>
                    <Input
                        className={classes.input}
                        value={size}
                        margin="dense"
                        onChange={(event) => handleInputChange(event, setSize)}
                        onBlur={() => handleBlur(size, setSize)}
                        inputProps={{
                            step: 10,
                            min: 0,
                            max: 100,
                            type: 'number',
                            'aria-labelledby': 'input-slider',
                        }}
                    />
                </Grid>
            </Grid>

            <Typography id="input-slider" gutterBottom>
                Falloff
            </Typography>
            <Grid container spacing={2} alignItems="center">
                <Grid item>
                    <GradientIcon />
                </Grid>
                <Grid item xs>
                    <Slider
                        value={typeof falloff === 'number' ? falloff : 0}
                        onChange={(event, newValue) => handleSliderChange(event, newValue, setFalloff)}
                        aria-labelledby="input-slider"
                    />
                </Grid>
                <Grid item>
                    <Input
                        className={classes.input}
                        value={falloff}
                        margin="dense"
                        onChange={(event) => handleInputChange(event, setFalloff)}
                        onBlur={() => handleBlur(falloff, setFalloff)}
                        inputProps={{
                            step: 10,
                            min: 0,
                            max: 100,
                            type: 'number',
                            'aria-labelledby': 'input-slider',
                        }}
                    />
                </Grid>
            </Grid>

            <Typography id="input-slider" gutterBottom>
                Blur Amount
            </Typography>
            <Grid container spacing={2} alignItems="center">
                <Grid item>
                    <BlurOnIcon />
                </Grid>
                <Grid item xs>
                    <Slider
                        value={typeof blur === 'number' ? blur : 0}
                        onChange={(event, newValue) => handleSliderChange(event, newValue, setBlur)}
                        aria-labelledby="input-slider"
                    />
                </Grid>
                <Grid item>
                    <Input
                        className={classes.input}
                        value={blur}
                        margin="dense"
                        onChange={(event) => handleInputChange(event, setBlur)}
                        onBlur={() => handleBlur(blur, setBlur)}
                        inputProps={{
                            step: 10,
                            min: 0,
                            max: 100,
                            type: 'number',
                            'aria-labelledby': 'input-slider',
                        }}
                    />
                </Grid>
            </Grid>

            <Typography id="input-slider" gutterBottom>
                Darken Amount
            </Typography>
            <Grid container spacing={2} alignItems="center">
                <Grid item>
                    <Brightness3Icon />
                </Grid>
                <Grid item xs>
                    <Slider
                        value={typeof darken === 'number' ? darken : 0}
                        onChange={(event, newValue) => handleSliderChange(event, newValue, setDarken)}
                        aria-labelledby="input-slider"
                    />
                </Grid>
                <Grid item>
                    <Input
                        className={classes.input}
                        value={darken}
                        margin="dense"
                        onChange={(event) => handleInputChange(event, setDarken)}
                        onBlur={() => handleBlur(darken, setDarken)}
                        inputProps={{
                            step: 10,
                            min: 0,
                            max: 100,
                            type: 'number',
                            'aria-labelledby': 'input-slider',
                        }}
                    />
                </Grid>
            </Grid>
            <Button variant="contained" color="primary" onClick={confirmVignetteEffects}>Add Vignette Effects</Button>

        </div>
    );
}