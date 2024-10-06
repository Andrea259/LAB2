#importando las librerias
import pandas as pd
import matplotlib.pyplot as plt


csv = "gym_members_exercise_tracking.csv"
dataframe = pd.read_csv(csv)
Age = dataframe["Age"].value_counts().head() #utilizando head para que aparezcan los primeros cinco datos
print(Age)

#crear grafico de barras con los datos del dataset de gym
op=["43 años", "50 años", "52 años", "45 años", "54 años"]
fre=[34,33,32,30,30]
colores=["pink","blue", "brown","purple"]
plt.bar(op,fre,color=colores,linewidth=3)
plt.title("Edades")
plt.show()

#Explicacion
#En el siguiente grafico se puede visualizar las edades de las personas que asisten al gym 
# y la cantidad de personas que tienen esa edad.