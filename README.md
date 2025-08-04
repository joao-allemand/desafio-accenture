# Análise de Risco de Portfólio com VaR Explodido

## Objetivo do Projeto

O objetivo deste projeto é calcular o **Value at Risk (VaR)** de uma carteira de ativos de forma paramétrica, oferecer visualizações interativas das séries de preço, retornos e correlações entre os ativos, para assim poder utilizar como ferramenta para uma análise de risco.  
Entre os resultados estão:
- Retornos diários por ativo e da carteira;
- Volatilidade histórica (anualizada);
- VaR total da carteira em um horizonte definido;
- Component VaR (decomposição do risco);
- Matriz de correlação dos retornos e heatmap;
- Gráficos de preços e retornos acumulados/diários.

## Bibliotecas Usadas

- **Python** – linguagem.
- **NumPy** – manipulação numérica e álgebra linear.  
- **Pandas** – organização de séries temporais e cálculo de covariâncias/correlações.  
- **SciPy** – para obter o z-score da distribuição normal (nível de confiança).  
- **Plotly** – gráficos interativos (séries de preço e retorno).  
- **Seaborn / Matplotlib** – visualização da matriz de correlação (heatmap) e VaR explodido (barras).  
- **yfinance** – para baixar dados históricos de ativos (ex.: tickers `.SA` da B3).  

## Estrutura do Código

Projeto separado em arquivos, onde:
- **objects.py** - contém as classes e métodos implementados.
- **utils.py** - contém as funções pro funcionamento do código.
- **graphs.py** - contém as funções de criação de gráficos.
- **apresentacao.ipynb** - contém a apresentação do projeto, onde serão plotados os gráficos e apresentados os índices.
- **Testes.ipynb** - arquivo de testes, pode ser ignorado.

## Fórmulas


| Símbolo | Definição |
|--------|-----------|
| $r_t$ | Retorno simples do ativo entre os dias $t-1$ e $t$: $r_t = \dfrac{P_t}{P_{t-1}} - 1$. |
| $P_t$ | Preço do ativo no tempo $t$ (fechamento ajustado). |
| $r_{p,t}$ | Retorno da carteira no tempo $t$: $r_{p,t} = \sum_i w_{i,t-1} r_{i,t} = \sum_i \dfrac{P_{i,t-1} q_i}{V_{p,t-1}} \left( \dfrac{P_{i,t}}{P_{i,t-1}} - 1 \right)$. |
| $w_{i,t-1}$ | Peso do ativo $i$ no dia $t-1$: $w_{i,t-1} = \dfrac{P_{i,t-1} q_i}{V_{p,t-1}}$. |
| $q_i$ | Quantidade do ativo $i$ detida. |
| $V_{p,t-1}$ | Valor da carteira no tempo $t-1$: $V_{p,t-1} = \sum_j P_{j,t-1} q_j$. |
| $\sigma_{i,\text{daily}}$ | Volatilidade diária do ativo $i$: $\sqrt{\mathrm{Var}(r_{i,t})}$. |
| $T$ | Número de dias agregados. |
| $\sigma$ | Volatilidade de um período sob independência. |
| $\sigma_T$ | Volatilidade em $T$ dias: $\sqrt{T}\,\sigma$. |
| $\sigma_{i,\text{anual}}$ | Volatilidade anualizada do ativo $i$: $\sqrt{252}\,\sigma_{i,\text{daily}}$. |
| $\sigma_{port,\text{anual}}$ | Volatilidade anualizada da carteira: $\sqrt{252}\,\mathrm{StdDev}(r_{p,t})$. |
| $\alpha$ | Nível de confiança para o VaR. |
| $z$ | Quantil da normal padrão: $z = \Phi^{-1}(\alpha)$. |
| $A_i$ | Valor investido no ativo $i$: $q_i \cdot P_{i,\text{último}}$. |
| $\mathrm{VaR}_i$ | VaR do ativo $i$: $z \cdot \sigma_i \cdot A_i$. |
| $\mathrm{VaR}_{\text{portfólio}}$ | VaR da carteira: $z \cdot \sigma_{\text{port}} \cdot V_p$. |
| $h$ | Horizonte em dias úteis. |
| $\Sigma$ | Matriz de covariância dos retornos diários. |
| $\mathbf{w}$ | Vetor de pesos da carteira. |
| $(\Sigma \mathbf{w})_i$ | Entrada $i$ de $\Sigma \mathbf{w}$. |
| $\sigma_p$ | Volatilidade diária da carteira: $\sqrt{\mathbf{w}^\top \Sigma \mathbf{w}}$. |
| $\mathrm{mVaR}_i$ | Marginal VaR: $z \sqrt{h} \cdot \dfrac{(\Sigma \mathbf{w})_i}{\sigma_p} \cdot V_p$. |
| $\mathrm{CompVaR}_i$ | Component VaR: $w_i \cdot \mathrm{mVaR}_i$. |




## Como Executar

1. Clonar o repositório.
2. Instalar as bibliotecas utilizadas.

## Referências

[1] J. C. Hull, Risk Management and Financial Institutions, 6th ed. Hoboken, NJ, USA: John Wiley & Sons, 2023.

[2] M. A. P. Cabral, Finanças Matemática, 1th ed., 2020.

[3] D. R. Harper, "What Is Value at Risk (VaR) and How to Calculate It?". Disponível: https://www.investopedia.com/articles/04/092904.asp

