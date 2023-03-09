#!/bin/bash

# This script is used to start the container and run pytest

# Run pytest
pytest -p no:warnings -p no:cacheprovider -v -rPx --html=report/report.html --self-contained-html --css=pytest_report.css "$@"
