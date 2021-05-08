import React, { Component } from "react";
import Button from "@material-ui/core/Button";
import Slider from "@material-ui/core/Slider";

class TransformationEditingMenu extends Component {
  constructor(props) {
    super(props);
    this.emojiPreview = React.createRef();
    // This is a temporary solution while I find a way to read files from a directory from react or pass it here somehow
    this.emojiList = [
      "blush", "cry", "derp", "heart_punch", "heart", "hearts", "nom", "sweat",
      "okay", "owo", "punch", "shake", "shock", "smile", "sparkle", "stare"
    ];
    this.emojiIdx = 0;
  }

  previewEmoji = () => {
    this.img = new Image();
    this.img.onload = () => {
      const context = this.emojiPreview.current.getContext("2d");
      context.clearRect(0, 0, 150, 150);
      context.drawImage(this.img, 0, 0, this.img.width, this.img.height, 0, 0, 150, 150);
      
      const functions = this.props.getCanvas("functions");
      functions.emoji[0] = this.img;
      this.props.setCanvas("functions", functions);
    }
    this.img.src = "./emojis/bugcat_owo.png";
  }

  componentDidMount() {
    this.previewEmoji();

    const emoji = this.props.getCanvas("functions").emoji;
    this.savedEmoji = [null, emoji[1], emoji[2], emoji[3], emoji[4], true];
    
    const img = this.props.getCanvas("image");
    let minEdge = img[3] < img[4] ? img[3] : img[4];

    emoji[1] = 0;
    emoji[2] = 0;
    emoji[3] = 0.999;
    emoji[4] = 0.3;
    emoji[5] = false;
    this.props.setCanvas("activeFunction", "emoji");
  }

  componentWillUnmount() {
    this.props.setCanvas("activeFunction", null);
    this.props.getCanvas("functions").emoji = this.savedEmoji;
  }

  onScaleChange = (e, v) => {
    this.setState({ scale: v });
    const functions = this.props.getCanvas("functions");
    // Clamps scale to prevent errors
    if (v < 0.002) v = 0.002;
    if (v > 0.999) v = 0.999;
    functions.emoji[3] = v;
    this.props.setCanvas("functions", functions);
  }

  onOpacityChange = (e, v) => {
    this.setState({opacity: v});
    const functions = this.props.getCanvas("functions");
    functions.emoji[4] = v;
    this.props.setCanvas("functions", functions);
  }

  updateEmojiBackend = () => {
    const emoji = this.props.getCanvas("functions").emoji;
    const name = "bugcat_" + this.emojiList[this.emojiIdx] + ".png"
    this.props.applyFilter("emoji", [name, [parseInt(emoji[1]), parseInt(emoji[2])], parseFloat(emoji[3]), 0.5]);
  }

  onApply = () => {
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

export default TransformationEditingMenu;
