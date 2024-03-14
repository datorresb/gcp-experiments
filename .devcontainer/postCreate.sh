#!/usr/bin/bash
# Check if Pipfile.lock exists
if [ ! -f "Pipfile.lock" ]; then
    echo -e "Pipfile.lock not found. Generating...\n"
    pipenv lock
fi

# Install dependencies
pipenv sync --dev

# export PYTHONPATH=/workspaces/gcp-experiments:$PYTHONPATH
