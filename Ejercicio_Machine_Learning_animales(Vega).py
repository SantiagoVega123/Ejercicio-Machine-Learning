import pandas as pd
datos = pd.read_csv('../input/animales/animales (1).csv')
datos

df1 = pd.DataFrame(datos)
df1

caracteristicas = [[7,0.6,40],[7,0.6,41],[37,0.8,37],[37,0.8,38]]

etiquetas = [0,0,1,1]

from sklearn import tree

clasificador = tree.DecisionTreeClassifier()

clasificador.fit(caracteristicas,etiquetas)

altura = int(input("ingresar altura: "))
peso = float(input("ingresar peso: "))
temperatura = int(input("ingresar temperatura: "))
​
prediccion = clasificador.predict([[altura,peso,temperatura]])
if (prediccion == 0):
    print("los datos ingresados corresponden a un gato")
else:
    print("los datos ingresados corresponden a un perro")
