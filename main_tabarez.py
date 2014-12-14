from logica import *
from accesoDatos import *

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic


#==============================================================================
def mostrarReturn(resultado):
    """Este metodo por ahora es el que se encarga de "controlar" las
    excepciones a nivel de la base de datos (psycopg2).
    Lo que hace es simplemente mostrar el mensaje de la excepcion capturada"""
    if resultado is not None:
        print("\nExcepcion capturada! Falta Implementar juemadre!!")
        print((resultado.pgerror))
#==============================================================================


#==============================================================================
def pruebasDaoPaciente(conexion):
    daoPac = DaoPaciente(conexion)

    # INSERTAR PACIENTE
    paciente = Paciente(110, 'Esteban Quito', 'Calle 5', '018800777',
       '2014-01-01', 'corredor de bolsa', 900)
    result = daoPac.guardarPaciente(paciente)
    if isinstance(result, Exception):
        mostrarReturn(result)

    # CONSULTAR PACIENTE
    paciente2 = daoPac.consultarPaciente(110)
    if isinstance(paciente2, Exception):
        mostrarReturn(paciente2)
    if paciente2 == 0:
        print("LA CONSULTA NO ARROJO RESULTADOS :(")
    else:
        print((paciente2.get_identificacion()))
        print((paciente2.get_nombre()))
        print((paciente2.get_fecha_nacimiento()))
        print((paciente2.get_direccion()))

    # MODIFICAR PACIENTE
    pac = daoPac.consultarPaciente(110)
    pac.set_fecha_nacimiento('1990-05-07')
    pac.set_direccion("AV 1 CRA 2")
    daoPac.modificarPaciente(pac)

    ## BORRAR PACIENTE
    #daoPac.borrarPaciente(110)
#==============================================================================


#==============================================================================
def pruebasDaoEnfermera(conexion):
    daoEnfe = DaoEnfermera(conexion)

    ## INSERTAR ENFERMERA
    angely = Enfermera(114230, "Angelly", "calle 45", "3108304383", 1,
        "angelly@correo.com", 2000000, 110, 3, [1, 4])
    insertEnf = daoEnfe.guardarEnfermera(angely)
    if isinstance(insertEnf, Exception):
        mostrarReturn(insertEnf)

    # CONSULTAR ENFERMERA

    # MODIFICAR ENFERMERA

    # BORRAR ENFERMERA
    deleteEnf = daoEnfe.borrarEnfermera(114230)
    if isinstance(deleteEnf, Exception):
        mostrarReturn(deleteEnf)
#==============================================================================


#==============================================================================
def pruebasDaoArea(conexion):
    daoArea = DaoArea(conexion)
    ## INSERTAR AREA
    """Como la llave primaria es codigo y este es un serial, se puede ingresar
    varias veces la misma area y va cambiando solo el codigo de area"""
    area = Area(2, "INFANTIL", """Cirugias ambulatorias y Hospitalizacion
    desde Recien Nacido hasta menores de 16 anios.""")
    insertArea = daoArea.guardarArea(area)
    if isinstance(insertArea, Exception):
        mostrarReturn(insertArea)

    # CONSULTAR AREA
    area = daoArea.consultarArea(2)
    if isinstance(area, Exception):
        mostrarReturn(area)
    if area == 0:
        print("LA CONSULTA NO ARROJO RESULTADOS :(")
    else:
        print((area.get_nombre_area()))

    # MODIFICAR AREA
    area.set_nombre_area("Pediatria")
    modArea = daoArea.modificarArea(area)
    if isinstance(modArea, Exception):
        mostrarReturn(modArea)

    # BORRAR AREA
    #delArea = daoArea.borrarArea(1)
    #if isinstance(delArea, Exception):
        #mostrarReturn(delArea)
#==============================================================================


