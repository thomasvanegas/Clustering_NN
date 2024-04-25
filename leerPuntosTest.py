from leerPuntos import leerPuntos

file_path = './data/datapoints-100.csv'

puntos = leerPuntos(file_path)

for p in puntos:
    print(p)