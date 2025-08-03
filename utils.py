from objects import Instrument, Portfolio, VarMask
import datetime
from scipy.stats import norm
import numpy as np

def dataframe_to_instruments(dataframe) -> dict[str, Instrument]: # chave: ticker, valor: Objeto instrumento referente ao ticker
    """
    Given a dataframe return a list of Instrument objects
    
    Args:
        dataframe: dataframe of pandas containing the prices of a instrument
    
    Return a dictionary of Instrument objects
    """
    response = {}
    for ticker in dataframe.columns: 
        price_by_date = {}
        for date in dataframe.index:
            price = dataframe.loc[date, ticker]
            price_by_date[date.date()] = price
        instrument = Instrument(ticker=ticker, prices=price_by_date)
        response[ticker] = instrument

    return  response
  


def var_by_instrument(
    portfolio: Portfolio, 
    mask: VarMask,
    ) -> dict[str, float]: # key: ticker, value: var of the instrument 
    '''
    VaR = Z-Score x Std Dev x Amt. Invested
    where:

    Z-Score is a constant used to determine the confidence level (e.g. 95%, 99%, ...)

    Std Dev measure the positions individual volatility

    Tenho que implementar um looping para calcular o var de cada um dos instrumentos do portfolio

    '''
    z_score = norm.ppf(float(mask.confidence_level))

    response = {}

    pf_inst = portfolio.instruments

    for ticker in pf_inst.keys():

        vol = vol_instrument(pf_inst[ticker])[ticker]

        # o total investido de um ativo é a quantidade de ativos * o ultimo preço do ativo.
        amt_inv = portfolio.quantities_dict[ticker] * list(pf_inst[ticker].prices.values())[-1]

        var = z_score * vol * amt_inv

        response[ticker] = var

    
    return response





def corr_instruments(portfolio:Portfolio) -> dict[list, float]: # key: list of tickers, value: correlation 
    """
    Given a portfolio, returns the covariance matrix of the instruments
    """
    
    return




def vol_instrument(instrument:Instrument) -> dict[str, float]: # key: 'ticker', value: volatility of the instrument
    """
    Given an instrument, returns an dicionary with the ticker and the volatiliy.
    Observe que a volatilidade de um ativo é o desvio-padrão dos retornos do mesmo."""

    daily_vol = np.std(instrument.returns) 
    
    annualized = np.sqrt(252)*daily_vol # annualized volatility considering a period of a year 

    return {instrument.ticker: annualized} 

def vol_portfolio(portfolio:Portfolio) -> list:
    """
    Given a portfolio, returns a list with it's volatility of 6 months and of 1 year.

    [vol_6months,annualized]

    """

    daily_vol = np.std(portfolio.return_portfolio(), ddof=1) # Std Dev amostral

    vol_6months = np.sqrt(126)*daily_vol

    annualized = np.sqrt(252)*daily_vol

    return [vol_6months,annualized]

def var_carteira(portfolio: Portfolio, mask: VarMask) -> float:
    """
    Given a portfolio and a Var mask, returns the 
    """

    z_score = norm.ppf(float(mask.confidence_level))

    vol = vol_portfolio(portfolio)[0]

    amt_inv = list(portfolio.value_portfolio().values())[-1]

    var = z_score * vol * amt_inv

    return var
