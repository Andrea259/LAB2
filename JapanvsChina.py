#importando las librerias
import pandas as pd
import matplotlib.pyplot as plt


csv = "Big_Japan_vs_China_Technology.csv"
dataframe = pd.read_csv(csv)
year = dataframe["Year"].head() #utilizando head para que aparezcan los primeros cinco datos
star = dataframe["Number of Startups"].head()
print(star)

#creando grafica lineal
x = [166,217,451,264,463]
y = [2001,2011,2009,2019,2002]
plt.plot(x,y,linewidth=3,color="purple")
plt.xlabel("startups")
plt.ylabel("Año")
plt.title("China vs Japan")
plt.show()

#Explicacion
# el dataset nos da una comparación detallada de los avances tecnológicos en China y Japón, 
# abarcando sectores clave como la inteligencia artificial, la robótica, las telecomunicaciones
#  y las energías limpias. y en l grafico visualiamos los campos de año y startups que han tenido


