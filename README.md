# `dhsc-project-template`

A cookiecutter template for analytical, Python-based projects within
the DHSC.

This template helps to set up standardised project structures, and [includes security
features using pre-commit hooks]({{ cookiecutter.repo_name }}/docs/user_guide/pre_commit_hooks.md) 

This cookiecutter template is designed for analytical projects in python. 
If you are developing software or packages - see our dhsc_pacakge_template,
which contains additionaly functionality such as unit testing and sphix documentation,
and  also acts as an installable template.


## Getting started

[First, make sure your system meets the
requirements](#requirements-to-create-a-cookiecutter-template). Next, open your
terminal, navigate to the directory where you want your new repository to exist. Then
run the following command for the latest stable release:

```shell
python -m cookiecutter https://github.com/DataS-DHSC/dhsc-project-template.git
```

or for a specific branch, tag, or commit SHA `{SPECIFIC}`, run:

```shell
python -m cookiecutter https://github.com/DataS-DHSC/dhsc-project-template.git --checkout {SPECIFIC}
```

Follow the prompts; if you are asked to re-download `dhsc-project-template`, input `yes`.
Default responses are shown in the squared brackets; to use them, leave your response
blank, and press enter.

Once you've answered all the prompts, your project will be created. Then:


1. Navigate to the root directory of your new project in a **bash terminal**

2.  In your terminal type
     ```shell
    bash -i setup_project.bat
    ```
    This will perform a number of steps for you, including:
    * Setting up a virtual environment
    * Installing pre-commit hooks
    * Initalising a git repository 

3. Stage all your project files, and make your first commit
   ```shell
   git add .
   git commit -m "Initial commit"
   ```

Once you've completed these steps, [consider making some optional changes before
kicking off your project development](#optional-changes-to-consider-post-project-creation).

### Requirements to create a cookiecutter template


To get started your system should meet the following requirements:

1. Python 3.6.1+ installed
2. The [`cookiecutter` package installed](https://github.com/best-practice-and-impact/govcookiecutter/blob/main/README.md#installing-the-cookiecutter-package)


#### Installing the `cookiecutter` package

There are many ways to install the `cookiecutter` package. Our recommendation is to
install it at the system or user level, rather than as a Python package with `pip` or
`conda`. This ensures it is isolated from the rest of your system, and always available.

For macOS, open your terminal, and [install `cookiecutter` with Homebrew][homebrew]:

```shell
brew install cookiecutter
```

For Debian/Ubuntu, use the following commands:

```shell
sudo apt-get install cookiecutter
```

Otherwise, you can install `cookiecutter` with `pip` — you may wish to create a virtual
environment first:

```shell
python -m pip install --user cookiecutter
```

## Optional changes to consider post-project creation

Here are some suggested changes to make before your first commit:
- Checkout the `READ.ME` and have a look inside the `docs/user_guide` folder
  to familarise yourself with features of the project template
- make sure the `README.md` reflects what you want to do with your project
- (if present) confirm that the pull or merge request template checklists meet your
  requirements
  - These can be found at `.github/pull_request_template.md` (GitHub)

## Licence

Unless stated otherwise, the codebase is released under the MIT License. This covers
both the codebase and any sample code in the documentation. The documentation is ©
Crown copyright and available under the terms of the Open Government 3.0 licence.

## Contributing

[If you want to help us build, and improve `dhsc_python_template`, view our contributing
guidelines](CONTRIBUTING.md).

## Acknowledgements

[This project structure is based on the `govcookiecutter` template
project][govcookiecutter].


[aqua-book]: https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government
[docs-pre-commit]: https://github.com/DataS-DHSC/dhsc-project-template/blob/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/user_guide/pre_commit_hooks.md
[homebrew]: https://brew.sh/
[issue-windows-os]: https://github.com/best-practice-and-impact/govcookiecutter/issues/20
[pluralsight]: https://www.pluralsight.com/tech-blog/managing-python-environments/
[youtube]: https://www.youtube.com/watch?v=N7_d3k3uQ_M
[issue20]: https://github.com/best-practice-and-impact/govcookiecutter/issues/20
[govcookiecutter]: https://github.com/best-practice-and-impact/govcookiecutter
