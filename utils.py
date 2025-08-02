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
  


def portfolio_var_by_instrument(
    portfolio: Portfolio, 
    mask: VarMask,
): #portfolio_var_by_instrument 
    '''confianca == % do var (0.90, 0.95, 0.99). dias == quantidade de dias analisado'''

    # Dada uma carteira, calcula o car de cada ativo (instrumento) na carteira. -> Dict[ticker, float(valor do instrumento)]

    # Dois  responsenarios, Dict[ticker, Dict[datetime.datime, float(valor do instrumento)]]
    z_score = norm.ppf(float(mask.confidence_level))

    '''
    VaR = Z-Score x Std Dev x Amt. Invested
    where:

    Z-Score is a constant used to determine the confidence level (e.g. 95%, 99%, ...)

    Std Dev measure the positions individual volatility
    '''

    """
    instrument_prices = portfolio.instruments
    posicoes = portfolio.posicoes

    time_horizon = mask.time_horizon
    confidence_level = mask.confidence_level 
    """
    return





def corr_instruments(retorno_portfolio): # 
    """
    Given the array of daily returns of a portfolio, returns the covariance matrix of the instruments
    """
    
    return




def vol_instrument(instrument:Instrument) -> dict[str, float]: # key: 'ticker', value: volatility of the instrument
    """
    Given an instrument, returns an dicionary with the ticker and the volatiliy.
    Observe que a volatilidade de um ativo é o desvio-padrão dos retornos do mesmo."""

    daily_vol = np.std(instrument.returns) 
    return {instrument.ticker: daily_vol} 

def vol_portfolio():
    """""Dada uma carteira, calcula a volatilidade da mesma."""

    return 

def var_carteira():

    return
