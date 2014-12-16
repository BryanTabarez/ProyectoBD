from accesoDatos import DaoMedico
from logica import Medico


def mostrarReturn(resultado):
    if resultado is not None:
        print("\nExcepcion capturada! Falta Implementar!!")
        print((resultado.pgerror))


class ControlDaoMedico():

    def __init__(self, conexion):
        self.daoMedico = DaoMedico(conexion)

    def insertarMedico(self, identificacion, nombre, direccion, telefono,
    codigo_area, email, salario, id_jefe, especialidad, universidad,
    num_licencia):
        medico = Medico(identificacion, nombre, direccion, telefono,
        codigo_area, email, salario, id_jefe, especialidad, universidad,
        num_licencia)
        insertarMedico = self.daoMedico.guardarMedico(medico)
        if insertarMedico is 0:
            print "INSERCION EXITOSA!"
        if isinstance(insertarMedico, Exception):
            mostrarReturn(insertarMedico)

    def consultarMedico(self, id):
        consultarmedico = self.daoMedico.consultarMedico(id)
        if isinstance(consultarmedico, Exception):
            mostrarReturn(consultarmedico)
        return consultarmedico

    def modificarMedico(self, id, nombre, direccion, telefono,
        codigo_area, email, salario, id_jefe, especialidad, universidad,
        num_licencia):
        medico = Medico(id, nombre, direccion, telefono,
        codigo_area, email, salario, id_jefe, especialidad, universidad,
        num_licencia)
        modificarmedico = self.daoMedico.modificarMedico(id, medico)
        if modificarmedico is 0:
            print "Modificacion Exitosa!!"
        if isinstance(modificarmedico, Exception):
            mostrarReturn(modificarmedico)

    def borrarMedico(self, id):
        borrarmedico = self.daoMedico.borrarMedico(id)
        if borrarmedico is 0:
            print "Se Elimino Satisfactoriamente!!"
        if isinstance(borrarmedico, Exception):
            mostrarReturn(borrarmedico)

