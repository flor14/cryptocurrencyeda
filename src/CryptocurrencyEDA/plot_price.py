def plot_price(price_df, name, window):
    """
    Plot the price of the cryptocurrenty inputted over window specified.

    Parameters
    ----------
    price_df : pandas DataFrame
        Data frame with time and price data.
    name: str
        Name of the cryptocurrency of interest.
    window: list
        List containing two date objects.

    Returns
    -------
    plot: plot object
        An altair plot object.

    Examples
    >>> plot_price(price_df, "BTCBitcoin", [2021-01-01, 2021-12-31])
    """
