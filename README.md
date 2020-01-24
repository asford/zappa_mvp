# Zappa MVP Development Environment

Used to conda, but need to hack out a service with Zappa? This is for you.

This is an MVP hybrid conda/zappa development environment. A local
conda env, specified in `environment.yml`, hosts dev tools and pipenv.
`pipenv` is then used to create an isolated venv for `zappa` to deploy
a `flask` app to lambda.

A `direnv` `.envrc` is provided for interactive work, with a basic set of
`pre-commit` hooks for `flake8`, `mypy`, `black`, [...]

## Setup

1. `conda env create -p ./.conda` the host env.
2. `direnv allow` auto-activation of the host environment.
3. `pipenv install` the deployment env.
4. `pipenv run zappa deploy` to lambda.
