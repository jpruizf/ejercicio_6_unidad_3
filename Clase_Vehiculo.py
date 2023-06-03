
class Vehiculo:
    __patente: str
    __anio: int
    __marca: str
    __color: str
    __cantidad_puertas: int
    __modelo: str
    __patente: str
    def __init__(self):
        self.__patente = ""
        self.__anio = 0
        self.__marca = ""
        self.__color = ""
        self. __cantidad_puertas = 0
        self.__modelo = ""
    def get_patente(self):
        return self.__patente
    def get_anio(self):
        return self.__anio
    def get_marca(self):
        return self.__marca
    def get_color(self):
        return self.__color
    def get_cantidad_puertas(self):
        return self.__cantidad_puertas
    def get_modelo(self):
        return self.__modelo