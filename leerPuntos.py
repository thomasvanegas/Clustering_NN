from Punto2D import Punto2D

def leerPuntos(filename: str):
    puntos = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # El formato CSV, está separado por comas (,)
                valores = line.strip().split(',')
                if len(valores) != 2:
                    print("Error: El formato de línea no es válido:", line)
                    continue
                try:
                    x = float(valores[0])
                    y = float(valores[1])
                    puntos.append(Punto2D(x, y))
                except ValueError:
                    print("Error: No se pudo convertir a flotante:", valores)
    except FileNotFoundError:
        print("Error: El archivo no existe.")
    return puntos