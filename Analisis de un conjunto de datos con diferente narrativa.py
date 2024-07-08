from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Ejercicio 1
#Seleccion de datos
#Dos graficos con narrativa diferente tratando el mismo conjunto de datos.

df= pd.read_csv("Social_Network_Ads.csv") # Solo por si el archivo se arrastra a los archivos del colab
# df = pd.read_csv("/content/drive/MyDrive/Social_Network_Ads.csv")
print(df)

# Diccionario de mapeo para reemplazar los valores
mapeo = {1: 'Sí', 0: 'No'}

# Aplicar el reemplazo a la columna 'purchased'
df['Purchased'] = df['Purchased'].replace(mapeo)

print(df)

genero = df["Gender"]
salario = df["EstimatedSalary"]
edad= df['Age']
comprado=df['Purchased']
sns.scatterplot(x=edad, y=salario, hue=comprado, data=df)


pltTitle1 = "Relacion entre el salario estimado y las edades en la compra de un producto"
pltTitle2 = "Relacion entre el salario estimado (Mayor a 80000) y las edades en la compra de un producto"
xlabel1 = "Edades"
ylabel1 = "Salario estimado"
legendTitle1 = "Compraron producto"

plt.title(pltTitle1, fontsize=14)
plt.xlabel(xlabel1)
plt.ylabel(ylabel1)
plt.legend(title= legendTitle1)


etiquetas_personalizadas = ['Mujeres', 'Hombres']

df_1 = df.loc[df['Purchased'] == 'Sí']
compras_por_genero = df_1["Gender"].value_counts()
# plt.pie(compras_por_genero, labels=compras_por_genero.index, autopct="%1.1f%%")
plt.pie(compras_por_genero, labels=etiquetas_personalizadas, autopct="%1.1f%%")
plt.title("Compras por Género")
plt.show()

#Ejercicio 2
#Manipulación de escalas
#Manipular las escalas de las graficas para dar diferentes conclusiones


genero = df["Gender"]
salario = df["EstimatedSalary"]
edad= df['Age']
comprado=df['Purchased']
sns.scatterplot(x=edad, y=salario, hue=comprado, data=df)
#Real- los viejitos compran el producto, los chavos no


plt.title(pltTitle1, fontsize=14)
plt.xlabel(xlabel1)
plt.ylabel(ylabel1)
plt.legend(title= legendTitle1)

df_40 = df.loc[df['EstimatedSalary'] >= 80000]
genero1 = df_40["Gender"]
salario1 = df_40["EstimatedSalary"]
edad1= df_40['Age']
comprado1=df_40['Purchased']

sns.scatterplot(x=edad1, y=salario1, hue=comprado1, data=df)
#El producto no es para gente pobreXD


plt.title(pltTitle1, fontsize=14)
plt.xlabel(xlabel1)
plt.ylabel(ylabel1)
plt.legend(title= legendTitle1)
plt.show()


#Con un mejor título se entiende mejor el gráfico, de lo contrario se pueden confundir el porposito de las gráficas

sns.scatterplot(x=edad1, y=salario1, hue=comprado1, data=df)

plt.title(pltTitle2, fontsize=14)
plt.xlabel(xlabel1)
plt.ylabel(ylabel1)
plt.legend(title= legendTitle1)
plt.show()

#Ejercicio 3
#Uso de colores
#Modificar los colores para influir en la interpretación emocional

# Gráfico sin colores
sns.scatterplot(x=edad, y=salario, hue=comprado, data=df)

plt.title(pltTitle1, fontsize=14)
plt.xlabel(xlabel1)
plt.ylabel(ylabel1)
plt.legend(title= legendTitle1)

plt.show()



# Gráfico con colores más comprensibles

custom_palette = {"Sí": 'blue', "No": 'red'}
sns.scatterplot(x=edad, y=salario, hue=comprado,  data=df, palette=custom_palette)

plt.title(pltTitle1, fontsize=14)
plt.xlabel(xlabel1)
plt.ylabel(ylabel1)
plt.legend(title= legendTitle1)

plt.show()

# gráfico sin color
etiquetas_personalizadas = ['Mujeres', 'Hombres']

df_1 = df.loc[df['Purchased'] == 'Sí']
compras_por_genero = df_1["Gender"].value_counts()
# plt.pie(compras_por_genero, labels=compras_por_genero.index, autopct="%1.1f%%")
plt.pie(compras_por_genero, labels=etiquetas_personalizadas, autopct="%1.1f%%")
plt.title("Compras por Género")
plt.show()

# gráfico con color
etiquetas_personalizadas = ['Mujeres', 'Hombres']

colores = ['pink', 'lightblue']

df_1 = df.loc[df['Purchased'] == 'Sí']
compras_por_genero = df_1["Gender"].value_counts()
plt.pie(compras_por_genero, labels=etiquetas_personalizadas, autopct="%1.1f%%", colors=colores)
plt.title("Compras por Género")






plt.show()
# Gráfico sin colores

sns.scatterplot(x=edad1, y=salario1, hue=comprado1, data=df)


plt.title(pltTitle2, fontsize=14)
plt.xlabel(xlabel1)
plt.ylabel(ylabel1)
plt.legend(title= legendTitle1)
plt.show()

# Gráfico con colores

custom_palette = {"Sí": 'blue', "No": 'red'}

sns.scatterplot(x=edad1, y=salario1, hue=comprado1, data=df, palette=custom_palette)


plt.title(pltTitle2, fontsize=14)
plt.xlabel(xlabel1)
plt.ylabel(ylabel1)
plt.legend(title= legendTitle1)
plt.show()



