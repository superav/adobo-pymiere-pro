import React, { Component } from 'react';
import TopLevelToolbar from './TopLevelToolbar'
import CenterImagePage from './CenterImagePage'
import './ImageUIPage.css'

class ImageUIPage extends Component {

  constructor(props) {
    super(props)
  }

  render() {
    return (
      <div id="imageUIPageMainArticle">
        <TopLevelToolbar />
        <CenterImagePage selectedImage={this.props.selectedImage}/>
      </div>
    )
  }
}

export default ImageUIPage;