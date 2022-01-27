from cryptocurrencyeda.avg_daily_return import avg_daily_return
import pandas as pd
from pytest import raises

# create a testing dataframe
df = pd.DataFrame({'Date':['2022-01-15', '2022-01-16', '2022-01-17', '2022-01-18'],
                   'Price':[1.5, 2.5, 3.5, 4.5]})
output = avg_daily_return(df['Price'])

def test_output_value():
    """A test to check if avg_daily_return outputs the correct value"""
    output = avg_daily_return(df['Price'])
    assert output == 1

def test_output_type():
    """A test to check if the output of avg_daily_return is in correct type"""
    assert isinstance(output, float)

def test_if_raise_error_with_wrong_input():
    """A test to check if avg_daily_return raises error for the wrong input type"""
    test_input = 1.5
    with raises(ValueError, 
                       match="input must be list or pandas series"):
        avg_daily_return(test_input)
