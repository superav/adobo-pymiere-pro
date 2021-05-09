import React, { Component } from "react";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import { makeStyles } from '@material-ui/core/styles';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';

class StoreLocalFilesystem extends Component {
  constructor(props) {
    super(props);
    this.state = {
      fileName: "",
      extension: ""
    };
  }

  handleChange = (name) => (event) => {
    this.setState({[name]: event.target.value});
  }

  saveImage = () => {
    console.log("image name: " + this.state.fileName);
    console.log("image extension: " + this.state.extension);
    this.props.downloadImage(this.state.fileName, this.state.extension);
  };

  render() {
    return (
      <div>
        <h4>Save File As:</h4>
        <TextField
          value={this.state.fileName}
          id="outlined-basic"
          label="File Name"
          variant="outlined"
          onChange={this.handleChange("fileName")}
        />
        <br></br>
        <br></br>
        <TextField
          value={this.state.extension}
          id="outlined-basic"
          label="Extension"
          variant="outlined"
          onChange={this.handleChange("extension")}
        />
        <br></br>
        <br></br>
        <Button
          variant="contained"
          color="primary"
          onClick={this.saveImage}
        >
          Save
        </Button>
      </div>
    );
  }
}

export default StoreLocalFilesystem;
