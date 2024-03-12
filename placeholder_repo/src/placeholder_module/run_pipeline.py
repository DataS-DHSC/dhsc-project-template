# %%
#standard
import datetime as dt
from pathlib import Path
#project specific
import yaml
# custom 
from src.placeholder_module.example_modules import (
    download,
    process,
    visualise,
)




def run_pipeline():

    BASE_DIR = Path(__file__).parents[2]
    OUTPUT_DIR = BASE_DIR / "outputs"

    print(BASE_DIR)
    # GJ change when setting up as  cookie cutter to
    # with open("src/{{ cookiecutter.repo_name.lower().replace(' ', '_').replace('-', '_') }}/example_config.yml", "r") as file:
    with open("src\\placeholder_module\\example_config.yml", "r") as file:
        example_config = yaml.safe_load(file)
    example_config['date_stamp'] = dt.datetime.now().strftime("%Y%m%d-%H%M")
    print(example_config.keys())

    download.download_nhs_data(example_config)

    summary_df, _, nims_monthly_df = process.load_and_process()

    visualise.make_plots(summary_df, nims_monthly_df, example_config)

    with open(
        OUTPUT_DIR / f'config_{example_config['date_stamp'] }.yml', 'w'
        ) as outfile:
        yaml.dump(example_config, outfile)#, default_flow_style=False)

if __name__ == "__main__":
    run_pipeline()
