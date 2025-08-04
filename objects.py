import datetime
import numpy as np

class VarMask:
    def __init__(
        self,
        time_horizon: int = 126,
        confidence_level: float = 0.99,
    ):
        """
        Object that takes the parameters for the var calculation.

        time_horizon: int = period of time that look behind for prices 
        confidence_level: int = 
        """
        self.time_horizon = time_horizon
        self.confidence_level = confidence_level
    
    def __str__(self):
        return f"Var Mask looking {self.time_horizon} days and confidence level of {self.confidence_level}"


class Instrument:
    def __init__(
        self,
        ticker: str = None,
        prices: dict[datetime.datetime, float] = {},
        type: str = None,
    ):
        self.ticker = ticker
        self.prices = prices
        self.returns = self.return_by_instrument() #array of daily returns

    def return_by_instrument(self):
        """
        Returns an array of daily returns of a single instrument.
        """
        prices_list = list(self.prices.values())
        prices_array_tomorrow = np.array(prices_list[1:])
        prices_array_today = np.array(prices_list[:-1])
        retorno = (prices_array_tomorrow/prices_array_today - 1) 
        return retorno
        

class Portfolio: # posicoes: {'PETR4': 3, 'VALE3': 15, ...}
    """       # instruments: {'PETR4': Instrument('PETR4', {06-03-2025: 27.05})}
    """
    def __init__(
        self,
        quantities_dict: dict[str, float] = {},    # chave: ticker, valor: quantidade de um determinado ativos
        instruments: dict[str, Instrument] = {}  # chave: ticker, valor: Objeto instrumento referente ao ticker
    ):
        self.quantities_dict = quantities_dict
        self.instruments = instruments
        self.pl = self.value_portfolio # pl é patrimônio líquido == valor do portifolio

    def __str__(self):
        """
        Apresentação do Portifolio.
        """
        response = "O Portfolio tem:\n----------------------------------------------------------"
        for ticker in self.quantities_dict.keys(): 
            posicao = self.quantities_dict[ticker] * list(self.instruments[ticker].prices.values())[-1]
            ticker_str = f"""\n{ticker}: {self.quantities_dict[ticker]} papéis. Com posição R${posicao}\n----------------------------------------------------------"""
            response += ticker_str

        return response



    def value_portfolio(self) -> dict[datetime.datetime, float]:
        """
        retorna o valor total do portifolio, que é calculado assim:
        somatorio para todos os instrumentos de (preço instrumento tempo t-1  *  quantidade do instrumento)
        """
        
        list_dates = list(self.instruments[list(self.instruments.keys())[0]].prices.keys())
        array_soma = np.zeros_like(list_dates, dtype=float)

        for ticker in self.instruments.keys():
            
            prices_array = np.array(list(self.instruments[ticker].prices.values()), dtype=float)
            quantity = self.quantities_dict[ticker]
            array_soma += prices_array * quantity 


        response = dict(zip(list_dates, array_soma))
        return response



    def return_portfolio(self):
        """
        Returns an array of daily returns of a portfolio.
        """
        
        sample_returns = list(self.instruments[list(self.instruments.keys())[0]].returns) #pega uma lista com os retornos do primeiro instrumento, para poder criar um array de zeros com a mesma dimensão 
        retornos = np.zeros_like(sample_returns, dtype=float)
        for ticker in self.instruments.keys():
            array_pl = np.array(list(self.pl().values())[:-1]) # array com o valor do portfolio por dia, cortado o ultimo elemento para simbolizar o dia anterior
            array_prices_instrument = np.array(list(self.instruments[ticker].prices.values())[:-1]) 

            weight = array_prices_instrument * self.quantities_dict[ticker] / array_pl

            retornos += self.instruments[ticker].returns * weight

        return retornos
    
