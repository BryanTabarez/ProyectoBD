from accesoDatos import DaoMedicamento
from logica import Medicamento


class ControlDaoMedicamento():

    def __init__(self, conexion):
        self.daoMedicamento = DaoMedicamento(conexion)

    def insertarMedicamento(self, costo, nombre, descripcion):
        medicamento = Medicamento(costo, nombre, descripcion)
        insertar = self.daoMedicamento.guardarMedicamento(medicamento)
        if insertar is 0:
            return "Se ha ingresado satisfactoriamente"
        if isinstance(insertar, Exception):
            return insertar.pgerror

    def buscarMedicamento(self, nombre):
        buscar = self.daoMedicamento.consultarMedicamento(nombre)
        if buscar is 1:
            return "La consulta no arrojo resultados"
        else:
            return buscar
        if isinstance(buscar, Exception):
            return buscar.pgerror

    def actualizarMedicamento(self, codigo, costo, nombre, descripcion):
        medicamento = Medicamento(codigo, costo, nombre, descripcion)
        actualizar = self.daoMedicamento.modificarMedicamento(medicamento)
        if actualizar is 0:
            return "Se ha modificado satisfactoriamente"
        if isinstance(actualizar, Exception):
            return actualizar.pgerror

    def eliminarMedicamento(self, codigo):
        eliminar =self.daoMedicamento.borrarMedicamento(codigo)
        if actualizar is 0:
            return "Se ha eliminado satisfactoriamente"
        if isinstance(actualizar, Exception):
            return actualizar.pgerror

    def listarMedicamento(self):
        listar = self.daoMedicamento.mostrarMedicamento()
        if listar is 1:
            return "No hay Medicamentos"
        if isinstance(listar, Exception):
            return listar.pgerror