#Script for calculating daily cases and deaths of Influenza in the US 2019-20

import pandas as pd, os, matplotlib.pyplot as plt, plotly.express as px

#Weekly laboratory confirmed cases from CDC 2019-20 (n=26 weeks)
df = pd.read_csv('/Volumes/GoogleDrive/My Drive/coding/python/fight-club/covid19/FluView_StackedColumnChart_Data.csv')
basic_df = df[['YEAR', 'WEEK', 'TOTAL SPECIMENS']]

#Smallest number of total estimated cases/laboratory confirmed cases per week
ratio = 39000000/basic_df['TOTAL SPECIMENS'].sum()

corrected_df = basic_df
corrected_df['ESTIMATED CASES'] = basic_df['TOTAL SPECIMENS']*ratio
corrected_df['ESTIMATED DEATHS'] = corrected_df['ESTIMATED CASES']*(0.1/100)
values = [number for number in range(27)]
corrected_df['WEEK'] = values[1:]

#PLOT
fig = px.line(corrected_df, x='WEEK', y='ESTIMATED DEATHS', title='Mortes Estimadas por Influenza nos EUA')
fig.show()

#DEBUGGER
#print(corrected_df.head())
#print(corrected_df.describe())
#print(corrected_df['ESTIMATED CASES'].sum())
#print(corrected_df['ESTIMATED DEATHS'].sum())

