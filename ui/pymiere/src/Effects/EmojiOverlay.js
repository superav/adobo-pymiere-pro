import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import Slider from '@material-ui/core/Slider';

export default class EmojiOverlay extends Component {
  constructor(props) {
    super(props);
    this.emojiPreview = React.createRef();
    // This is a temporary solution while I find a way to read files from a directory from react or pass it here somehow
    this.emojiList = [
      "blush", "cry", "derp", "heart_punch", "heart", "hearts", "nom", "sweat",
      "okay", "owo", "punch", "shake", "shock", "smile", "sparkle", "stare"
    ];
    this.state = {
      scale: 1,
      opacity: 255
    }
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
      functions.emoji[1] = 0;
      functions.emoji[2] = 0;
      this.props.setCanvas("functions", functions);
    }
    this.img.src = "./emojis/bugcat_" + this.emojiList[this.emojiIdx] + ".png";
  }

  componentDidMount() {
    this.previewEmoji();

    const emoji = this.props.getCanvas("functions").emoji;
    this.setState({
      scale: emoji[3],
      opacity: emoji[4]
    })
    this.props.setCanvas("activeFunction", "emoji");
  }

  componentWillUnmount() {
    this.props.setCanvas("activeFunction", null);
  }

  onPrevEmoji = () => {
    this.emojiIdx--;
    if (this.emojiIdx < 0)
      this.emojiIdx = this.emojiList.length-1;
    this.previewEmoji();
  }

  onNextEmoji = () => {
    this.emojiIdx = (this.emojiIdx + 1) % this.emojiList.length;
    this.previewEmoji();
  }

  onScaleChange = (e, v) => {
    this.setState({ scale: v });
    const functions = this.props.getCanvas("functions");
    functions.emoji[3] = v;
    this.props.setCanvas("functions", functions);
  }

  onOpacityChange = (e, v) => {
    this.setState({opacity: v});
    const functions = this.props.getCanvas("functions");
    functions.emoji[4] = v;
    this.props.setCanvas("functions", functions);
  }

  onApply = () => {

  }

  render() {
    return <div>
      <h3>Emoji</h3>
      <canvas ref={this.emojiPreview} width={150} height={150}/><br/>
      <Button variant="contained" color="primary" onClick={this.onPrevEmoji}>Prev</Button>
      <Button variant="contained" color="primary" onClick={this.onNextEmoji}>Next</Button>
      <br/><br/>
      <h3>Scale</h3>
      <Slider
        value = {this.state.scale}
        onChange={this.onScaleChange}
        aria-labelledby="continuous-slider"
        valueLabelDisplay="auto"
        step={0.001}
        min={0}
        max={1}
      />
      <br/><br/>
      <h3>Opacity</h3>
      <Slider
        value = {this.state.opacity}
        onChange={this.onOpacityChange}
        aria-labelledby="discrete-slider"
        valueLabelDisplay="auto"
        min={0}
        max={255}
      />
      <br/><br/>
      <Button variant="contained" color="primary" onClick={this.onApply}>Apply</Button>
    </div>
  }
}