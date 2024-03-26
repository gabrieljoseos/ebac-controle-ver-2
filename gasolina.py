import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv("gasolina.csv")

gasolina_df.head(10)

gasolina = sns.lineplot(data=gasolina_df, x="dia", y="venda", color='blue')
gasolina.set(title="Valor da Gasolina durante 10 dias", xlabel="Dia", ylabel="Valor")

gasolina_fig = gasolina.get_figure()
gasolina_fig.savefig('gasolina.png')
