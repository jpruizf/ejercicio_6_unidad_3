from Clase_Vehiculo import Vehiculo

class Vehiculo_nuevo(Vehiculo):
    __precio_base: float
    __kilometraje: float
    def __init__(self, kilometraje):
        super().__init__()
        self.__kilometraje = kilometraje
        self.__precio_base = 0.0
    def get_precio(self,nuevo):
        '''Modifico precio si nuevo es mayor a 0'''
        if nuevo > 0:
            self.__precio_base = nuevo
        else:
            return self.__precio_base
    def get_kilometraje(self):
        return self.__kilometraje