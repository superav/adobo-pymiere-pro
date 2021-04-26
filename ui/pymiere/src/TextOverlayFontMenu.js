import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormHelperText from '@material-ui/core/FormHelperText';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import TextOverlayFontSizeMenu from './TextOverlayFontSizeMenu'

const useStyles = makeStyles((theme) => ({
  formControl: {
    margin: theme.spacing(1),
    minWidth: 120,
  },
  selectEmpty: {
    marginTop: theme.spacing(2),
  },
}));

export default function TextOverlayFontMenu(props) {
  const classes = useStyles();

  const handleChange = (event) => {
    console.log(event.target.value);
    props.setFontType(event.target.value);
  };

  return (
    <div>
      <FormControl className={classes.formControl}>
        <InputLabel id="demo-simple-select-label">Font</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={props.fontType}
          onChange={handleChange}
        >
          <MenuItem value={"open_sans"}>Open Sans</MenuItem>
          <MenuItem value={"calibri"}>Calibri</MenuItem>
          <MenuItem value={"comic_sans"}>Comic Sans</MenuItem>
          <MenuItem value={"futura"}>Futura </MenuItem>
          <MenuItem value={"papyrus"}>Papyrus</MenuItem>
          <MenuItem value={"windings"}>Windings</MenuItem>
          <MenuItem value={"helvetica"}>Helvetica</MenuItem>
          <MenuItem value={"roboto"}>Roboto</MenuItem>
          <MenuItem value={"times_newer_roman"}>Times Newer Roman</MenuItem>
          <MenuItem value={"inconsolata"}>Inconsolata</MenuItem>
        </Select>
      </FormControl>
      <TextOverlayFontSizeMenu setFontSize={props.setFontSize}/>
    </div>
  );
}