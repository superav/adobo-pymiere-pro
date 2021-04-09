import React from 'react'
import { Card, Icon } from 'semantic-ui-react'

const extra = (
  <a>
    <Icon name='user' />
    16 Friends
  </a>
)

const ProjectCard = (props) => (
  <Card
    id="card"
    link
    image={props.image}
    header={props.header}
    //meta='Friend'
    description={props.disc}
    //extra={extra}
  />
)

export default ProjectCard