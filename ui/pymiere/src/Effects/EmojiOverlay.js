import React, { Component } from 'react';
import Button from '@material-ui/core/Button';

export default class EmojiOverlay extends Component {
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
    console.log(this.emojiIdx);
    const img = new Image();
    img.onload = () => {
      this.context.clearRect(0, 0, 150, 150);
      this.context.drawImage(img, 0, 0, img.width, img.height, 0, 0, 150, 150);
    }
    img.src = "./emojis/bugcat_" + this.emojiList[this.emojiIdx] + ".png";
  }

  componentDidMount() {
    this.context = this.emojiPreview.current.getContext("2d");
    this.previewEmoji();
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

  render() {
    return <div>
      <canvas ref={this.emojiPreview} width={150} height={150}/><br/>
      <Button variant="contained" color="primary" onClick={this.onPrevEmoji}>Prev</Button>
      <Button variant="contained" color="primary" onClick={this.onNextEmoji}>Next</Button>
    </div>
  }
}