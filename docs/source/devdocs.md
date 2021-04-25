# Developer Documentation

## Getting Started

Clone the git repository through:

`git clone http://cmsc435.garrettvanhoy.com/superav/adobo-pymiere-pro.git`

In the top-level directory, run `python -m pip install -r requirements.txt` to install necessary python modules.

In `ui/pymiere`, run `npm install` to install necessary Node.js modules.

Check out [Architecture](./architecture.md) and the [style guide](#style-guide) for how to add features.

See [Useful Links](#useful-links) for quick links to more documents about sprint and product backlogs.

---

## How to Test Features

Refer to [User Documentation](./userdocs.md) for how to build Docker images for frontend and backend.

### Logic

Test scripts are stored in `tests/` and can be run using `pytest`. You can also import the image processing methods
in `logic` directly into your own test file.

To run test suites, in `tests/`, you can run:

```
python -m pytest as_image_proc_tests.py -v --cov

python -m pytest jz_image_proc_tests.py -v --cov

python -m pytest john_logic_test.py -v --cov
``` 

### UI

To run the UI, you can run `npm start` in `ui/pymiere`.

---

## Style Guide

### Python

- Indentation - **4 spaces**, no tabs
- Must follow [PEP8](https://pep8.org/)
- Type hints are required
- Use [docstrings](https://www.python.org/dev/peps/pep-0257) to label classes and methods (this just makes code easier to read)
  - Must format according to [Google-style docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
  - Simple example:

```python
def update_game(request: dict) -> dict:
    """ <Description of method>
    
        Args:
            request: dictionary describing the "move" to be made in the game

        Returns:
            <Return Type>: dictionary describing the game's new state.
    """
```

### React/JavaScript

- Use semicolons
- Indentation - **2 spaces**, no tabs

### CSS

- Indentation - **2 spaces**, no tabs

---

## Useful Links

- [Sprint 1 Planning](https://docs.google.com/document/d/1P07zavGMqTPCiqGF2OF3D2gBqslt_bnp2AIl3g_MXNg/edit?usp=sharing)
- [Sprint 1 Backlog](https://docs.google.com/spreadsheets/d/1AZSluWLcC_vbxHlxw8vF818qNlPNkdO_HmxYUeLmf6o/edit#gid=0)
- [Product Backlog](https://docs.google.com/spreadsheets/d/1unLgkR4rvNnqmJrZjnZdQsl4nE7awgJnOwqOPmWbu08/edit#gid=0)
- [Figma UI Mockup](https://www.figma.com/file/bmx8HOgE1KYulGbAN5Yn50/Adobe-Pymiere?node-id=0%3A1)

---

## Teams

### UI

- Avi
- Eric
- Arush
- Phong
- John
- Jessica

### Logic

- Avi
- Jessica
- John
- Aidan
