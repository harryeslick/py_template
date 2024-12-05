#!/bin/bash

pip install uv
uv venv .venv
uv pip install -r requirements.lock 
uv pip install -r requirements-dev.lock
source .venv/bin/activate

# pip install -r ./.devcontainer/dev_requirements.txt
# pip install -e .
