#%%
import yaml

from example_modules import (
    download,
    visualise,
    process,
)



# with open("src/{{ cookiecutter.repo_name.lower().replace(' ', '_').replace('-', '_') }}/example_config.yml", "r") as file:
def run_pipeline():
    with open("{src\\{{ cookiecutter.repo_name.lower().replace(' ', '_').replace('-', '_') }}\\example_config.yml", "r") as file: 
        example_config = yaml.safe_load(file)

    download.download_nhs_data(example_config)

    summary_df, _, nims_monthly_df = process.load_and_process()

    visualise.make_plots(summary_df,
                         nims_monthly_df)
    
if __name__ == "__main__":
    run_pipeline()