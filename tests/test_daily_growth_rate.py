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