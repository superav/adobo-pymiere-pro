import React from 'react'
import { Card, Icon, Image } from 'semantic-ui-react'

const extra = (
  <a>
    <Icon name='user' />
    16 Friends
  </a>
)

const ProjectCard = (props) => (
  // <Card
  //   link
  //   image={props.image}
  //   header={props.header}
  //   //meta='Friend'
  //   description={props.disc}
  //   //extra={extra}
  // />

  <Card>
    <Card.Content header={props.header} />
    <Image src={props.image}/>
    <Card.Content>
      <Card.Description>
        {props.disc}
      </Card.Description>
    </Card.Content>
  </Card>
)

export default ProjectCard