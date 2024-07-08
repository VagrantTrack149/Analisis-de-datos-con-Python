import pandas as pd
import seaborn as sns
import numpy as np
sns.get_dataset_names()

sns.load_dataset('planets')

DS_prueba=sns.load_dataset('planets')

resultado = []

for value in DS_prueba['mass']:
  if np.isnan(value):
    resultado.append(False)
  else:
    resultado.append(True)

true_count = 0
false_count = 0

for value in resultado:
  if value:
    true_count += 1
  else:
    false_count += 1

print("True:", true_count)
print("False:", false_count)

DS_prueba=sns.load_dataset('planets')
DS_prueba.notnull()


df_filtrado = DS_prueba.loc[DS_prueba.isnull().any(axis=1)]

print(df_filtrado)

DS_prueba=sns.load_dataset('planets')

sns.load_dataset('planets')

DS_prueba.dropna()

DS_prueba=sns.load_dataset('planets')

DS_prueba['mass'].fillna('UnKnown',inplace=True)
print(DS_prueba)



DS_prueba=sns.load_dataset('planets')

DS_prueba['mass'].fillna(method="bfill",inplace=True)
print(DS_prueba)

