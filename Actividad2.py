import pandas as pd
import numpy as np
df= pd.read_csv("C:\Users\Ruben Rubio\OneDrive\Escritorio\VS Code Sem tec\titanic (1).csv")
print(df.head())
print(df.columns)
print(df.describe())
print(df.info())
print(df.isnull().sum())
# Reporte de Dataset
## El dataset del titanic contiene informacion de los pasajeros del titanic, con un total de 891 filas y 12 columnas, representando valores nulos en la columna Age con 177 valores nulos, Cabin con 687 valores nulos y Embarked con 2 valores, analizando los rangos que se encuentran cada variable numerica, se observa que la variable Age tiene un rango de 0.42 a 80, indicando que hay pasajeros de todas las edades, la variable Fare tiene un rango de 0 a 512.3292, indicando que hay una gran variabilidad en los precios de los boletos, las variables Pclass y SibSp tienen valores entre 1 y 3 y 0 y 8 respectivamente, indicando que hay una gran variedad en las clases y en el numero de hermanos o esposos a bordo, la variable Parch tiene valores entre 0 y 6, indicando que hay una gran variedad en el numero de padres o hijos a bordo. Para concluir después de este analisis inicial, se puede decir que el dataset de titanic es un dataset interesante para analizar, ya que contiene una gran variedad de variables y valores, pero requiere una limpieza previa debido a la presencia de valores nulos.
