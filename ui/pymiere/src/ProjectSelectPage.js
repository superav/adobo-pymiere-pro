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
        this.state = {projects: []}
        this.cardList = []
    }

    getProjects() {
        const init = {
            method: "GET",
            headers: {
                "Access-Control-Allow-Origin": "*",
            }
        };

        const url = "http://localhost:5000/logic/image_list_usr";

        return fetch(url, init)
            .then((response) => {
                return response.json().then((data) => {
                    return data;
                }).catch((err) => {
                    console.log(err);
                });
            })
            .catch((e) => {
                console.log(e);
            });
    }

    filterProjects(list) {
        return list.filter(item => {
            return !item.includes("/assets/") && item.includes("/image_projects/") && item.includes(".png")
        })
    }

    componentDidMount() {
        this.getProjects().then(res => {
            var filteredList = this.filterProjects(res.list)
            filteredList.splice(0, 0, "/images/new.svg")
            this.setState({ projects: filteredList })
            console.log(this.state.projects)

            var testList = [1, 2, 3, 4]

            this.cardList = testList.map(project => {
                <li>{project}</li>
            })
        })

    }

    render() {
        return (
            <div id="outerContainer">
                <div id="imageProjectsContainer">
                    <h1>Select a Project</h1>
                    <div id="imageProjects">
                        <ProjectList projects={this.state.projects} imageSelectHandler={this.props.imageSelectHandler}/>
                    </div>
                </div>

                {/* <div id="videoProjectsContainer">
                    <div id="videoProjects">
                            <ProjectCard className="card" image="/images/new.svg" header="New Video Project" disc="Create a new video project with Adobo Pymiere Pro"/>
                    </div>
                </div> */}
            </div>
        );
    }
}

function ProjectList(props) {
    const projects = props.projects;
    const imageSelectHandler = props.imageSelectHandler;

    console.log(projects)
    const projectCards = projects.map(project => {
        return (
            <Link to="/image" onClick={(e) => { imageSelectHandler("https://adobo-pymiere.s3.amazonaws.com/" + project, e) }}><ProjectCard image={project === "/images/new.svg" ? project : "https://adobo-pymiere.s3.amazonaws.com/" + project} header={project === "/images/new.svg" ? "New Project" : project.substring(project.lastIndexOf('/') + 1)} disc={project === "/images/new.svg" ? "Create a new project with Adobo Pymiere Pro" : "Continue working on " + project.substring(project.lastIndexOf('/') + 1)} /></Link>
        )
    });

    return <div>{projectCards}</div>
}

export default ProjectSelectPage