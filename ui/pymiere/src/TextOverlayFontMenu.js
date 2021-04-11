import React, { Component, useState } from 'react'
import FontPicker from "font-picker-react"
import './FontMenu.css'
import TextOverlayFontSizeMenu from './TextOverlayFontSizeMenu'
import TextOverlayColorPicker from './TextOverlayColorPicker'

export default function TextOverlayFontMenu (props) {

    const [activeFontFamily, setActiveFontFamily] = useState("Open Sans");
    const [fontSize, setFontSize] = useState(12);
    const [rColor, setRColor] = useState(0);
    const [gColor, setGColor] = useState(0);
    const [bColor, setBColor] = useState(0);
    var colorStr = "";

    return (
        <div>
            <p>Fonts: </p>
            <FontPicker 
                apiKey="AIzaSyD85O_DqqgZb3xNBSCn2pkq7HMtDqQ1ISY"
                activeFontFamily={activeFontFamily}
                onChange={(nextFont) => 
                    setActiveFontFamily(nextFont.family)
                }
            />
            <TextOverlayFontSizeMenu setFontSize={setFontSize}/>
            <TextOverlayColorPicker setRColor={setRColor} setGColor={setGColor} setBColor={setBColor}/>
            {colorStr = "rgb(" + rColor + "," + gColor + "," + bColor + ")"}
            {console.log(fontSize)}
            
            <p className="apply-font" style={{"color": colorStr, "font-size": fontSize*1.6}}>{props.inputText}</p>
        </div>
    )
    // add "className="apply-font"" to all JSX elements that the selected font should be applied to
}

