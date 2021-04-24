# User Documentation

## Getting Started

Clone the git repository through:

`git clone http://cmsc435.garrettvanhoy.com/superav/adobo-pymiere-pro.git`

---

## Quickstart

Make sure Docker Desktop is installed.

Run `docker compose up` in the top-level directory. This will build and run docker images for both UI and backend.

UI will be on port 3000 and backend will be on port 5000.

---

## Building the Backend

To build the logic docker image:

```docker build -f ./docker/logic.Dockerfile -t pymiere-logic . ```

Running the logic image:

```docker run -d -p 5000:5000 pymiere-logic```

The container will accessible on port 3000

---

## Building the Frontend

Building the UI docker image:

```docker build -f ./docker/ui.Dockerfile -t pymiere-ui . ```

Running the UI docker image:

```docker run -d -p 3000:3000 pymiere-ui```

The container will be accessible on port 3000

---

## Running the Backend Test Suite

In the top-level directory, run: `python -m pip install -r requirements.txt`

To run test suites, in `tests/`, you can run:

```
python -m pytest as_image_proc_tests.py -v --cov

python -m pytest jz_image_proc_tests.py -v --cov

python -m pytest john_logic_test.py -v --cov
``` 
