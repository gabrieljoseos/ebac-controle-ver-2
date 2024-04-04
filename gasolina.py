import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# código de geração do gráfico
gasolina_df = pd.read_csv("gasolina.csv")
gasolina = sns.lineplot(data=gasolina_df, x="dia", y="venda", color='red')
gasolina.set(title="Valor da Gasolina em reais durante 10 dias", xlabel="Dias", ylabel="Valor(R$)")

#salvar o grafico como png
gasolina_fig = gasolina.get_figure()
gasolina_fig.savefig('gasolina.png')
