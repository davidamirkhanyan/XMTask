# XM Task

## Requirements
 * Python 3.8 or higher (3.8 recommended)

## Installation
1) Clone the repository
2) It's recommended to create a virtual environment. 
3) Install the required dependencies by running "pip install -r requirements.txt"

## Usage
* For running tests all you need is to copy the path of desired test or test suite
and paste it in pytest.ini file's first row and then run "pytest"

## Pytest.ini
Beside the first row where we store desired path to run tests, there are some additional configurations
* env - Values in [Dev, Prod], to define the environment to run tests on. (Configurable from conftest.py)
* browser - Values in [Chrome, Firefox], to define the browser.
* headless - Values in [yes, no], if yes test run in headless mode.
* html - To define the path where to generate the html report.
* dist - Recommended to be loadfile
* n - Here you can define CPU count to run tests

## Structure
1) PageModels Folder - Used to Store all POM Structure of Project
2) Resources Folder  - Used to Store all needed resources for tests
3) Report Folder     - After each run a simple report was generated here
4) Tests Folder      - All Test Suites containing the tests stored here
5) Utilities Folder  - Used to store all utilities for testing


