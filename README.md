# `pytest_mip`: Pytest and Selenium -based integration tests of the up-and-running MIP federations

This open-source tool provides integration tests, written in Python, based on `selenium` and `pytest` for testing the up-and-running federations of the MIP. For portability and easy deployment, the tests are encapsulated in a Docker software container image.

## Prerequisites

This tool is intended to be run using its Docker image and so Docker is required to be installed.

## How to build the Docker image

1. Clone the repository

2. Go to the clone directory

3. Edit the `project_parameters.py.template` and set the variables `UserID` and `UserPWD` with your own EBRAIN credentials for login to the different MIP federations.

4. Rename `project_parameters.py.template` to `project_parameters.py`

5. Build the Docker image with the following command:

    ```bash
    $ docker build -t pytest_mip .
    ```

## How to run the tests using the Docker image

### Test all MIP federations

Once `pytest_mip` is built, you can execute the tests for all federations as follows:

   ```bash
   $ docker run -t pytest_mip
   ```

### Test a specific MIP federation

You can run the following command to test a specific federation:

   ```bash
   $ docker run -t pytest_mip test_<fed_name>.py
   ```

where `<fed_name>` designs a specific federation.

Here is a list of `<fed_name>` / filename pairs for the different federations that are now available:
* `qa_federation` : `test_qa_federation.py`
* `public_mip` : `test_public_mip.py`
* ...
