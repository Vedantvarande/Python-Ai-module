import pandas as pd
import csv
df = pd.read_csv('Total Stars.csv')
del df['Luminosity']
del df['Star_name']
del df['Distance']
del df['Mass']
del df['Radius']
df.to_csv('Final.csv')