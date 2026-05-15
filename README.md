# Software Documentation with Sphinx

A Python project demonstrating proficiency in internal code documentation and automated external HTML documentation generation using Sphinx.

## Project Overview
This repository was created to fulfill the requirements of the Software Documentation module. It showcases best practices in writing PEP-8 compliant Python docstrings and utilizing the Sphinx library to parse those docstrings into a readable, professional web format.

## Features
* **Modular Math Functions:** Includes basic arithmetic operations (`add`, `subtract`, `multiply`, `divide`) written in Python.
* **Robust Error Handling:** The `divide.py` module includes explicit `try/except` logic to gracefully handle `ZeroDivisionError` edge cases.
* **Standardized Docstrings:** All functions are thoroughly documented using the Sphinx `:param:`, `:returns:`, and `:rtype:` directive formats.
* **Sphinx HTML Build:** Fully configured `conf.py` utilizing the `sphinx_rtd_theme` (Read the Docs) for a clean UI.

## How to Generate the Documentation
To rebuild the HTML documentation locally, ensure you have Sphinx installed, then navigate to the `docs` folder and run the build command:

1. `cd sphinx_maths/docs/`
2. `make clean`
3. `make html`

The generated HTML files will be available inside the `sphinx_maths/docs/_build/html/` directory. Open `index.html` in any web browser to view the documentation.
