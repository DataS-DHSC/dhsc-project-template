import os
import shutil

from pathlib import Path

base_dir = Path(os.getcwd())
def remove(path):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)

keep_example_code = '{{cookiecutter.include_example_code}}' == 'yes'
if not keep_example_code:
    #remove exitsing src folder
    src_path = base_dir / 'src'
    remove(src_path)
    #make new empty src folder
    os.makedirs(src_path, exist_ok=True)
    #remove old env
    remove(base_dir /'environment.yml')
    #rename no example code env
    os.rename('no_ex_code_environment.yml', 'environment.yml')
    



