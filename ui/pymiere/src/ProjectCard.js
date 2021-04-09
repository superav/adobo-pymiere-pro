import React from 'react'
import { Card, Icon } from 'semantic-ui-react'

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
        <Card.Content
          style={{
            height: "50%",
            backgroundImage: "/images/new.svg",
            backgroundSize: "cover",
          }}
        >
          <Card.Description style={{ color: "white" }}>
            {props.disc}
          </Card.Description>
        </Card.Content>
      </Card>
)

export default ProjectCard