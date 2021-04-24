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
