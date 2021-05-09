import React, { Component } from "react";
import Button from "@material-ui/core/Button";
import { withSnackbar } from 'notistack';

class TransformationEditingMenu extends Component {
  constructor(props) {
    super(props);
    this.emojiPreview = React.createRef();
  }

  componentDidMount () {
    this.img = new Image();
    this.img.onload = () => {
      const context = this.emojiPreview.current.getContext("2d");
      context.clearRect(0, 0, 150, 150);
      context.drawImage(this.img, 0, 0, this.img.width, this.img.height, 0, 0, 150, 150);
      
      const emoji = this.props.getCanvas("functions").emoji;
      this.savedEmoji = [...emoji];
      
      emoji[0] = this.img;
      const img = this.props.getCanvas("image");
      if (this.img.width <= img[3] && this.img.height <= img[4]) {
        console.log(img);
        // Center the watermark and set scale to 1
        emoji[1] = (img[3] - this.img.width) / 2;
        emoji[2] = (img[4] - this.img.height) / 2;
        emoji[3] = 0.999;
      } else {
        let scaleX = this.img.width  / img[3];
        let scaleY = this.img.height / img[4];
        emoji[3] = 1 / (scaleX > scaleY ? scaleX : scaleY);
        emoji[1] = (img[3] - this.img.width * emoji[3]) / 2;
        emoji[2] = (img[4] - this.img.height * emoji[3]) / 2;
      }
      // Scale
      emoji[4] = 0.3;
      emoji[5] = false;
      this.props.setCanvas("activeFunction", "emoji");
    }
    this.img.src = "./emojis/bugcat_owo.png";
  }

  componentWillUnmount() {
    this.props.setCanvas("activeFunction", null);
    this.props.getCanvas("functions").emoji = this.savedEmoji;
  }

  updateEmojiBackend = () => {
    const emoji = this.props.getCanvas("functions").emoji;
    const name = "bugcat_owo.png";
    this.props.applyFilter("emoji", [name, [parseInt(emoji[1]), parseInt(emoji[2])], parseFloat(emoji[3]), 0.5]);
  }

  onApply = () => {
    this.props.enqueueSnackbar("Applying watermark...", {
      variant: 'info',
      autoHideDuration: 2000,
    });
    this.updateEmojiBackend();
  }

  render() {
    return <div>
      <h3>Watermark</h3>
      <canvas ref={this.emojiPreview} width={150} height={150}/><br/>
      <br/><br/>
      <Button variant="contained" color="primary" onClick={this.onApply}>Apply Watermark</Button>
    </div>
  }
}

export default withSnackbar(TransformationEditingMenu);
