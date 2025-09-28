"""
    Este programa exibe dois graficos que serao utilizados para
    identificar padroes e insights para melhorar o desempenho.
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from trab3.db import db_connect

SQL_QUERY = 'SELECT * FROM vendas1' # Query SQL que será lida pelo pandas
# Criando um data frame a partir de uma query sql
df_sales = pd.read_sql_query(SQL_QUERY, db_connect())

def graph_plot():
    """ Esta funcao gera um grafico do valor de venda total por categoria """
    # Criando um data frame de categorias e somando os valores de venda
    sales_by_category = df_sales.groupby('categoria')['valor_venda'].sum().reset_index()
    category = sales_by_category['categoria']
    total_sales = sales_by_category['valor_venda']

    plt.style.use("ggplot")

    colors = plt.cm.viridis([0.2, 0.5, 0.8])

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(category, total_sales,
                  color=colors,
                  edgecolor="black",
                  linewidth=1,
                  linestyle='-')

    ax.set_title("Valor de venda total por categorias", fontsize=18, fontweight="bold", pad=15)
    ax.set_ylabel('Valor total de vendas')
    ax.set_xlabel('Categorias')

    ax.grid(axis="y", linestyle="--", alpha=0.7)

    # Exibindo o valor de cada barra no grafico
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 30,
                s=f"R${bar.get_height():,.0f},00",
                ha="center", va="bottom", fontsize=12)

    plt.tight_layout()
    plt.show()


def graph_sea():
    """ Esta funcao gera um grafico do valor de venda por dia """
    sns.set_theme(style='whitegrid')

    plt.figure(figsize=(12, 6))
    ax = sns.lineplot(data=df_sales,
                      x='data_venda',
                      y='valor_venda',
                      marker="o",
                      linewidth=2,
                      color="royalblue")

    ax.set_title("Valor de vendas por Dia", fontsize=18, fontweight="bold", pad=20)
    ax.set_xlabel("Data", fontsize=14)
    ax.set_ylabel("Valor da venda", fontsize=14)

    plt.xticks(rotation=45, ha="right")
    ax.grid(True, linestyle="--", alpha=0.3)
    sns.despine()

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    graph_plot()
    graph_sea()
