import React, { useState } from 'react'
import TextField from '@material-ui/core/TextField';
import { makeStyles } from '@material-ui/core/styles';
import TextOverlayFontMenu from './TextOverlayFontMenu'
import Button from '@material-ui/core/Button'
import TextOverlayLocationSelector from './TextOverlayLocationSelector'
import TextOverlayColorPicker from './TextOverlayColorPicker'

export default function TextOverlayMenu(props) {

    const [curTextInput, setCurTextInput] = useState("");
    const [fontType, setFontType] = useState("Open Sans");
    const [fontSize, setFontSize] = useState(10);
    const [colorRed, setColorRed] = useState(0);
    const [colorGreen, setColorGreen] = useState(0);
    const [colorBlue, setColorBlue] = useState(0);
    const [locationX, setLocationX] = useState(0);
    const [locationY, setLocationY] = useState(0);
    var colorStr = "";


    const useStyles = makeStyles(theme => ({
        container: {
            display: 'flex',
            flexWrap: 'wrap',
        },
        formControl: {
            margin: theme.spacing(1),
        },
        }));
    const classes = useStyles();

    function handleChange(e) {
        setCurTextInput(e.target.value);
    }

    function confirmTextOverlay() {
        console.log(curTextInput);
        console.log(fontType);
        console.log(fontSize);
        console.log(colorRed);
        console.log(colorGreen);
        console.log(colorBlue);
        console.log(locationX);
        console.log(locationY);
        props.applyfilter("add-text", [curTextInput, fontType, parseInt(fontSize), [parseInt(locationX), parseInt(locationY)], [parseInt(colorRed), parseInt(colorGreen), parseInt(colorBlue)]])
    }

    return (
        <div>
            <h4>Enter Text Below</h4>
            <form className={classes.formControl} noValidate autoComplete="off">
                <TextField id="outlined-basic" label="Input" variant="outlined" value={curTextInput} onChange={handleChange}/>
            </form>
            <TextOverlayFontMenu inputText={curTextInput} fontType={fontType} setFontType={setFontType} fontSize={fontSize} 
                setFontSize={setFontSize}/>
            <br></br>
            <TextOverlayColorPicker setRColor={setColorRed} setGColor={setColorGreen} setBColor={setColorBlue}/>
            {colorStr = "rgb(" + colorRed + "," + colorGreen + "," + colorBlue + ")"}
            
            <p className="apply-font" style={{"color": colorStr, "font-size": fontSize*1.6}}>{curTextInput}</p>
            <TextOverlayLocationSelector xCoord={locationX} yCoord={locationY} setLocationX={setLocationX} setLocationY={setLocationY}/>
            <br></br>
            <Button variant="contained" color="primary" onClick={confirmTextOverlay}>Add Text Overlay</Button>
        </div>
    )
}