import pandas as pd

df = pd.read_csv('data/exemplo.csv')

df_filtrado = df[df['estado'] == 'SP']

df_filtrado = df[df['preço'] == '10,50']

print(df_filtrado)