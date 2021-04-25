import React, { useState } from 'react'
import TextField from '@material-ui/core/TextField';

export default function TextOverlayColorPicker(props) {

    const rColor = 0;
    const gColor = 0;
    const bColor = 0;

    function handleChangeR(e) {
        props.setRColor(e.target.value);
        rColor = e.target.value;
    }
    function handleChangeG(e) {
        props.setGColor(e.target.value);
        gColor = e.target.value;
    }
    function handleChangeB(e) {
        props.setBColor(e.target.value);
        bColor = e.target.value;
    }
    return (
        <div>
            <h3>Color Selection</h3>
            <TextField id="outlined-basic" value={rColor} label="R Value (0 - 255)" variant="outlined" onChange={handleChangeR}/>
            <br />
            <br />
            <TextField id="outlined-basic" value={gColor} label="G Value (0 - 255)" variant="outlined" onChange={handleChangeG}/>
            <br />
            <br />
            <TextField id="outlined-basic" value={bColor} label="B Value (0 - 255)" variant="outlined" onChange={handleChangeB}/>
        </div>
    )
}
