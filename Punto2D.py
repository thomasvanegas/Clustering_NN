#Importacion de librerias, paquetes y clases.
import math

class Punto2D:

    """
        Clase que representa puntos en el plano XY (Cartesiano)
    """
    def __init__(self, x:float, y:float):
        """
            Constructs a Point2D instance from the x,y coordinates
        """
        self._x = x
        self._y = y


    def __str__(self):
        """
            Returns a String representation of the point2D
        """
        return f'({self.getX()},{self.getY()})'

    def getDistance(self, other:'Punto2D') -> float:
        """
            Computes the distance to other Point2D
        """
        return math.sqrt( (self.getX()-other.getX())**2 + (self.getY()-other.getY())**2 )
    
    def getAngle(self) -> float:
        """
            Returns the angle to the x axis
        """
        return math.atan2( self._y, self._x )

    def __abs__(self):
        """
            Returns the distance to the origin (magnitude)
        """
        return math.sqrt( self._x**2 + self._y**2 )

    def getX(self) -> float:
        """
            Returns the x component
        """
        return self._x

    def getY(self) -> float:
        """
            Returns the y component
        """
        return self._y
    
    def __eq__(self, other:'Punto2D') -> bool:
        """
            Equality between instances of Point2D
            Returns True if the points are the same
        """
        if other is None:
            return False
        if not(isinstance(other,Point2D)):
            return False
        if self.distance(other)<1E-12:
            return True
        return False