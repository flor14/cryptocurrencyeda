def plot_price(df):
    """
    Plot the price of the cryptocurrenty inputted over window specified.

    Parameters
    ----------
    df : pandas DataFrame
        Data frame with cryptocurrency name, date and close price.

    Returns
    -------
    plot: plot object
        An altair plot object.

    Examples
    >>> df = retrieve_data(symbol:str="BTC-USDT",
                  time_period:str="15min",
                  start_date:str="2019-01-01",
                  end_date:str="2019-02-01",
                 )
    >>> plot_price(df)
    """
    name = df.Name[0]
    chart = alt.Chart(df).mark_line().encode(
        x=alt.X('Date', title = 'Date'),
        y=alt.Y('Close', title = 'Close Price')
    ).properties(title = symbol + ': close price over time'
                ).configure_title(fontSize = 18,
                                  anchor = 'start'
                                 ).configure_axis(labelFontSize=10,
                                                  titleFontSize=15
                                                 )
    return chart
