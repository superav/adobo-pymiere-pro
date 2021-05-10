import React, { Component } from 'react';
import "./ProjectSelectPage.css";
import ProjectCard from "./ProjectCard.js";
import {
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

        const url = "http://ec2-3-235-179-211.compute-1.amazonaws.com:5000/logic/image_list_usr";

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

    emptyCache() {
    if ('caches' in window) {
        caches.keys().then((names) => {
            // Delete all the cache files
            names.forEach(name => {
                caches.delete(name);
            })
        });
    }
}

    componentDidMount() {
        this.emptyCache()
        this.loadImages()
    }

    loadImages() {
        this.getProjects().then(res => {
            let filteredList = this.filterProjects(res.list)
            filteredList.splice(0, 0, "/images/new.svg")
            this.setState({ projects: filteredList })
            console.log(this.state.projects)
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
            <Link to="/image" key={Date.now() + project} onClick={(e) => { imageSelectHandler("https://adobo-pymiere.s3.amazonaws.com/" + project + "?dummy=" + Math.random(), e) }}><ProjectCard image={project === "/images/new.svg" ? project : "https://adobo-pymiere.s3.amazonaws.com/" + project + "?dummy=" + Math.random()} header={project === "/images/new.svg" ? "New Project" : project.substring(project.lastIndexOf('/') + 1)} disc={project === "/images/new.svg" ? "Create a new project with Adobo Pymiere Pro" : "Continue working on " + project.substring(project.lastIndexOf('/') + 1)} /></Link>
        )
    });

    return <div>{projectCards}</div>
}

export default ProjectSelectPage