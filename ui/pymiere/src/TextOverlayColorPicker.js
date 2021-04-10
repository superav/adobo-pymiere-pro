import React, { useState } from 'react'
import TextField from '@material-ui/core/TextField';

export default function TextOverlayColorPicker(props) {

    function handleChangeR(e) {
        props.setRColor(e.target.value);
    }
    function handleChangeG(e) {
        props.setGColor(e.target.value);
    }
    function handleChangeB(e) {
        props.setBColor(e.target.value);
    }
    return (
        <div>
            <h3>Color Selection</h3>
            <TextField id="outlined-basic" label="R Value" variant="outlined" onChange={handleChangeR}/>
            <br />
            <br />
            <TextField id="outlined-basic" label="G Value" variant="outlined" onChange={handleChangeG}/>
            <br />
            <br />
            <TextField id="outlined-basic" label="B Value" variant="outlined" onChange={handleChangeB}/>
        </div>
    )
}
