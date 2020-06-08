#Script to generate plot for budget data

import pandas as pd, numpy as np, plotly.express as px

df = pd.read_excel(r'/Users/joaopedropadua/Dropbox/Textos Padua/covid ciencia brasil/orcamento_universidades.xlsx')
graph_df = df[['Universidade', 'Valor per capita (em US$ dólares)']]
graph_df_rounded = graph_df.round(3)

#Plot
fig = px.bar(graph_df_rounded, x='Universidade', y='Valor per capita (em US$ dólares)', title='Gastos em Universidades com alunos (2018)')
fig.show()


#DEBUGGER:
#print(df.head())
#print(graph_df_rounded.head())