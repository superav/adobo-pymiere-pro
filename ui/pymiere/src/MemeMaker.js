import React, { Component } from 'react';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import Button    from '@material-ui/core/Button';

class MemeMaker extends Component {
    constructor(props) {
        super(props)
        this.state = {
            topText: "",
            bottomText: ""
        };

    }

    handleChange = name => event => {
        this.setState({ [name]: event.target.value });
    };

    submitText = () => {
        console.log("top text: " + this.state.topText);
        console.log("bottom text: " + this.state.bottomText);
    }

    render() {
        return (
            <div>

                <Typography id="text-fields" gutterBottom>
                    Meme Maker
                </Typography>

                <Grid container spacing={1}>
                    <TextField
                        id="outlined-basic"
                        label="Top Text"
                        variant="outlined"
                        value={this.state.topText}
                        onChange={this.handleChange('topText')} />
                    <br />
                    <br />
                    <br />
                    <br />
                    <TextField
                        id="outlined-basic"
                        label="Bottom Text"
                        variant="outlined"
                        value={this.state.bottomText}
                        onChange={this.handleChange('bottomText')} />
                </Grid>
                <br></br>
                <Button
                    variant="contained"
                    color="primary"
                    disabled="true"
                    onClick={this.submitText} >
                    Submit
                </Button>

            </div>
        );
    }
    
}

export default MemeMaker;