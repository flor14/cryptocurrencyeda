from cryptocurrencyeda.retrieve_data import retrieve_data

import pandas as pd
from pandas._testing import assert_frame_equal


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
