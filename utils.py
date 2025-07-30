from objects import Instrument, Portfolio, VarMask


def dataframe_to_instruments(dataframe) -> dict[str, Instrument]: # chave: ticker, valor: Objeto instrumento referente ao ticker
    """
    Given a dataframe return a list of Instrument objects
    
    Args:
        dataframe: dataframe of pandas containing the prices of a instrument
    
    Return list of Instrument objects
    """
    pass

    """
    response = {}
    for ticker in dataframe:
        prices_ticker = dataframe[ticker]
        instrument = Instrument(ticker=ticker, prices=prices_ticker)
        response[ticker] = instrument
    
    return response
    """

def portfolio_var_by_instrument(
    portfolio: Portfolio, 
    mask: VarMask,
): #portfolio_var_by_instrument 
    '''confianca == % do var (0.90, 0.95, 0.99). dias == quantidade de dias analisado'''

    # Dada uma carteira, calcula o car de cada ativo (instrumento) na carteira. -> Dict[ticker, float(valor do instrumento)]

    # Dois dicionarios, Dict[ticker, Dict[datetime.datime, float(valor do instrumento)]]

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


def corr_ativos():
    # Dados os ativos de uma carteira calcula a correlação entre eles.
    return

def vol_carteira():
    # Dada uma carteira, calcula a volatilidade da mesma.
    return


def vol_ativo():
    # Dado um ativo, calcula a volatilidade do mesmo.
    # Observe que a volatilidade de um ativo é o desvio-padrão do mesmo.
    return


def var_carteira():

    # Dada uma carteira, calcula o var da carteira.
    # Chama a função (var_ativo_carteira) que calcula o var por ativo (instrumento)
    # Chama a função (vol_ativo) que é o desvio padrão usado no calculo do var
    return
