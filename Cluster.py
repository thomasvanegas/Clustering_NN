#Importacion de librerias, paquetes y clases.
from Punto2D import Punto2D

class Cluster:
    def __init__(self, punto: 'Punto2D'):
        """
            Contructor: Inicialmente cada punto del dataset es un cluster de un elemento
        
            argument: punto2D
        """
        if isinstance(punto, Punto2D):
            self._elementos = [punto]
        else:
            return 'Error al inicializar el cluster... el argumento no es una instancia de la clase Punto2D'
        self._centro = punto

    def size() -> int:
        return len(self._elementos)