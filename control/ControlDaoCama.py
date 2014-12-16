from accesoDatos import DaoCama
from logica import Cama

def mostrarReturn(resultado):
    if resultado is not None:
        print("\nExcepcion capturada! Falta Implementar!!")
        print((resultado.pgerror))

class ControlDaoCama():

    def __init__(self, conexion):
        self.daoCama = DaoCama(conexion)

    def ingresarCama(self, estado, descripcion, cod_area):
        cama = Cama(estado, descripcion, cod_area)
        insertarcama = self.daoCama.guardarCama(cama)
        if insertarcama is 0:
            print "INSERCION EXITOSA!"
        if isinstance(insertarcama, Exception):
            mostrarReturn(insertarcama)