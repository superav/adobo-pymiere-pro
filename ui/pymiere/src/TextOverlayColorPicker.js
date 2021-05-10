import React from 'react'
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
            <TextField id="outlined-basic" value={props.colorRed} label="R Value (0 - 255)" variant="outlined" onChange={handleChangeR}/>
            <br />
            <br />
            <TextField id="outlined-basic" value={props.colorGreen} label="G Value (0 - 255)" variant="outlined" onChange={handleChangeG}/>
            <br />
            <br />
            <TextField id="outlined-basic" value={props.colorBlue} label="B Value (0 - 255)" variant="outlined" onChange={handleChangeB}/>
        </div>
    )
}