#==============================================================================
class ControlDaoMedicamento():

    def __init__(self, conexion):
        self.daoDrug = DaoMedicamento(conexion)

    def insertarMedicamento(self, codigo, costo, nombre, descripcion):
        nwDrug = Medicamento(codigo, costo, nombre, descripcion)
        insertDrug = self.daoDrug.guardarMedicamento(nwDrug)
        if isinstance(insertDrug, Exception):
            mostrarReturn(insertDrug)
        else:
            return insertDrug

    def consultarMedicamento(self, codigo):
        drug = self.daoDrug.consultarMedicamento(codigo)
        if isinstance(drug, Exception):
            mostrarReturn(drug)
        if drug is 1:
            return 1
        else:
            return [drug.get_costo(), drug.get_nombre(), drug.get_descripcion()]
#==============================================================================


#==============================================================================
def pruebasDaoMedicamento(conexion):
    daoDrug = DaoMedicamento(conexion)

    ## INSERTAR MEDICAMENTO

    # CONSULTAR MEDICAMENTO

    # MODIFICAR MEDICAMENTO

    # BORRAR MEDICAMENTO
    deleteDrug = daoDrug.borrarMedicamento("vag100")
    if isinstance(deleteDrug, Exception):
        mostrarReturn(deleteDrug)
#==============================================================================


#==============================================================================
def main():
    app = QApplication(sys.argv)

    fachada = FachadaDB()
    conexion = fachada.obtenerConexion()

    mostrarVentana = VentanaMedicamento(None, conexion)
    mostrarVentana.show()
    r = app.exec_()
    #pruebasDaoMedicamento(conexion)

    fachada.cerrarConexion()

    print(("Fin " + str(r)))
    sys.exit(r)
#==============================================================================

#  CAMA
#  CAUSA
#  CAMPANIA_PREVENCION
#  FORMULA_MEDICA

VmClass, InterfazAdministradorInterfazBase_class = uic.loadUiType('untitled.ui')


class VentanaMedicamento(QMainWindow, VmClass):


    def __init__(self, parent, conexion):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        # CENTRAR EL QMainWindow
        pantalla = QDesktopWidget().screenGeometry()
        interfaz = self.geometry()
        pos_horizontal = (pantalla.width() - interfaz.width()) / 2
        pos_vertical = (pantalla.height() - interfaz.height()) / 2
        self.move(pos_horizontal, pos_vertical)

        # SENIALES Y SLOTS
        self.connect(self.pushButtonInsertar, SIGNAL("clicked()"),
            self.pruebaInsertarMedicamento)
        self.connect(self.pushButtonConsultar, SIGNAL("clicked()"),
            self.pruebaBuscarMedicamento)
        self.connect(self.pushButtonLimpiar, SIGNAL("clicked()"),
            self.limpiarCampos)

        # CREAR EL CONTROLADOR DEL DAO MEDICAMENTO
        self.ctrlDaoMedicamento = ControlDaoMedicamento(conexion)

    def limpiarCampos(self):
        self.lineEditCodigo.clear()
        self.lineEditCosto.clear()
        self.lineEditNombre.clear()
        self.lineEditDescripcion.clear()

    def pruebaInsertarMedicamento(self):
        codigo = str(self.lineEditCodigo.text())
        costo = str(self.lineEditCosto.text())
        nombre = str(self.lineEditNombre.text())
        descripcion = str(self.lineEditDescripcion.text())

        insert = self.ctrlDaoMedicamento.insertarMedicamento(codigo, costo,
            nombre, descripcion)

        self.limpiarCampos()

        if insert is 0:
            self.lineEditMensaje.setText("Se agrego el registro en la BD!")

    def pruebaBuscarMedicamento(self):
        codigo = str(self.lineEditCodigo.text())
        result = self.ctrlDaoMedicamento.consultarMedicamento(codigo)
        if type(result) is list:
            self.lineEditCosto.setText(result[0])
            self.lineEditNombre.setText(result[1])
            self.lineEditDescripcion.setText(result[2])
        if result is 1:
            self.lineEditMensaje.setText("La consulta no arrojo resultados!")


main()