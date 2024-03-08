#general
from pathlib import Path
import os
#project specfici
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
#custom
from example_modules.process import load_and_process
from example_modules import util



summary_df, nims_df, nims_monthly_totals = load_and_process()


def make_plots(summary_df,
              nims_monthly_totals):
    
    BASE_DIR =Path(__file__).parents[3]
    OUTPUT_DIR = BASE_DIR / "outputs"

    plot_nims_monthly(nims_monthly_totals,
                      output_path = OUTPUT_DIR)
    
    plot_summary(summary_df,
                 output_path = OUTPUT_DIR)

#%%
def plot_nims_monthly(nims_monthly_totals: pd.DataFrame,
                      output_path = None, 
                      ):

    fig, ax = plt.subplots()
    nims_plot = sns.lineplot(data = nims_monthly_totals.query('year in [2021, 2022]'),
                x = 'month',
                hue ='year',
                y = 'total',
                palette = 'coolwarm',
                ax= ax,
                linewidth=2,
                )
    y_format = ticker.FuncFormatter(util.million_format)
    nims_plot.yaxis.set_major_formatter(y_format)
    ax = util.set_labels(ax,
                         'Number of NIMS GP attendances',
                         fontsize =12)
    
    ax = util.style_plot(ax)
    plt.show()

    #if path supplied then save figure 
    if output_path:
        plt.savefig(output_path / "test.svg")

#%%
def plot_summary(summary_df: pd.DataFrame,
                 output_path = None):
    for col in ['attended', 'did_not_attend', 'unknown']:
        util.convert_to_proportion(summary_df,
                                   col,
                                   'total_count_of_appointments')
        
    melt_df = summary_df.drop(['total_count_of_appointments'], 
                    axis =1).melt(id_vars = ['weekday', 'appointment_date'],
                                  var_name = 'type',
                                  value_name = 'proportion')

    fig, ax = plt.subplots(1,1,figsize = (10,6))
    summary_plot = sns.lineplot(data = melt_df,
                                x = 'appointment_date',
                                hue ='type',
                                y = 'proportion',
                            #  palette = 'coolwarm',
                                ax= ax,
                                linewidth=2,
                                )
    plt.xticks(melt_df.appointment_date)

    x_format = ticker.FuncFormatter(util.weekday_date_formatter)
    summary_plot.xaxis.set_major_formatter(x_format)
    y_format = ticker.PercentFormatter(xmax=1)
    summary_plot.yaxis.set_major_formatter(y_format)

    util.set_labels(ax,
                    title= 'Proportion of GP attendances by type',
                    fontsize =12)    #
    util.style_plot(ax)
    plt.show()
    if output_path:
        plt.savefig(output_path / "test.svg")