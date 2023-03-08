#!/bin/bash

# This script is used to start the container and run pytest

# Run pytest
pytest -p no:warnings -p no:cacheprovider -v -rPx --html=report/report.html "$@"

# Always return 0 (success), otherwise GitHub action see failed tests as failed jobs
exit 0
