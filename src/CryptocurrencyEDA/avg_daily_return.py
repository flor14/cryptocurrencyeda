import pandas as pd

def avg_daily_return(prices):
    """
    Outputs the average daily return of the inputted cryptocurrency price.
    
    Parameters
    ----------
    prices : array-like
        Inputted cryptocurrency price.
    
    Returns
    -------
    float
        Average daily return of the cryptocurrency.
    
    Examples
    --------
    >>> avg_daily_return("BTCBitcoin")
    >>> 0.1
    """
    if not isinstance(prices, (list, pd.Series)):
        raise ValueError(
            'input must be list or pandas series')
        
    return_sum = 0
    for i in range(len(prices)-1):
        return_sum += prices[i+1] - prices[i]
    return return_sum / len(prices)