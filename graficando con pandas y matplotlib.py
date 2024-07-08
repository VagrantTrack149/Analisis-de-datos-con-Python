import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

iris_df = sns.load_dataset("iris")

print(iris_df.head())

print(iris_df.describe())

especie_unica = iris_df["species"].unique()

print(f"Cantidad de especies únicas: {especie_unica}")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for i, col in enumerate(iris_df.columns[:3]):
    sns.histplot(data=iris_df, x=col, ax=axes[i], kde=True)
    axes[i].set_title(col)

plt.show()

titanic_df = sns.load_dataset("titanic")

print(titanic_df)

print(titanic_df.isnull().sum())

proporcion_faltantes = titanic_df.isnull().mean()*100

print(proporcion_faltantes)

titanic_df = titanic_df.dropna()
print(titanic_df)


titanic_df.describe()

sns.histplot(data=titanic_df, x="age", kde=True)
plt.show()

sns.boxplot(x=titanic_df['sibsp'])
plt.show()

def g(titanic_df):
    titanic_df['sibsp'] = np.where(titanic_df['sibsp'] > 2, titanic_df['sibsp'].mean(), titanic_df['sibsp'])
    return titanic_df

titanic_df = g(titanic_df.copy())

sns.boxplot(x=titanic_df['sibsp'])
plt.show()

sns.boxplot(x=titanic_df['parch'])
plt.show()

def g(titanic_df):
    titanic_df['parch'] = np.where(titanic_df['parch'] > 1, titanic_df['parch'].mean(), titanic_df['parch'])
    return titanic_df

titanic_df = g(titanic_df.copy())

sns.boxplot(x=titanic_df['parch'])
plt.show()


sns.boxplot(x=titanic_df['fare'])
plt.show()

def g(titanic_df):
    titanic_df['fare'] = np.where(titanic_df['fare'] > 150, titanic_df['fare'].mean(), titanic_df['fare'])
    return titanic_df

titanic_df = g(titanic_df.copy())

sns.boxplot(x=titanic_df['fare'])
plt.show()


tips_df = sns.load_dataset("tips")
print(tips_df)

corr = tips_df.set_index('alpha_3').corr()

sns.heatmap(corr, annot=True,)
plt.title("Matriz de correlación")
plt.show()

#Grafico de dispersion
fig, ax= plt.subplots()
colors={"Sun":"blue", "Fri":"red","Sat":"green", "Thur":"purple"}
tipo=tips_df.day.map(colors)

ax.scatter(tips_df.tip,tips_df.total_bill,color=tipo)

propinas_dia = tips_df.groupby("day")["tip"].mean()
sns.barplot(x=propinas_dia.index, y=propinas_dia)
plt.title("Propina por día de la semana")
plt.show()

