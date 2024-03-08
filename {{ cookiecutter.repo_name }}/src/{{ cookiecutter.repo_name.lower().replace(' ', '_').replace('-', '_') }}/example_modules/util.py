import re
from pathlib import Path
import numpy as np 
import seaborn as sns
import matplotlib.dates as mdates
import pandas as pd
import matplotlib.pyplot as plt

def million_format(x, pos):
    """format ticks to be in million format"""
    s = f'{x/1000000:,g}m'
    return s

def weekday_date_formatter(x, pos):
    """format ticks to be first letter of weekday,
    and date below if Sunday """
    weekday_fmt = mdates.DateFormatter('%a')
    date_fmt = mdates.DateFormatter('%d')
    if  weekday_fmt(x) == 'Sun':
         s = f'{weekday_fmt(x)[0]}\n {date_fmt(x)}'
    else:
        s = weekday_fmt(x)[0]
    return s

def get_regex_match(series: pd.Series, 
                    regex: str):    
    """returns index of row in series that match regular expression"""
    bool_array = series.apply(lambda x: bool(re.search(regex, str(x).strip())))
    match_idx = bool_array[bool_array].index[0]
    return match_idx

def set_labels(ax: plt.Axes, 
               title:str,
               fontsize: int) -> plt.Axes:
    """Modify axes labels

    Formats labels from snake case, sets text color to grey

    Args:
        ax (plt.Axes): axis of plot to update
        title (str): title of plot
        fontsize (int): fontsize of smaller lables (xlabel, ylabel, legend title)

    Returns:
        plt.Axes: axis of plot to update
    """
     
    ax.set_xlabel(xlabel = ax.get_xlabel().replace('_',' ').capitalize(),
                  color= 'grey',
                  fontsize = fontsize)
    ax.set_ylabel(ylabel = ax.get_ylabel().replace('_',' ').capitalize(),
                   color= 'grey',
                   fontsize = fontsize)
    ax.set_title(title,
                 pad=10,
                 fontsize = np.ceil(fontsize *1.3),
                 color= 'grey',)
    #if legend exists then also update
    if ax.get_legend() is not None:
        handles, labels = ax.get_legend_handles_labels()
        labels = [l.replace('_',' ').capitalize() for l in labels]
        ax.legend(title = ax.get_legend().get_title().get_text().replace('_',' ').capitalize(),
                  handles= handles,
                  labels = labels,
                  labelcolor= 'grey')
        ax.get_legend().get_title().set_color('grey')
    return ax


def convert_to_proportion(df: pd.DataFrame,
                           x: str,
                           total: str):
    """converts column x of data frame into a proportion of x/total"""
    df[x] = df[x].astype('float')
    df.loc[:,x] = df[x] / df[total]
    return df



def style_plot(ax: plt.Axes) -> plt.Axes:
    """styles plot

    Sets major x gridlines, modify axis, ticks and labels

    Args:
        ax (Axes):  axis of plot to update

    Returns:
        _type_:  axis of plot to update
    """
    sns.despine()
    ax.grid(which='major', alpha=0.5, linestyle = ':', axis = 'x')
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_linewidth(2)
        ax.spines[spine].set_color('lightgray')
        ax.tick_params(width=1,
                       color= 'grey',
                       length = 4,
                       labelcolor = 'grey',
                       labelfontfamily ='sans-serif')
    return ax 