import React, { useState } from 'react'
import TextField from '@material-ui/core/TextField';

export default function TextOverlayLocationSelector(props) {
    const [xCoord, setXCoord] = useState(0);
    const [yCoord, setYCoord] = useState(0);

    function handleChangeX(e) {
        setXCoord(e.target.value);
    }
    function handleChangeY(e) {
        setYCoord(e.target.value);
    }
    return (
        <div>
            <h3>Location Selection</h3>
            <TextField id="outlined-basic" label="X Coordinate" variant="outlined" value={xCoord} onChange={handleChangeX}/>
            <TextField id="outlined-basic" label="Y Coordinate" variant="outlined" value={yCoord} onChange={handleChangeY}/>
            <p>X, Y: ({xCoord}, {yCoord})</p>
        </div>
    )
}