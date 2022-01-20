from cryptocurrencyeda.daily_growth_rate import daily_growth_rate
from pytest import raises

import os

import pandas as pd
import numpy as np
from pandas._testing import assert_frame_equal

def test_daily_growth_rate_df_not_dataframe():
    df = "Hello"
    
    with raises(TypeError):
        daily_growth_rate(df, "Hello")

def test_daily_growth_rate_colname_not_str():
    df = pd.DataFrame()
    
    with raises(TypeError):
        daily_growth_rate(df, [2])

def test_daily_growth_rate_colname_type_not_float():
    data = {'Date':['2022-01-15', '2022-01-16', '2022-01-17', '2022-01-18'],
        'Price':[20.11, 21.22, 19.13, 18.23]}
    df = pd.DataFrame(data)
    col_name = "Date"
    
    with raises(TypeError):
        daily_growth_rate(df, col_name)

def test_daily_growth_rate_increasing_price():
    data = {'Date':['2022-01-15', '2022-01-16', '2022-01-17', '2022-01-18'],
        'Price':[5.00, 10.00, 40.00, 50.00]}
    df = pd.DataFrame(data)
    col_name = "Price"
    result = daily_growth_rate(df, col_name)
    expected = pd.DataFrame({"daily_growth_rate":[np.nan, 1.0, 3.0, 0.25]})
    assert_frame_equal(expected, result)

def test_daily_growth_rate_decreasing_price():
    data = {'Date':['2022-01-15', '2022-01-16', '2022-01-17', '2022-01-18'],
        'Price':[100.00, 40.00, 10.00, 5.00]}
    df = pd.DataFrame(data)
    col_name = "Price"
    result = daily_growth_rate(df, col_name)
    expected = pd.DataFrame({"daily_growth_rate":[np.nan, -0.6, -0.75, -0.5]})
    assert_frame_equal(expected, result)

def test_daily_growth_rate_same_price():
    data = {'Date':['2022-01-15', '2022-01-16', '2022-01-17', '2022-01-18'],
        'Price':[50.00, 50.00, 50.00, 50.00]}
    df = pd.DataFrame(data)
    col_name = "Price"
    result = daily_growth_rate(df, col_name)
    expected = pd.DataFrame({"daily_growth_rate":[np.nan, 0.0, 0.0, 0.0]})
    assert_frame_equal(expected, result)