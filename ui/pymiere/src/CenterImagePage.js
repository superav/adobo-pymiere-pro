import React, { Component } from 'react';
import "./CenterImagePage.css"
import VerticalTabs from './EffectsOptionsMenu'

class CenterImagePage extends Component {

    render(){
        return (
            //three horizontal boxes taking up the entire vertical space 
            //List of different effects
            //UI for view of current effect options
            //View Image
            <div id="mainImageUIandEffectsBar">
                <VerticalTabs />
                <div id="imageDisplay">
                    Image
                </div>
            </div>
        );
    }
}
export default CenterImagePage;