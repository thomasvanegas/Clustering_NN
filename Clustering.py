#Importacion de librerias, paquetes y clases.
import heapq
from Punto2D import Punto2D
from leerPuntos import leerPuntos

# --- Creacion de los puntos con base en el dataset inicial ---
file_path = './data/datapoints-100.csv'

puntos_list = leerPuntos(file_path)


class Clustering:
    """
        Clase que representa un cluster (Conjunto de puntos cercanos)
    """

    def __init__(self):
        pass

    def clusterizar() -> int:
        num_clusters = 0
        return num_clusters