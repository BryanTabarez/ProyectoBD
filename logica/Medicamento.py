class Medicamento():
    """Clase Medicamento"""
    def __init__(self, codigo=0, costo, nombre, descripcion):
        self.__costo = costo
        self.__nombre = nombre
        self.__descripcion = descripcion
