# User Documentation

Adobo Pymiere Pro is a web-based image editing platform with the latest
image processing features to support your image editing needs. We support both
casual and advanced users with amazing, high tech features from automated meme
generation to neural style transfer!

## Getting Started

Clone the git repository through:

`git clone http://cmsc435.garrettvanhoy.com/superav/adobo-pymiere-pro.git`

---

### Quickstart

Make sure Docker Desktop is installed.

Build both docker images with:

```docker compose build```

Run both docker images with:

```docker compose up```

UI will be on port 3000 and backend will be on port 5000.

---

### Building the Backend

To build the logic docker image:

```docker build -f ./docker/logic.Dockerfile -t adobo-pymiere-pro_logic . ```

Running the logic image:

```docker run -d -p 5000:5000 -v "$(pwd)"/logic:/docker_root/logic adobo-pymiere-pro_logic```

The container will accessible on port 3000

---

### Building the Frontend

Building the UI docker image:

```docker build -f ./docker/ui.Dockerfile -t adobo-pymiere-pro_web . ```

Running the UI docker image:

```docker run -d -p 3000:3000 -v "$(pwd)"/ui/pymiere:/docker_root/ui adobo-pymiere-pro_web```

The container will be accessible on port 3000

---

### Running the Backend Test Suite

In the top-level directory, run: `python -m pip install -r requirements.txt`

To run test suites, navigate to `tests/`. Unit tests are labelled with the
`test_` prefix. You can run any unit test file individually as such:

```
python -m pytest test_asset_manager.py -v --cov
``` 

Feature tests can be run in the top-level directory through:

```
./feature_tests.sh
```

## How to Use

[Tutorials Videos](https://youtube.com/playlist?list=PLQjWzm6-0M1GTdSGCUaUetnYN8Pmpy4lj)

## Notes

- The vignette feature works when running the server outside of Docker. However,
there are issues with certain graphics libraries missing when installing OpenCV
on Docker. We've left the UI for the feature in, but have left it disabled for now.
