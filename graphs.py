from objects import Instrument, Portfolio, VarMask
from scipy.stats import norm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

def plot_price_series(
    portfolio,
    normalize: bool = False):
    """
    Plota os preços de todos os instrumentos do portfolio.

    Args:
        portfolio: seu objeto Portfolio.

        normalize: se True, plota retornos normalizados (100 * (P_t / P_0 - 1)).
    """
    fig = go.Figure()

    for ticker, inst in portfolio.instruments.items():

        dates = sorted(inst.prices.keys()) # Ordena as datas cronologicamente
        prices = [inst.prices[d] for d in dates]

        if normalize:
            base = prices[0]
            if base != 0:
                prices = [(p / base - 1) * 100 for p in prices]  # retorno % desde o início

        hover_label = "Preço"
        if normalize:
            hover_label = "Retorno (%)"

        fig.add_trace(
            go.Scatter(
                x=dates,
                y=prices,
                mode="lines",
                name=ticker,
                hovertemplate=(
                    "%{x|%Y-%m-%d}<br>"
                    + f"{ticker}: " 
                    + ("%{y:.2f}%" if normalize else "%{y:.2f}") 
                    + "<extra></extra>")))

    y_title = "Retorno (%)" if normalize else "Preço"

    fig.update_layout(
        title="Séries históricas de preços",
        xaxis_title="Data",
        yaxis_title=y_title,
        legend_title_text="Ativos",
        template="plotly_white",
        height=600,
        width=1000,
        hovermode="x unified")

    return fig



import plotly.graph_objects as go
import numpy as np

def plot_daily_return_series_interactive(portfolio, normalize: bool = False):
    """
    Plota os retornos diários de todos os instrumentos do portfólio.
    Se normalize=True, converte os retornos diários em retorno acumulado (%).
    Caso contrário, mostra o retorno diário (%) diretamente.
    """
    fig = go.Figure()

    for ticker, inst in portfolio.instruments.items():
        # datas ordenadas e retornos (retorno_by_instrument já dá array de retornos simples)
        dates = sorted(inst.prices.keys())
        rets = inst.return_by_instrument()  # array como (P_t / P_{t-1} - 1)
        if len(dates) < 2 or len(rets) == 0:
            continue
        x = dates[1:]  # retornos correspondem a partir da segunda data
        if normalize:
            # retorno acumulado: (1+R).cumprod - 1 em %
            y = (np.cumprod(1 + rets) - 1) * 100
            subtitle = " (acumulado)"
        else:
            y = rets * 100
            subtitle = ""

        fig.add_trace(
            go.Scatter(
                x=x,
                y=y,
                mode="lines",
                name=ticker,
                hovertemplate=(
                    "%{x|%Y-%m-%d}<br>"
                    + f"{ticker}: "
                    + "%{y:.2f}%"
                    + "<extra></extra>")))

    fig.update_layout(
        title=f"Retornos Diários dos Ativos{subtitle}",
        xaxis_title="Data",
        yaxis_title="Retorno (%)",
        legend_title_text="Ativos",
        template="plotly_white",
        height=600,
        width=1000,
        hovermode="x unified")

    return fig



def plot_heatmap_corr(portfolio:Portfolio):
    """
    Plota um gráfico Heatmap das correlações de cada instrumento.
    """
    data = {}
    for ticker, inst in portfolio.instruments.items():
        rets = inst.return_by_instrument()  
        data[ticker] = rets

    df = pd.DataFrame(data)  # columns = tickers

    corr = df.corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        center=0,
        cmap="vlag",
        square=True,
        linewidths=0.5,
        cbar_kws={"label": "Correlação"}
    )
    plt.title("Heatmap da Matriz de Correlação dos Retornos Diários")
    plt.xticks(rotation=90)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()

    return


def plot_decompose_var(pct_contrib:pd.Series):
    """
    Plota um gráfico de barras verticais da contribuição percentual (component VaR) de cada ativo.
    """
    # ordena decrescentemente para maior contribuição primeiro
    pct_sorted = pct_contrib.sort_values(ascending=False)
    tickers = pct_sorted.index.tolist()
    values = pct_sorted.values * 100  # converte para porcentagem
    cmap = plt.get_cmap("tab10")
    colors = [cmap(i % cmap.N) for i in range(len(tickers))]

    fig, ax = plt.subplots(figsize=(8, 4 + 0.2 * len(tickers)))
    x = np.arange(len(tickers))
    bars = ax.bar(x, values, color=colors, edgecolor="black")

    ax.set_xticks(x)
    ax.set_xticklabels(tickers, rotation=45, ha="right")
    ax.set_ylabel("Contribuição para o VaR (%)")
    ax.set_title("Contribuição percentual para o VaR")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.5,
            f"{height:.1f}%",
            ha="center",
            va="bottom",
            fontsize=8,
            )

    plt.tight_layout()
    plt.show()
    return fig