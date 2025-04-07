#!/bin/bash
echo "Installing Poetry..."
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"
echo "Installing dependencies using Poetry..."
poetry config virtualenvs.create false  # install in system env (for CodeBuild)
poetry install --no-interaction --no-ansi
