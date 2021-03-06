# %load q04_get_match_specific_df/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
import pandas as pd

def get_match_specific_df(match_code):
    
    dfi=ipl_df.groupby('match_code').get_group(598057)
    
    return dfi



