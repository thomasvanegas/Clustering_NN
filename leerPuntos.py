#Importacion de librerias, paquetes y clases.
from Punto2D import Punto2D
import csv

def leerPuntos(filename: str) -> list:
    """
        Lee los puntos de un archivo CSV y los almacena en una lista de objetos de la clase Punto2D.

    Args:
        filename: La ruta del archivo CSV.

    Returns:
        una lista de instacias de la clase Punto2D.
    """
    puntos_list = []

    try:
        with open(filename, 'r') as csvfile:
            # reader = csv.reader(file)
            for line in csvfile:
                # Separando los valores por coma y convertirlos a flotantes
                x, y = map(float, line.strip().split(','))
                # Creando una instancia de Punto2D y agregarla a puntos_list
                puntos_list.append(Punto2D(x, y))
    except FileNotFoundError:
        print(f"El archivo {filename} no existe.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return puntos_list
