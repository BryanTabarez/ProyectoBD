from accesoDatos import DaoCama
from logica import Cama

class ControlDaoCama():

    def __init__(self, conexion):
        self.daoCama = DaoCama(conexion)

    #Pendiente de modificacion (Bryan)
    def ingresarCama(self, estado, descripcion, cod_area):
        cama = Cama(estado, descripcion, cod_area)
        insertarcama = self.daoCama.guardarCama(cama)
        if insertarcama is 0:
            print "INSERCION EXITOSA!"
        if isinstance(insertarcama, Exception):
            mostrarReturn(insertarcama)


    def listarCamas(self, estado):

        camas = self.daoCama.listarCamas(estado)
        return camas