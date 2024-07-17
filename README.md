# `dhsc-project-template`

Cookiecutter templates for Python-based projects within
the DHSC.

This Cookiecutter offers two templates

1) An Analytical Project template - for analytical projects
2) A Package template - for developing software or packages

These templates help to set up standardised project structures, and [includes security
features using pre-commit hooks][docs-pre-commit]

The Package template includes the same features as the Analytical Project template, 
but has some addtional features such as unit testing and sphix automatic documentation.

If you are unsure which template to use, we reccomend the project template. 

|                               	| **Analytical Project Template** 	| **Package Template** 	|
|-------------------------------	|----------------------	|----------------------	|
| Standardised Folder Structure 	|   </center>:heavy_check_mark:</center>   |   </center>:heavy_check_mark:</center>   |
| Pre-commit Hooks              	|   :heavy_check_mark:   |   :heavy_check_mark:   |
| Example Analysis Pipeline     	|   :heavy_check_mark:   |   :heavy_check_mark:   |
| Automatic Documentation       	|         :x:            |   :heavy_check_mark:   |
| Example Unit Tests            	|         :x:            |   :heavy_check_mark:   |

## Getting started

[First, make sure your system meets the
requirements](#requirements-to-create-a-cookiecutter-template). 

### Downloading the template

To download the template - you will need the [`cookiecutter` python package installed](#requirements-to-create-a-cookiecutter-template) - preferably in a virtual environment. 

1. Open your terminal, navigate to the directory where you want your new repository to exist.
  
2. Create a conda environment to hold cookiecutter - then activate it
    ```shell
    conda create -n cookiecutter-setup-env
    conda activate cookiecutter-setup-env
    ```
     
3. Download python and cookiecutter
   ```shell
   conda install python
   pip install cookiecutter
   ```

4. Run the following command to download the latest stable release of the template:
   ```shell
   python -m cookiecutter https://github.com/DataS-DHSC/dhsc-project-template.git
   ```
   or for a specific branch, tag, or commit SHA `{SPECIFIC}`, run:
   ```shell
   python -m cookiecutter https://github.com/DataS-DHSC/dhsc-project-template.git --checkout {SPECIFIC}
   ```

5. Follow the prompts; if you are asked to re-download `dhsc-project-template`, input `yes`.
   - Default responses are shown in the squared brackets; to use them, leave your response blank, and press enter.
   - Once you've answered all the prompts, your project will be created.
  
6. Deactivate your cookiecutter setup environment:
    ```shell
    conda deactivate cookiecutter-setup-env
    ```

### Setting up your project

Now your template is downloaded you're ready to set up your project

1. Navigate to the root directory of your new project in a **bash terminal** (for example git bash or the integrated bash terminal in vs code)

2.  In your terminal type
     ```shell
    bash -i run_setup.bat
    ```
    This will perform a number of steps for you, including:
    * Setting up a virtual environment (containing packages needed to run pre-commit hooks
    * Installing pre-commit hooks
    * Initalising a git repository 

3. Set up a repo on Github to track your project folder
   Create a new repo on Github and copy the url.
   Stage all your project files, and make your first commit
   
   ```shell
   git remote add origin {url}
   git branch -m main
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```

Once you've completed these steps, [consider making some optional changes before
kicking off your project development](#optional-changes-to-consider-post-project-creation).

### Requirements to create a cookiecutter template


To get started your system should meet the following requirements:

1. Python 3.6.1+ installed
2. The `cookiecutter` package installed

#### Installing the `cookiecutter` package

There are many ways to install the `cookiecutter` package. Our recommendation is to
install it within a virtual environment.

After creating your virtual environment you can install cookiecutter using either conda 

```shell
conda install conda-forge::cookiecutter
```

or pip

```shell
python -m pip install cookiecutter
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
[docs-pre-commit]: https://github.com/DataS-DHSC/dhsc-project-template/blob/main/dhsc-project-template/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/user_guide/pre_commit_hooks.md
[homebrew]: https://brew.sh/
[issue-windows-os]: https://github.com/best-practice-and-impact/govcookiecutter/issues/20
[pluralsight]: https://www.pluralsight.com/tech-blog/managing-python-environments/
[youtube]: https://www.youtube.com/watch?v=N7_d3k3uQ_M
[issue20]: https://github.com/best-practice-and-impact/govcookiecutter/issues/20
[govcookiecutter]: https://github.com/best-practice-and-impact/govcookiecutter
