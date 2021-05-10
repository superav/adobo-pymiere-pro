import React from 'react'

export default function ImageResolution(props) {
    return (
      <div>
        <h3>Image height: {props.imageResolution()[0]}</h3>
        <h3>Image width: {props.imageResolution()[1]}</h3>
      </div>
    )
}