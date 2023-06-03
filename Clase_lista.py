from Clase_nodo import Nodo

class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
    def __iter__(self):
        return self
    def __next__(self):
        self.__tope = 0
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.get_Dato()
            self.__actual = self.__actual.getSiguiente()
            return dato
    def agregar_vehiculo(self, vehiculo):
        '''Agregar un vehiculo a la lista'''
        nodo = Nodo(vehiculo)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
    def insertar_vehiculo(self, vehiculo, posicion):
        '''Insertar un vehiculo en una posicion determinada'''
        if posicion < 0 or posicion > self.__tope:
            raise ValueError("Posicion de insercion no valida")
        nuevo_nodo = Nodo(vehiculo)

        if posicion == 0:
            nuevo_nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nuevo_nodo
        else:
            nodo_anterior = self.__comienzo
            for _ in range(posicion - 1):
                nodo_anterior = nodo_anterior.getSiguiente()
            
            nuevo_nodo.setSiguiente(nodo_anterior.setSiguiente())
            nodo_anterior.getSiguiente(nuevo_nodo)
        self.__tope += 1
    def mostrar_objeto_por_posicion(self, posicion):
        if posicion < 0 or posicion > self.__tope:
            raise ValueError("Posicion de insercion no valida")
        aux = self.__comienzo
        nuevo = Nodo(posicion)
        if posicion is not None:
            print(f"Dato almacenado en la posicion ingresada >>{aux.get_Dato()}")
            nuevo.getSiguiente()
    def listar_datos_coleccion(self):
        '''Lista todos los datos del vehiculos mas economico'''
        aux = self.__comienzo
        while aux is not None:
            if aux.get_Dato().get_precio() < 5000.000:
                print(aux.get_Dato())
                aux = aux.getSiguiente()
    def mostrar_vehiculos_venta(self):
        '''Lista los datos modelo de auto,cantidad de puertas e importe de todos los vehiculos de la concesionaria'''
        aux = self.__comienzo
        while aux is not None:
            print(aux.get_Dato().get_modelo(),aux.get_Dato().get_cantidad_puertas(),aux.get_Dato().get_precio())
            aux = aux.getSiguiente()
    def modificar_por_patente(self, patente):
        '''Busca por patente del vehiculo para modificar el precio base del mismo'''
        aux = self.__comienzo
        encontrado = False
        if aux.get_Dato().get_patente() == patente:
            encontrado = True
            print("Vehiculo encontrado")
            nuevo_precio = input("Ingrese el nuevo precio del vehiculo >> ")
            aux.get_Dato().get_precio(nuevo_precio)
            print("< Precio del vehiculo modificado satisfactoriamente >")
            self.__comienzo = aux.getSiguiente()
            self.__tope -= 1
        else:
            anterior = aux
            aux = aux.getSiguiente()
            while  not encontrado and aux is not None:
                if aux.get_Dato().get_patente() == patente:
                    encontrado = True
                else:
                    anterior = aux
                    aux = aux.getSiguiente()
            if encontrado:
                print("Vehiculo encontrado")
                anterior.setSiguiente(aux.getSiguiente())
                nuevo_precio = input("Ingrese el nuevo precio del vehiculo >> ")
                aux.get_Dato().get_precio(nuevo_precio)
                print("< Precio del vehiculo modificado satisfactoriamente >")
                self.__comienzo = aux.getSiguiente()
                self.__tope -= 1
            else:
                print(f"La patente {patente} no esta en la lista")
    def cartel(self):
        print("Archivo json registrado : )")