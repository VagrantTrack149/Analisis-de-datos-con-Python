import matplotlib.pyplot as plt

conjunto1 =[0,2,4,8,16,32,64]
conjunto2 =[0,0.5,1.0,1.5,2.0,2.5,3.0]

plt.plot(conjunto1,conjunto2, label='caso 1', linestyle='dotted',color='green')
plt.plot([0,64],[0,3],label='caso 2', linestyle='dashed', color='orange')
plt.legend()
plt.title('Grafica de muestra')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

#Grafico de dispersion
import numpy as np
N=100
X1=np.random.rand(N)
Y1=np.random.rand(N)
X2=np.random.rand(N)
Y2=np.random.rand(N)
plt.scatter(X1,Y1, color='blue',alpha=0.5,label='Puntos de dispersión azules')
plt.scatter(X2,Y2, color='pink',alpha=0.7,label='Puntos de dispersión rosas')
plt.legend(loc='best')
plt.grid(True)
plt.show()

#Grafico de barras
meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio']
Ganancias=[13,35,32,45,23,98,65]
fig, ax = plt.subplots()
ax.bar(x = meses, height = Ganancias)
plt.title('Ganancias por meses')
plt.xlabel('Meses')
plt.ylabel('Ganancias (Miles)')
plt.show()
plt.bar(meses,Ganancias)
plt.show()

#Grafica de pastel
manzanas = [20,10,25,30]
nombres = ["Ana","Juan","Diana","Catalina"]
colors = ["#fff6d5", "#5b3a29", "#d53032", "#ca987f"]
plt.figure(figsize=(8,6))
plt.pie(manzanas, labels=nombres,colors=colors,autopct="%0.1f %%")
plt.show()

#Graficos con el dataset "tips"
#Grafico de dispersion relacion total cuenta - propina
import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset('tips')

plt.figure(figsize=(10,8))
sns.lmplot(data=tips,x='total_bill',y='tip', hue='time',legend=0)
plt.title('Relacion entre total de la cuenta y la propina')
plt.xlabel('Total de la cuenta')
plt.ylabel('Propina')
plt.legend(title='Momento del dia')
plt.show()

#Grafico de histograma: mostrar las distribuciones de los totales de las cuentas
plt.figure(figsize=(10,8))
sns.histplot(tips['total_bill'],bins=20,kde=True,color='lightblue')
plt.title('Distribución total de la cuenta')
plt.xlabel('Total de la cuenta')
plt.ylabel('Frecuencia')
plt.show()

#Ejercicio 1
#Cargar penguins
#Describe
#Dispersion longitud pico y profundidad pico
#histograma longitud aleta por especie
#boxplot comparar peso corporal

penguins=sns.load_dataset('penguins')
sns.load_dataset('penguins')

penguins.describe()

plt.figure(figsize=(10,8))
sns.lmplot(data=penguins,x='bill_depth_mm',y='bill_length_mm',hue='species',legend=0)
plt.xlabel('Profundidad')
plt.ylabel('Longitud')
plt.title('Relación entre la profundidad y la longitud del pico de los pinguinos')
plt.legend()
plt.show()
#¿Hay alguna relación aparente entre la longitud y la profundidad del pico de los pinguinos?
#Si, en la especie Gentoo es muy poco profunda pero más largo.
#Para la chinstrap es casi lineal la relación
#Y para Adelie, tiene mucha profundidad y muy corta longitud

plt.figure(figsize=(10, 6))
sns.histplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack", palette="Set1")
plt.title("Histograma de la longitud de la aleta")
plt.xlabel('Longitud')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

sns.boxplot(data=penguins, x='species', y="body_mass_g", hue="species", palette="Set1")
plt.xlabel('Especies')
plt.ylabel('Peso en gramos')
plt.title('Comparar peso corporal por especies')
plt.show()
#¿Como varian las caracteristicas fisicas de los pinguinos entre las diferentes especies?
#Adelie y Chinstrap son bastante similares en su peso
#Pero Gentoo son más pesados
#Los pinguinos entre más masa corporal tienen entonces la longitud de sus aletas es mayor



#Ejercicio 2
#Cargar flights
#Describe
#Lineas pasajeros y años
#Heatmap pasajeros por mes a lo largo de los años

sns.load_dataset('flights')


fly=sns.load_dataset('flights')
fly.describe()

import pandas as pd
pasajeros_anio=fly.groupby("year")["passengers"].sum()

df_lineas=pd.DataFrame({"anio":pasajeros_anio.index,"total_pasajeros":pasajeros_anio.values})
sns.lmplot(data=df_lineas,x="anio",y="total_pasajeros")

plt.title('Relación entre año y pasajeros')
plt.xlabel('Años')
plt.ylabel('Suma de pasajeros')
plt.grid(True)
plt.show()
#¿Hay alguna tendencia clara a lo largo de los años?
#Si, existe un incremento lineal


glue = sns.load_dataset("flights").pivot(index="year", columns="month", values="passengers")
sns.heatmap(glue)
plt.xlabel('Año')
plt.ylabel('Mes')
plt.title('Mapa de calor pasajeros por mes y año')
plt.show()
#¿Puedes identificar patrones estacionales en el numero de pasajeros?
#Si, se puede decir que en verano (Junio y Julio) hay un mayor numero de pasajeros
