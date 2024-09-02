#!/bin/bash

# Check if the script is being sourced
(return 0 2>/dev/null) && sourced=1 || sourced=0

if [ "$sourced" -eq 0 ]; then
    echo "Error: This script should be sourced, not executed."
    exit 1
fi

# Path to the desired virtual environment
VENV_PATH="/home/johnwalshe/projects/nagswithnotions/venv_nagswithnotions"

# Check if the current virtual environment is different from the desired one
if [ "$VIRTUAL_ENV" != "$VENV_PATH" ]; then
    # Deactivate the current virtual environment, if any
    if [ -n "$VIRTUAL_ENV" ]; then
        echo "Deactivating current virtual environment: $VIRTUAL_ENV"
        deactivate
    fi

    # Activate the new virtual environment
    if [ -d "$VENV_PATH" ]; then
        source "$VENV_PATH/bin/activate"
        echo "Activated virtual environment: $VENV_PATH"
    else
        echo "Virtual environment directory not found: $VENV_PATH"
        return 1
    fi
else
    echo "Already in the desired virtual environment: $VENV_PATH"
fi

