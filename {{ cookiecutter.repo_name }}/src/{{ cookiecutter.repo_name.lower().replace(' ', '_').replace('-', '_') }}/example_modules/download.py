#%%
#standard 
from pathlib import Path
import os

#project specific
import requests
from bs4 import BeautifulSoup
import pandas as pd
# custom
from example_modules import util 

def download_nhs_data(url):
    """Runs the download sub-pipline
    """
    BASE_DIR =Path(__file__).parents[3]
    DATA_DIR = BASE_DIR / "data"
    # url = 'https://digital.nhs.uk/data-and-information/publications/statistical/appointments-in-general-practice/january-2023'
    file_links = scrape_file_links(url)

    file_regex    ='^Appointments.*Summary$' 
    download_file(file_links,
                   file_regex,
                   'summary',
                   DATA_DIR)
       
    file_regex ='Covid Vaccination Appointments'
    download_file(file_links,
                   file_regex,
                   'nims',
                   DATA_DIR)

def scrape_file_links(url: str) -> pd.DataFrame: 
    """ 
    Scrape website links
    
    Scrape the links to valid file formats (.xlsx, .csv) from supplied url

    Args:
        url (str): url of target website

    Returns:
        pd.DataFrame: df with a 'title'colum and a 'link' column containing the href 
    """
    html = requests.get(url =url,
                        timeout = 5)
    
    soup = BeautifulSoup(html.content,
                         "html.parser")
    link_results = soup.select('a[href$=".xlsx"], a[href$=".csv"]')

    file_links_df = pd.DataFrame()
    file_links_df.loc[:,'title'], file_links_df['link'] = [[x.find('p').text for x in link_results],
                                                        [x['href'] for x in link_results]]
    
    return file_links_df
    
def download_file(file_links_df: pd.DataFrame,
                   file_regex: str,
                   file_name: str,
                   data_path: Path):
    
    """
    Download file of interest

    Uses a regular expression to find file of interest in input df,
    then downloads and saves to named directory 

    Args:
        file_links_df (pd.DataFrame): df with a 'title'colum and a 'link' column containing the href
        file_regex (str): regular expression to match against file_links_df 'title'
        file_name (str): name to save file under
        data_path (Path): directory to save file in 
    """
    file_url = file_links_df.link[util.get_regex_match(file_links_df.title,
                                                      file_regex)]
    file = requests.get(file_url,
                        timeout =5 )
    
    with open(data_path / f'{file_name}.{file_url.split('.')[-1]}', 'wb') as output:
        output.write(file.content)     

