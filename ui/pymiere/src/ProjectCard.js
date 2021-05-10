import React from 'react'
import { Card, Image } from 'semantic-ui-react'


const ProjectCard = (props) => (

  <Card>
    <Card.Content header={props.header} />
    <Image key={Date.now() + props.image} src={props.image}/>
    <Card.Content>
      <Card.Description>
        {props.disc}
      </Card.Description>
    </Card.Content>
  </Card>
)

export default ProjectCard