import pandas as pd
import csv

def growth_rate(dataframe, col_name):

    """Function to calculate daily growth rate 
    Parameters
    ----------
    dataframe : pandas DataFrame
        Data frame with date and price data.
    col_name: str
        Name of the column holding daily ending price data. 

    Returns
    -------
    dataframe:
        A dataframe with a new column of daily growth rate

    Examples
    -------
    >>> growth_rate(price_df, closing_price)
               
    """

    