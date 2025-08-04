from objects import Instrument, Portfolio, VarMask
import datetime
from scipy.stats import norm
import numpy as np
import pandas as pd
import random

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
  
def portfolio_generator(seed, ativos:list):
    random.seed(seed)
    quantidade_de_cada_ativo = {}
    for ticker in ativos:
        quant = random.randint(0,1000) # quantidade de cada ativo da carteira 
        quantidade_de_cada_ativo[ticker] = quant

    return quantidade_de_cada_ativo


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


def corr_instruments(portfolio:Portfolio) -> pd.DataFrame: 
    """
    Given a portfolio, returns a pandas dataframe with the covariance matrix of its instruments.
    """
    # montando um dataframe a partir dos retornos
    data = {}
    for ticker, inst in portfolio.instruments.items():
        rets = inst.return_by_instrument()  
        data[ticker] = rets

    df = pd.DataFrame(data) 

    corr = df.corr()

    return corr


def vol_instrument(portfolio:Portfolio) -> dict[str, float]: # key: 'ticker', value: volatility of the instrument
    """
    Given an instrument, returns an dicionary with the ticker and the volatiliy.
    Observe que a volatilidade de um ativo é o desvio-padrão dos retornos do mesmo."""
    response = {}
    for ticker in portfolio.instruments.keys():
        daily_vol = np.std(portfolio.instruments[ticker].returns) 
    
        annualized = np.sqrt(252)*daily_vol # annualized volatility considering a period of a year 
        response[ticker] = annualized
    return response 

def vol_portfolio(portfolio:Portfolio) -> dict[str, float]:
    """
    Given a portfolio, returns a list with it's volatility of 6 months and of 1 year.

    Returns:
        dict[str, float] 

    """

    daily_vol = np.std(portfolio.return_portfolio(), ddof=1) # Std Dev amostral

    vol_6months = np.sqrt(126)*daily_vol

    annualized = np.sqrt(252)*daily_vol

    return {'vol em 6 meses': vol_6months,'vol anualizado': annualized}

def var_carteira(portfolio: Portfolio, mask: VarMask) -> float:
    """
    Given a portfolio and a Var mask, returns the 
    """

    z_score = norm.ppf(float(mask.confidence_level))

    vol = vol_portfolio(portfolio)['vol em 6 meses']

    amt_inv = list(portfolio.value_portfolio().values())[-1]

    var = z_score * vol * amt_inv

    return var

def component_var(portfolio:Portfolio, mask:VarMask):
    """
    Calcula o impacto de cada instrumento no var do portfolio.
    """

    days = mask.time_horizon 

    z_score = norm.ppf(float(mask.confidence_level))

    valor_carteira = list(portfolio.value_portfolio().values())[-1]

    # montando um dataframe de retornos diarios para facilitar contas
    data = {}
    for ticker, inst in portfolio.instruments.items():
        rets = inst.return_by_instrument()  # array de retornos simples
        data[ticker] = rets
    returns_df = pd.DataFrame(data)

    weight_vals = {}
    for ticker in portfolio.instruments.keys():
        last_price = list(portfolio.instruments[ticker].prices.values())[-1]
        qty = portfolio.quantities_dict.get(ticker, 0)
        weight_vals[ticker] = last_price * qty

    w_series = pd.Series(weight_vals)
    w_series = w_series / w_series.sum()  # normalizando
    w = w_series.to_numpy()

    cov = returns_df.cov()
    
    sigma_p_daily = np.sqrt(w @ cov.to_numpy() @ w)

    Sigma_w = cov.to_numpy() @ w 

    mvar_vals = z_score * np.sqrt(days) * (Sigma_w / sigma_p_daily) * valor_carteira

    mvar = pd.Series(mvar_vals, index=returns_df.columns) # marginal Var

    comp_var = w_series * mvar # component Var

    var_total = z_score * np.sqrt(days) * sigma_p_daily * valor_carteira

    pct_contrib_series = comp_var / var_total # contribuição percentual

    return (mvar.to_dict(),
        comp_var.to_dict(),
        pct_contrib_series.to_dict())

