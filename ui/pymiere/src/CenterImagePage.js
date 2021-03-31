import React, { Component } from 'react';
import "./CenterImagePage.css"

class CenterImagePage extends Component {
    constructor(props) {
      super(props);
  
  
    }

    render(){
        return (
            //three horizontal boxes taking up the entire vertical space 
            //List of different effects
            //UI for view of current effect options
            //View Image
            <div id="mainImageUIandEffectsBar">
                <div id="effectOptions">
                    effects Options
                </div>
                <div id="effectControls">
                    effects Controls
                </div>
                <div id="imageDisplay">
                    Image
                </div>
            </div>
        );
    }
}
export default CenterImagePage;