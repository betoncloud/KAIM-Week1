import pandas as pd
from datetime import datetime
def load_data(file_path):
    """
    Load data from from a .csv file
    Args:
        file_path (str): Path to the csv file
    Returns:
        pd.DataFrame: Loaded data.
    """
    dateparse = lambda dates: [datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in dates]
    
    return pd.read_csv(file_path,parse_dates=['datetime'], date_parser=dateparse)
     