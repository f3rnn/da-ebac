import seaborn as sns
import pandas as pd

csv = pd.read_csv('gasolina.csv')

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data = csv, x='dia', y='venda')
  grafico.set(title='Preço médio por dia da gasolina em São Paulo', xlabel = 'Dias', ylabel = 'Preço em reais')

grafico.figure.savefig("./gasolina.png")