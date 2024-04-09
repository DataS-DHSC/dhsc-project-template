import os
import shutil

from pathlib import Path

ext_dir = Path(__file__).parents[1]
base_dir = ext_dir / '{{cookiecutter.repo_name}}'
def remove(path):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)

keep_example_code = '{{cookiecutter.include_example_code}}' == 'yes'
print(keep_example_code)
if not keep_example_code:
    print('remove firing')
    #remove exitsing src folder
    src_path = base_dir / 'src'
    print(src_path)
    remove(src_path)
    #make new empty src folder
    os.makedirs(src_path, exist_ok=True)

    



