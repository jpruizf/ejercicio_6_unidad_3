from Clase_Vehiculo import Vehiculo

class Vehiculo_usado(Vehiculo):
    __kilometraje:float
    __precio_unitario: float
    def __init__(self, kilometraje):
        super().__init__()
        self.__kilometraje = kilometraje
        self.__precio_unitario = 0.0
    def __getKilometraje__(self):
        return self.__kilometraje
    def __get_precio_unitario__(self):
        return self.__precio_unitario