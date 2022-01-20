import requests
import json
import pandas as pd
    
def retrieve_data(symbol:str="BTC-USDT",
                  time_period:str="15min",
                  start_date:str="2019-01-01",
                  end_date:str="2019-02-01",
                 ):
    """
    Retrieves historical data from the KuCoin API.
    Using open API adress "https://openapi-v2.kucoin.com/api/v1/market/history/trade"
    
    Parameters
    ----------
    name : array-like
        Inputted cryptocurrency symbol.
    time_period : str
        Inputted time period.
        1min, 3min, 5min, 15min, 30min, 1hour,
        2hour, 4hour, 6hour, 8hour, 12hour, 1day, 1week
    start_date : array-like
        Inputted time frame.
    end_date : array-like
        Inputted time frame.
    
    Returns
    -------
    pandas.DataFrame
        Historical data of the cryptocurrency.
    """
    # Define the API URL
   
    urllink = "https://api.kucoin.com/api/v1/market/candles?type=15min&symbol=BTC-USDT&startAt=1420434000&endAt=1566789757"
    
    # Make the API call and convert the JSON response to a Python dictionary
    response = requests.get(urllink).json()
    
    # Convert the JSON response to a Python dictionary
    data = response["data"]
    
    # Create a pandas dataframe from the Python dictionary
    cols = ["time", "open", "close", "high",  "low", "volume", "turnover"]
    df = pd.DataFrame(data, columns=cols)
    
    df['time'] = pd.to_datetime(df['time'], unit='s')
    
    # Return the dataframe
    return df