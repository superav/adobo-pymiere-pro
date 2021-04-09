import React, { Component } from 'react';
import "./ProjectSelectPage.css";
import ProjectCard from "./ProjectCard.js";
import ImageUIPage from "./ImageUIPage.js";
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
  } from "react-router-dom";

class ProjectSelectPage extends Component {
    constructor(props) {
        super(props)
    }

    

    render() {
        return (
            <div id="outerContainer">
                <div id="imageProjectsContainer">
                    <div id="imageProjects">
                        <Link to="/image"><ProjectCard id="card" image="/images/new.svg" header="New Image Project" disc="Create a new image project with Adobo Pymiere Pro" /></Link>
                    </div>
                </div>

                <div id="videoProjectsContainer">
                    <div id="videoProjects">
                            <ProjectCard className="card" image="/images/new.svg" header="New Video Project" disc="Create a new video project with Adobo Pymiere Pro"/>
                    </div>
                </div>
            </div>
        );
    }
}

export default ProjectSelectPage