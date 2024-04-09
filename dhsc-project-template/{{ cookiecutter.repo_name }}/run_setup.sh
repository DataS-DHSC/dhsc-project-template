ENV_NAME="{{ cookiecutter.repo_name.lower().replace('_', '-').replace(' ', '-') }}-env"

ENV_FILE="environment.yml"

conda env create -f "$ENV_FILE"

source activate "$ENV_NAME"

git init

pre-commit install 

chmod +x run_setup.sh
