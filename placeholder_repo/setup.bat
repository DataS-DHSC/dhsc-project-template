eval $(conda shell.bash hook)
conda env create -f environment.yml 
source activate hook_test_env
conda list
git init 
pre-commit install 


