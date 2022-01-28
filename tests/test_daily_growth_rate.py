from cryptocurrencyeda.daily_growth_rate import daily_growth_rate
from pytest import raises

import os

import pandas as pd
import numpy as np
from pandas._testing import assert_frame_equal

def test_daily_growth_rate_df_not_dataframe():
    """
    Test to confirm TypeError is raised when input data is not a dataframe
    """
    df = 'Hello'
    
    with raises(TypeError):
        daily_growth_rate(df, 'Hello')

def test_daily_growth_rate_colname_not_str():
    """
    Test to confirm TypeError is raised when input data is not a string
    """
    df = pd.DataFrame()
    
    with raises(TypeError):
        daily_growth_rate(df, [2])

def test_daily_growth_rate_colname_type_not_float():
    """
    Test to confirm TypeError is raised when the type of input data is not float
    """
    data = {'Date':['2022-01-15', '2022-01-16', '2022-01-17', '2022-01-18'],
            'Close':[20.11, 21.22, 19.13, 18.23]}
    df = pd.DataFrame(data)
    col_name = 'Date'
    
    with raises(TypeError):
        daily_growth_rate(df, col_name)

def test_daily_growth_rate_increasing_price():
    """
    Test to confirm correct output when the price increases
    """
    data = {'Date':['2022-01-15', '2022-01-16', '2022-01-17', '2022-01-18'],
            'Close':[5.00, 10.00, 40.00, 50.00]}
    df = pd.DataFrame(data)
    col_name = 'Close'
    result = daily_growth_rate(df, col_name)
    expected = pd.DataFrame({
        'Date':['2022-01-15', '2022-01-16', '2022-01-17', '2022-01-18'],
        'Close':[5.00, 10.00, 40.00, 50.00],
        'daily_growth_rate(%)':[np.nan, 100.0, 300.0, 25.0]
    }
    )
    assert_frame_equal(expected, result)

def test_daily_growth_rate_decreasing_price():
    """
    Test to confirm correct output when the price decreases
    """
    data = {'Date':['2022-01-15', '2022-01-16', '2022-01-17', '2022-01-18'],
            'Close':[100.00, 40.00, 10.00, 5.00]}
    df = pd.DataFrame(data)
    col_name = 'Close'
    result = daily_growth_rate(df, col_name)
    expected = pd.DataFrame({
        'Date':['2022-01-15', '2022-01-16', '2022-01-17', '2022-01-18'],
        'Close':[100.00, 40.00, 10.00, 5.00],
        'daily_growth_rate(%)':[np.nan, np.nan, -60.0, -75.0, -50.0]
    }
    )
    assert_frame_equal(expected, result)

def test_daily_growth_rate_same_price():
    """
    Test to confirm correct output when the price does not change
    """
    data = {'Date':['2022-01-15', '2022-01-16', '2022-01-17', '2022-01-18'],
            'Close':[50.00, 50.00, 50.00, 50.00]}
    df = pd.DataFrame(data)
    col_name = 'Close'
    result = daily_growth_rate(df, col_name)
    expected = pd.DataFrame({
        'Date':['2022-01-15', '2022-01-16', '2022-01-17', '2022-01-18'],
        'Close':[50.00, 50.00, 50.00, 50.00],
        'daily_growth_rate(%)':[np.nan, 0.0, 0.0, 0.0]
    }
    )
    assert_frame_equal(expected, result)