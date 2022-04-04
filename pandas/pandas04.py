import pandas as pd

copacabana = pd.read_csv('./pandas/data/copacabana.csv', delimiter=';')


print(copacabana.columns)

print(copacabana['Quartos'].describe())
print(copacabana.loc[copacabana['Quartos'] == 6])

copacabana['TOTAL'] = copacabana['AreaConstruida'] * copacabana['VAL_UNIT']
print(copacabana['TOTAL'])

# populacao = pd.read_excel('./pandas/data/total_populacao_pernambuco.xls')

# print(populacao)