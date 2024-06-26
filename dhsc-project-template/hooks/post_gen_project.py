import os
import shutil

from pathlib import Path

def remove(path):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)

base_dir = Path(os.getcwd())

keep_example_code = '{{cookiecutter.include_example_code}}' == 'yes'
if not keep_example_code:
    #remove exitsing src folder
    src_path = base_dir / 'src'
    remove(src_path)
    #make new empty src folder
    os.makedirs(src_path, exist_ok=True)

    



