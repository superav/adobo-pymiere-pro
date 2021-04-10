import React, { useState } from 'react'
import TextField from '@material-ui/core/TextField';
import { makeStyles } from '@material-ui/core/styles';
import TextOverlayFontMenu from './TextOverlayFontMenu'

export default function TextOverlayTextInput(props) {

    const [curTextInput, setCurTextInput] = useState("");

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

    return (
        <div>
            <h4>{props.textLabel}</h4>
            <form className={classes.formControl} noValidate autoComplete="off">
                <TextField id="outlined-basic" label="Input" variant="outlined" value={curTextInput} onChange={handleChange}/>
            </form>
            <TextOverlayFontMenu inputText={curTextInput}/>
        </div>
    )
}