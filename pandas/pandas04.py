import pandas as pd

copacabana = pd.read_csv('./pandas/data/copacabana.csv', delimiter=';')


print(copacabana)

populacao = pd.read_excel('./pandas/data/total_populacao_pernambuco.xls')

print(populacao)