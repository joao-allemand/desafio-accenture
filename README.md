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

1. Retorno Diário:  $\;\;\; r_t = \frac{P_t}{P_{t-1}} - 1$

2. Retorno Portifólio: $\;\; r_{p,t} = \sum_i w_{i,t-1} \, r_{i,t}
= \sum_i \frac{P_{i,t-1} \, q_i}{V_{p,t-1}} \left( \frac{P_{i,t}}{P_{i,t-1}} - 1 \right)$

3. Volatilidade do instrumento (diária): $\sigma_{i,\text{daily}} =  Std Dev(r_t)$

#### Anualização da Volatilidade

Ao somar \(T\) dias independentes a variância total é:
   $$
   \mathrm{Var}\Bigl(\sum_{t=1}^{T} r_t\Bigr)
   \;=\;
   T \times \sigma^2.
   $$


   $$
   \sigma_{T}
   \;=\;
   \sqrt{\mathrm{Var}(r_1 + \dots + r_T)}
   \;=\;
   \sqrt{T \times \sigma^2}
   \;=\;
   \sqrt{T}\;\sigma.
   $$

Para os 252 dias de pregão.

4. Volatilidade do instrumento (anualizada): 
$\;\; \sigma_{i,\text{anual}} = \sqrt{252} \cdot \sigma_{i,\text{daily}} $


5. Volatilidade do Portifólio (anualizada): $\;\; \sigma_{port,\text{anual}} = \sqrt{252} \cdot  Std Dev(r_{p,t})$

6. Var do instrumento: $\;\;{VaR}_i = z \cdot \sigma_i \cdot A_i$

7. Var do Portfólio: 
$\;\;
\text{VaR}_{\text{portifólio}} = z \cdot \sigma_{port} \cdot V_p
$

8. Marginal Var: 
    $\;\;
\text{mVaR}_i
= z \cdot \sqrt{h} \cdot \frac{(\Sigma \mathbf{w})_i}{\sigma_p} \cdot V_p
$

9. Component Var: 
$\;\;
\text{CompVaR}_i = w_i \cdot \text{mVaR}_i
$

## Como Executar

1. Clonar o repositório.
2. Instalar as bibliotecas utilizadas.

## Referências

[1] J. C. Hull, Risk Management and Financial Institutions, 6th ed. Hoboken, NJ, USA: John Wiley & Sons, 2023.

[2] M. A. P. Cabral, Finanças Matemática, 1th ed., 2020.

[3] D. R. Harper, "What Is Value at Risk (VaR) and How to Calculate It?". Disponível: https://www.investopedia.com/articles/04/092904.asp

