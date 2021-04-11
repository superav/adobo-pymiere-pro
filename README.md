# Adobo Pymiere Pro
## Team Contributions
Avi -> 17.25%:
 - Sprint Planning
 - ML Research
 - Wrote NST Algorithm in a python notebook
 - Base responsive UI
 - Facilitating Group Meetings
 - Conducted Code Reviews
 - Helped Other group members whenever they got stuck
 - Research around EC2, S3, and Docker
 - Overall Project Design and research on how the moving parts would be integrated
 - Created Project Workflows and communicated to the rest of the team those workflows

Jessica -> 17.35%:
 - Sprint Planning
 - UI Mockup
 - Refactored NST Algorithm to work as an isolated function
 - Asset Manager Class
 - Multiple Image Filter Functions with tests
 - Researched how to write tests with images for the image filters
 - Helped other group members with Git
 - Research around EC2, S3, and Docker
 - Developer Documentation

Aidan -> 17.25%:
 - Entirely handled CI/CD and some Docker work
 - Multiple Image Filter Functions
 - Wrote tests for his implemented image filters
 - Wrote Flask app

Eric (Zhoucheng) -> 17.25%:
 - Research around EC2, and Docker
 - Supported Flask app creation
 - Developed Responsive Project Creation UI Page (both design and implementation)
 - Supported CI/CD development with Aidan
 - Created Example Curl Requests for the User Docs
 - Project Integration with Docker

Arush -> 12.0%:
 - Learned React and material UI from scratch
 - Created UI for Font Effects Menu
 - Created UI for Fonts Menu
 - Created UI for Text Overlay
 - Created UI for Audio Effects

John (Yinjun) -> 11.3%:
 - Created Image Processing Filter Functions and wrote tests for those
 - Created Audio Effect Functions and wrote tests for those
 - Scrum Master (Handled Transcription and Facilitation of Scrum Meetings)
 - Wrote User Documentation

Phong -> 7.6%:
 - Created UI for Zooming in and out of an image
 - Created UI to pan around an image
 - Research Canvas use to display image and interact with image
 - Wrote React Router implementation to add urls to our various UI pages
## Sprint One Reflection
Being the very first sprint, our team didn't really know what to expect in terms of the amount of time different tasks 
would take. We were overly-ambitious in trying to work on multiple tasks and develop complex features. 
We underestimated the amount of technical debt we'd incur refactoring and attempting to merge 
people's code together. We were able to get members of the UI team to integrate their code in the frontend; similarly,
members of the logic team successfully merged their code in the backend. However, at the moment, the frontend and
backend aren't able to communicate with each other. As such, the User Documentation will explain how to test and use 
both individually. We apologize for failing to meet the criteria laid out at the beginning of the sprint, and we'll be 
sure to set more realistic standards next sprint and deliver a working, responsive product.
## User Documentation
NOTE: please read Sprint One Reflection above before proceeding.

In order to ensure a satisfactory user experience, we've included a comprehensive user guide that covers how to install,
navigate, and leverage all the tools built into Adobo Pymiere Pro.
#### Setup and Installation
In this section, we walk through the steps necessary to get the backend and frontend components of our application up
and running. In addition, we'll cover how to run our automated test suite for the backend logic.
###### Project Download
First, navigate to the project Gitlab and clone the repository. After you have the repository on your local machine, 
make sure to cd into the project, then you can run the frontend, backend, or test suite.
###### Running the Backend
If you don't have Docker already, make sure to download Docker Desktop. Run Docker. Then, open up your terminal and run:

`docker build -t pymiere .`

Once the build finishes, run:

`docker run -d -p 5000:5000 pymiere`

After Docker's up and running, you can make HTTP GET requests to directly call the image and video processing functions
in the backend. You can either run GET requests through interfaces such as Postman or Advanced REST client, or you can
copy cURL commands into a Linux terminal. Use the sample cURL request below as a template to build your own requests:
```
curl --location --request GET 'localhost:5000/logic/image_editor' \
--header 'Content-Type: application/json' \
--data-raw '{
    "effect": "hue",
    "image_name": "turtle",
    "file_extension": "png",
    "is_working_copy": false,
    "specifications": 222
}'
``` 
Note that all image and video processing functions take in the same five-parameter dictionary: effect, image_name,
file_extension, is_working_copy, and specifications. "effect" delineates the type of special effect you want to apply to
the image/video. To see all the viable effects, reference lines 23-55 in app.py. "image_name" refers to the name of the 
image/video you want to process. At the moment, only images can be pulled from the cloud, so videos will have to be 
local to your machine. To see a list of available images, run the GET request shown below. For now, please only use the
turtle image for testing the backend. Other images are being modified by the tests, and the tests might fail if the 
images are modified by the user at the moment. We are working to fix this in the future!
```
curl --location --request GET 'localhost:5000/logic/image_list' \
--header 'Content-Type: application/json' \
--data-raw '{
    "list_everything": true
}'
```
This request returns a list of the images you can put into "image_name." At the moment, all files on the cloud are PNGs,
so "file_extension" should always be ".png" for every request. In addition, the features associated with "is_working_copy"
haven't been implemented yet, so that can just be set to false for now. Finally, the "specifications" variable refers to
any additional parameters this specific effect function needs besides the image/video object itself. All additional
parameters should be put in a list and set to "specifications." In order to see the parameters associated with the
effect, reference the corresponding function in lines 23-55 of app.py, go to that function, and look at the necessary 
parameters and their types.
###### Running the Backend Test Suite:
To thoroughly test the functionality of our image/video processing methods, we wrote a series of test suites to ensure
the backend logic works correctly. To run these test suites, navigate into the tests folder by running `cd tests`
in your terminal, then paste the following commands in:
```
python -m pytest as_image_proc_tests.py -v --cov
python -m pytest jz_image_proc_tests.py -v --cov
python -m pytest john_logic_test.py -v --cov
``` 
###### Running the Frontend:
To start up the frontend, make sure you have Node.js installed first. Then, navigate to the ui/pymiere folder by running
`cd ui/pymiere` in your terminal. Then, run the following two commands:
```
npm install
npm start
```
This should launch the UI in your browser window. To learn more about the UI and what features are available to you,
make sure to keep reading the rest of the guide! Note that, at the moment, the UI is NOT responsive, and you won't be able
to apply any of the effects through the UI.
#### Getting Started
#### Image Effects
#### Video Effects


