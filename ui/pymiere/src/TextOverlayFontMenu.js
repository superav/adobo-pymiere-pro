import React, { Component, useState } from 'react'
import FontPicker from "font-picker-react"
import './FontMenu.css'
import TextOverlayFontSizeMenu from './TextOverlayFontSizeMenu'
import TextOverlayColorPicker from './TextOverlayColorPicker'

export default function TextOverlayFontMenu (props) {

    const [activeFontFamily, setActiveFontFamily] = useState("Open Sans");


    function onFontSelect(nextFont) {
        setActiveFontFamily(nextFont.family)
        props.setFontType(nextFont.family)
    }
    return (
        <div>
            <p>Fonts: </p>
            <FontPicker 
                apiKey="AIzaSyD85O_DqqgZb3xNBSCn2pkq7HMtDqQ1ISY"
                activeFontFamily={activeFontFamily}
                onChange={onFontSelect}
            />
            <TextOverlayFontSizeMenu setFontSize={props.setFontSize}/>
        </div>
    )
    // add "className="apply-font"" to all JSX elements that the selected font should be applied to
}

