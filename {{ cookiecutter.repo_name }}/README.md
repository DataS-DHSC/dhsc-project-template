# `{{ cookiecutter.repo_name }}`

{{ cookiecutter.overview }}

```{warning}
Where this documentation refers to the root folder we mean where this README.md is
located.
```

## Getting started / Setting up 

To start using this project, [first make sure your system meets its
requirements](#requirements).

In order to setup your project, navigate to the root directory and run 

```shell
bash setup_project.bat
```
This will perform a number of steps for you, including:
* Setting up a [virtual environment] #virtual-environments
* Installing pre-commit hooks #pre-commit-hooks
* Initalising a git repository 

## Virtual environments

In programming we might work on several projects concurrently, each project depending on different packages of different versions. For example, our `project1` might require version `2.0.1` of `packageA`, and `project2` might require version `3.2.2` of that same `packageA`. If these versions are different enough, our `project1` and `project2` may not run with the wrong version of `packageA` installed. We use virtual environments so that all our projects can have separate, isolated environments with all their required dependencies inside, so working on one project does not disrupt our workflow in another.

Documentation on virtual environments in Python is available [here](https://docs.python.org/3/tutorial/venv.html)

Running the `setup_project.bat` file will create and environment for you called `{{ cookiecutter.repo_name.lower().replace('_', '-').replace(' ', '-') }}-env` using the `environment.yml` file in the root directory of this project.

This environment contains all the packages needed to run the example code and the pre-commit-hooks

* To activate this virtual environment, run `conda`: `conda activate {{ cookiecutter.repo_name.lower().replace('_', '-').replace(' ', '-') }}-env`.
* When you are finished with this project, run: `conda deactivate`.

## Required secrets and credentials PLACEHOLDER

To run this project, [you need a `.secrets` file with secrets/credentials as
environmental variables][docs-loading-environment-variables-secrets]. The
secrets/credentials should have the following environment variable name(s):

| Secret/credential | Environment variable name | Description                                |
|-------------------|---------------------------|--------------------------------------------|
| Secret 1          | `SECRET_VARIABLE_1`       | Plain English description of Secret 1.     |
| Credential 1      | `CREDENTIAL_VARIABLE_1`   | Plain English description of Credential 1. |

Once you've added, [load these environment variables using
`.env`][docs-loading-environment-variables].


## Pre-commit hooks

Git-hooks are scripts that can identify simple issues in code. Pre-commit hooks are run on every commit to ensure issues are identified before code is pushed to a repository hosting platform such as GitHub. If you have run `setup_project.bat` then pre-commit hooks will run automatically. 

[*Note*] if you try to make a commit in an environment that does not have access to the pre-commit hook packages the hooks will fail. Activate your environment with `conda`: `conda activate {{ cookiecutter.repo_name.lower().replace('_', '-').replace(' ', '-') }}-env` and commit your changes again. 

The pre-commit hooks installed with this project include:
* [*nbstripout*](https://pypi.org/project/nbstripout/) - Clears outputs of Jupyter notebooks - this hook will change your code
* [*isort*](https://pypi.org/project/isort/) - sorts python imports - this hook will change your code
* [*black*](https://pypi.org/project/black/) - formats code to be inline with the [PEP8 style guide for pyhton code](https://peps.python.org/pep-0008/)
* [*flake8*](https://pypi.org/project/flake8/) - 'lints' code, checking for formatting and syntax errors. this hook will *not* change your code for you, but will provide instructions on how to change it
* [*nbqa*](https://pypi.org/project/nbqa/) - applys black and isort to jupyter notebooks. 
* [*detect-secrets*](https://pypi.org/project/detect-secrets/) - *attempts* to identify secret within code. This should be considered as a complement to manually checking for secrets, not a replacemet. This hook will not change your code - but will alert you to the presence of secrets.

To exclude a false positive, add a `pragma` comment such as:

```python
secret = "Password123"  # pragma: allowlist secret
```

* [*bandit*](https://pypi.org/project/detect-secrets/) - *attempts* to identify security risks within code. This hook will not change your code - but will provide a report of possible security risks.

To exclude a false postive, add a `nosec` comment sch as:
```python
some_security_risk() #nosec
```


## Running the pipeline 

The entry point for the example pipeline is stored in the root directory and called `main.py`. This scripts imports and runs the pipline located within the src folder. 
To run the pipeline, run the following code in the terminal (whilst in the root directory of the
project).

```shell
python main.py
```

Alternatively, most Python IDE's allow you to run the code directly from the IDE using a `run` button.


## Documentation

All functions contained in `.py` scripts in the `src` folder should have docstrings explaining what they do, what parameters are passed to the function, what errors the function can raise, and what the function outputs. The [`numpydoc` style](https://numpydoc.readthedocs.io/en/latest/example.html) of formatting docstrings is recommended. Scripts as a whole can contain their own docstrings, in much the same way as a function - simply contain a description of the module inside triple quotation marks `"""` at the top of the script. Examples of such documentation are contained in the `src` modules and submodules.

Having documentation in this way is crucial to meet the minimum requirments of a Reproducible Analytical Pipeline.


## Code of Conduct

Please note that the {{cookiecutter.repo_name}} project is released with a [Contributor Code of Conduct](https://contributor-covenant.org/version/2/1/CODE_OF_CONDUCT.html). By contributing to this project, you agree to abide by its terms.

## License

Unless stated otherwise, the codebase is released under the MIT License. This covers
both the codebase and any sample code in the documentation. The documentation is ©
Crown copyright and available under the terms of the Open Government 3.0 licence.

## Contributing

[If you want to help us build, and improve `{{ cookiecutter.repo_name }}`, view our
contributing guidelines][contributing].

### Requirements

[```Contributors have some additional requirements!```][contributing]

- Python 3.6.1+ installed

- a `.secrets` file with the [required secrets and
  credentials](#required-secrets-and-credentials)
- [load environment variables][docs-loading-environment-variables] from `.env`

To install the contributing requirements, open your terminal and enter:
```shell
python -m pip install -U pip setuptools
pip install -e .[dev]
pre-commit install
```
or use the `make` command:
```shell
make install_dev
```

## Acknowledgements

[This project structure is based on the `govcookiecutter` template
project][govcookiecutter].

[contributing]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/CONTRIBUTING.md
[govcookiecutter]: https://github.com/best-practice-and-impact/govcookiecutter
[docs-loading-environment-variables]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/user_guide/loading_environment_variables.md
[docs-loading-environment-variables-secrets]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/user_guide/loading_environment_variables.md#storing-secrets-and-credentials



## Project Structure 


├───.github
│   └───workflows
└───placeholder_repo
    ├───data
    │   ├───external
    │   ├───interim
    │   ├───processed
    │   └───raw
    ├───outputs
    └───src
        └───placeholder_module
            └───example_modules