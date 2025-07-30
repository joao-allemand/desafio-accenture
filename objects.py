import datetime

class VarMask:
    def __init__(
        self,
        time_horizon: int = 132,
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


class Portfolio:
    """
    """
    def __init__(
        self,
        posicoes: dict[str, float] = {},    # chave: ticker, valor: posição
        instruments: dict[str, Instrument] = {}  # chave: ticker, valor: Objeto instrumento referente ao ticker
    ):
        self.posicoes = posicoes
        self.instruments = instruments
