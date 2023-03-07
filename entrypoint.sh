#!/bin/bash

# This script is used to start the container and run pytest

# Run pytest
pytest -p no:warnings -p no:cacheprovider -v -rPx "$@"
