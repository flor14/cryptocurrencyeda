import requests
import json
import pandas as pd
    
def retrieve_data(symbol:str, time_period:list, time_frame:list):
    """
    Retrieves historical data from the KuCoin API.
    Using open API adress "https://openapi-v2.kucoin.com/api/v1/market/history/trade"
    
    Parameters
    ----------
    name : array-like
        Inputted cryptocurrency symbol.
    time_period : array-like
        Inputted time period.
    time_frame : array-like
        Inputted time frame.
    
    Returns
    -------
    pandas.DataFrame
        Historical data of the cryptocurrency.
    """
    return None