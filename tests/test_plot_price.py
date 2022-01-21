from CryptocurrencyEDA import CryptoCurrencyEDA
import numpy as np
import altair as alt
import pandas as pd

helper_data = pd.DataFrame({
    'Name': np.array(['Bitcoin', 'Bitcoin', 'Bitcoin', 'Bitcoin' ,'Bitcoin']),
    'Date': np.array(['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05']),
    'Close': np.array([29374.15189, 32127.26794, 32782.02447, 31971.91352, 33992.42934])
})

helper_plot = CryptoCurrencyEDA.plot_price(helper_data)

def test_plot_price():
    assert helper_plot.encoding.x.field == 'Date', 'x_axis should be mapped to the x axis'
    assert helper_plot.encoding.y.field == 'Close', 'y_axis should be mapped to the y axis'
    assert helper_plot.mark == 'line', 'mark should be a line'
    assert helper_plot.encoding.y.type == 'quantitative', "y-axis should be of the type 'quantitative"
