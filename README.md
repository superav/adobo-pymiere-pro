# Adobo Pymiere Pro

## Project URL

[ec2-3-235-179-211.compute-1.amazonaws.com](ec2-3-235-179-211.compute-1.amazonaws.com)

## Setting up Sphinx

Run `python -m pip install -r sphinx-requirements.txt` to install necessary Sphinx extensions.

In the top-level directory, set the PYTHONPATH by running:
 
```export PYTHONPATH=`pwd` ```

* ***NOTE:** If you're using Windows, you must run this in Git Bash.*

To build Sphinx docs, in `/docs` run:

```./make.bat html```

Developer and user documentation can be found by navigating to `docs/build/html/` and
opening `index.html` in a browser.

## Tasks

###Jessica 14.28%

- Refactored logic code from previous and current sprint
- User/Dev docs
- Helped with integrating backend and frontend
- Debugged NST code
- Managed S3 bucket

###Arush 14.28%

- organized UI menus
- integrated sprint 3 features
- MR reviews
- NST integration

###Avi 14.28%

- Worked on fixing bugs
- Deployed on AWS
- Wrote code to help handle NST integration
- Implemented Snack bar
- Reviewed Merge Requests

###Aidan 14.28%

- logic function and testing for contrast, autocontrast, brightness, and vignette(removed)
- added tests for nst via flask
- more tests to test sprint 3 additions
- debugging pipeline errors
- MR review
  
###Phong 14.28%

- Integrate emoji, cropping and pen tool UI with backend
- Created UI for viewing slowing NST output
- Fixing bugs for integrated features

###John 14.28%

- Record tutorials for user docs
- Implemented meme generator backend
- UI to convert file between filetypes
- UI for changing contrast
- UI for uploading NST filters

###Eric 14.28%

- Docker Refactoring
- Project Persistence
- Backend for getting temp files from slow NST
- Selecting slow NST output
- Backend and integration for applying NST filter
- Fixing Docker for Tensorflow
