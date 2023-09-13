import pandas as pd

# Crie um objeto DataFrame para ler o arquivo CSV
df = pd.read_csv('arquivo.csv')

# Mostre as primeiras 5 linhas do DataFrame
print(df.head(5))
print()
# Mostre as 2 últimas linhas
print(df.tail(2))