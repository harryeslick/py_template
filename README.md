# Python Project Template

[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/copier-org/copier)

This is a repository template for building python projects.
It uses:

- [Copier](https://copier.readthedocs.io/) is used for templating
- `rye` for package and dependency management
- `uv` is used for dependencies within the dev container, using the `rye` `requirements.lock` file
- `mkdocs` for documentation with deployment via `gh_actions`
- `pytest` with `pytest-cov` for code coverage
- `pre-commit` used used to enforce code formatting using `ruff`, and spelling using `codespell`

## Project Organization

- `.github/workflows`: Contains GitHub Actions used for building, testing, and publishing.
- `.devcontainer/devcontainer.json`: Contains the configuration for the development container for VSCode, including  VSCode extensions to install.
- `.vscode/settings.json`: Contains VSCode settings specific to the project,
- `src`: Place new source code here.
- `tests`: Contains tests using `pytest`
- `pyproject.toml`: Contains metadata about the project and configurations for additional tools used to format, lint, type-check, and analyze Python code.

This template was originally based on Based on template from [Microsoft](https://github.com/microsoft/python-package-template)

## Using this template

- If required, install `Copier` using `uv tool install copier`
- Create new project from the template repo using `copier copy https://github.com/harryeslick/py_template path/to/destination`
- change workspace `titleBar.activeBackground` in `./.vscode/settings.json`

## Installation

### Local development

- setup environment `rye sync`
- setup pre-commit `pre-commit install-hooks`

### Using VSCode DevContainer

- open project folder in vscode
- install VSCode Dev-container extension
- run / Build Dev-container
