from cryptocurrencyeda.retrieve_data import retrieve_data

import pandas as pd
from pandas._testing import assert_frame_equal

def test_dataframe_specific_date():
    """
    Test dataframe values are equal in a specific date.
    """
    control_data = pd.DataFrame.from_dict({"Symbol":["BTC-USDT"],"Date":["2020-01-10"],"Close":[8192.4]})
    control_data['Date'] = pd.to_datetime(control_data['Date'])
    
    test_data = retrieve_data(symbol="BTC-USDT", start_date="2020-01-09", end_date="2020-01-10")
    
    assert_frame_equal(control_data, test_data)

def test_dataframe_length():
    """
    Test dataframe length.
    """
    test_data = retrieve_data(symbol="BTC-USDT", start_date="2020-01-01", end_date="2020-01-10")
    
    assert len(test_data) == 9
    
def test_dataframe_column_names():
    """
    Test dataframe column names are equal.
    """
    test_data = retrieve_data()
    
    assert test_data.columns.tolist() == ['Symbol', 'Date', 'Close']
