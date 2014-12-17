from accesoDatos import DaoMedicamento
from logica import Medicamento


#============= METODO PARA MOSTRAR LAS EXCEPCIONES DE psycopg2 ================
def mostrarReturn(resultado):
    if resultado is not None:
        print("\nExcepcion capturada! Falta Implementar!!")
        print((resultado.pgerror))
#==============================================================================


class ControlDaoMedicamento():

    def __init__(self, conexion):
        self.daoMedicamento = DaoMedicamento(conexion)

    def insertarMedicamento(self, costo, nombre, descripcion):
        medicamento = Medicamento(costo, nombre, descripcion)
        insertar = self.daoMedicamento.guardarMedicamento(medicamento)
        if insertar is 0:
            return "Se ha ingresado satisfactoriamente"
        if isinstance(insertar, Exception):
            return "No se pudo ingrsar el medicamento :("

    def buscarMedicamento(self, nombre):
        buscar = self.daoMedicamento.consultarMedicamento(nombre)
        if buscar is 1:
            return "La consulta no arrojo resultados"
        else:
            return buscar
        if isinstance(buscar, Exception):
            return "No se pudo consultar el medicamento :("

    def actualizarMedicamento(self, codigo, costo, nombre, descripcion):
        medicamento = Medicamento(codigo, costo, nombre, descripcion)
        actualizar = self.daoMedicamento.modificarMedicamento(medicamento)
        if actualizar is 0:
            return "Se ha modificado satisfactoriamente"
        if isinstance(actualizar, Exception):
            return "No se pudo modificar el medicamento :("

    def eliminarMedicamento(self, codigo):
        eliminar =self.daoMedicamento.borrarMedicamento(codigo)
        if actualizar is 0:
            return "Se ha eliminado satisfactoriamente"
        if isinstance(actualizar, Exception):
            return "No se pudo eliminar el medicamento :("

    def listarMedicamento(self):
        listar = self.daoMedicamento.mostrarMedicamento()
        if listar is 1:
            return "No hay Medicamentos"
        if isinstance(listar, Exception):
            return "No se pudo listar los medicamentos :("