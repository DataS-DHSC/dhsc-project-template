eval $(conda shell.bash hook)
conda env create -f environment.yml 
conda activate {{ cookiecutter.repo_name.lower().replace('_', '-').replace(' ', '-') }}-env
git init 
pre-commit install 


