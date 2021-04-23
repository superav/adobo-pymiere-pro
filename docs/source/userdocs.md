# User Documentation

## Setup and Installation

Clone the git repository through:

`git clone http://cmsc435.garrettvanhoy.com/superav/adobo-pymiere-pro.git`

In the top-level project directory, install all necessary python libraries using requirements.txt:

`python -m pip install -r requirements.txt`

## Running Backend

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

## Running the Backend Test Suite

To thoroughly test the functionality of our image/video processing methods, we wrote a series of test suites to ensure
the backend logic works correctly. To run these test suites, navigate into the tests folder by running `cd tests`
in your terminal, then paste the following commands in:

```
python -m pytest as_image_proc_tests.py -v --cov
python -m pytest jz_image_proc_tests.py -v --cov
python -m pytest john_logic_test.py -v --cov
``` 

## Running the Frontend

To start up the frontend, make sure you have Node.js installed first. Then, navigate to the ui/pymiere folder by running
`cd ui/pymiere` in your terminal. Then, run the following two commands:

```
npm install
npm start
```

This should launch the UI in your browser window. To learn more about the UI and what features are available to you,
make sure to keep reading the rest of the guide! Note that, at the moment, the UI is NOT responsive, and you won't be able
to apply any of the effects through the UI.
