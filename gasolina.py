import seaborn as sns
import pandas as pd

csv = pd.read_csv('gasolina.csv')

with sns.axes_style('darkgrid'):
  grafico = sns.lineplot(data = csv, x='dia', y='venda')
  grafico.set(title='Preço médio por dia da gasolina em São Paulo (jul/21)', xlabel = 'Dia', ylabel = 'Preço (R$)')

grafico.figure.savefig("./gasolina.png")