# Adobo Pymiere Pro

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

Jessica 17.55%

- user and dev docs
- migrated docs to Sphinx
- Sprint planning and user stories
- added draw on image support
- refactored asset manager to support temp projects
- refactored nst.py to save output images
- fixed nst.py
- git support

Arush 15.09%

- Text overlay integration
- Color menu UI & integration (Saturation, Hue, Gradient)
- Brightness UI
- Mosaic filter UI & integration
- Solarize filter and auto-contrast filter UI
- UI polishing

Avi 14.09%

- Sprint Planning
- Designed Integration Workflow
- Wrote boilerplate code for integration requests and responses to update image
- Helped solve bugs across all integration issues
- Wrote components to upload NST filters and Images to S3
- Wrote Faster NST algorithm that will allow for a quicker NST
- Reviewed Merge Requests for UI

Aidan 13.09%

- logic function and testing for code to remove red eye effects, apply solarize effect, apply mirror/flip effect,
  apply mosaic effect, and adding a frame
- Updating flask for new features being added
- Tested the flask endpoints with bash script feature tests, testing and sending get/post requests, and pulling/pushing
  to s3 buckets
- Improving variable names, making methods to prevent complicated if statements, and checking PEP8 through codebase
- Update CI to properly run new tests and fix its installations
  
Phong 15.29%

- Revamp canvas for rendering image by streamlining the event loop
- Implemented front end pen functionality
- Implemented front end cropping functionality
- Implemented UI for viewing NST algorithm outputs
- Cropping functionality integration with backend
- Help with fetching image to the s3 bucket
- Fix bugs for pen tool, cropping and support for all canvas related issues

John 13.60%

- Implemented ui for transformation menu, size editing menu, and storing into local filesystem 
- Used Avi's method to integrate menus with backend requests
- Fixed comments and PEP8 violations from Sprint 1
- Approved merge requests for other ui tasks
- Wrote and posted scrum logs for Sprint 2

Eric 11.29%

- ui for vignette and meme generator
- Dockerized Node server
- added support for docker compose
- assisted with feature testing
- general bugfixes
- assisting with CI
