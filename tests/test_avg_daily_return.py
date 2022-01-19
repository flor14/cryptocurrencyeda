from cryptocurrencyeda.avg_daily_return import avg_daily_return
import pandas as pd

# create a testing dataframe
df = pd.DataFrame({'Date':['2022-01-15', '2022-01-16', '2022-01-17', '2022-01-18'],
                   'Price':[1.5, 2.5, 3.5, 4.5]})
output = avg_daily_return(df['Price'])

def test_output_value():
    assert output == 1

def test_output_type():
    assert isinstance(output, float)

def test_if_raise_error_with_wrong_input():
    test_input = 1.5
    with pytest.raises(ValueError, 
                       match="input must be list or pandas series"):
        cryptocurrencyeda.avg_daily_return(test_input)
