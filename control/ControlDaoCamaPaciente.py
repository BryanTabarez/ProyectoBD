from accesoDatos import DaoCamaPaciente
from accesoDatos import DaoCama
from logica import Cama
from logica import Paciente

class ControlDaoCamaPaciente():

    def __init__(self, conexion):
        self.daoCamaPaciente = DaoCamaPaciente(conexion)
        self.daoCama = DaoCama( conexion )

    def ingresarCamaPaciente(self, num_cama, id_paciente, fecha):
        
        asignar_cama = self.daoCamaPaciente.guardarCamaPaciente( num_cama, id_paciente, fecha)
        
        cambio_estado_cama = self.daoCama.modificarEstadoCama( num_cama , False )

        return ( asignar_cama , cambio_estado_cama )

    def liberarCama(self, num_cama ):

        cambio_estado_cama = self.daoCama.modificarEstadoCama( num_cama , True )

        return cambio_estado_cama


    def consultarCamaPaciente(self, id):
        cama = self.daoCamaPaciente.consultarCamaPaciente(id)
        return cama
