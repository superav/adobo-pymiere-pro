import React, { Component } from "react";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";

class StoreLocalFilesystem extends Component {
  constructor(props) {
    super(props);
    this.state = {
      fileName: "",
    };
  }

  handleFileNameChange = (e) => {
    this.setState({
      fileName: e.target.value,
    });
  };

  saveImage = () => {
    console.log("image name: " + this.state.fileName);
    this.props.downloadImage(this.state.fileName);
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
          onChange={this.handleFileNameChange}
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
