import React from 'react'
import TextField from '@material-ui/core/TextField';

export default function TextOverlayLocationSelector(props) {

    function handleChangeX(e) {
        props.setLocationX(e.target.value);
    }
    function handleChangeY(e) {
        props.setLocationY(e.target.value);
    }
    return (
        <div>
            <h3>Location Selection</h3>
            <TextField id="outlined-basic" label="X Coordinate" variant="outlined" value={props.xCoord} onChange={handleChangeX}/>
            <TextField id="outlined-basic" label="Y Coordinate" variant="outlined" value={props.yCoord} onChange={handleChangeY}/>
            <p>X, Y: ({props.xCoord}, {props.yCoord})</p>
        </div>
    )
}