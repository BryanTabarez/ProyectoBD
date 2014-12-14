from logica import *
from accesoDatos import *


#==============================================================================
def mostrarReturn(resultado):
    """Este metodo por ahora es el que se encarga de "controlar" las
    excepciones a nivel de la base de datos (psycopg2).
    Lo que hace es simplemente mostrar el mensaje de la excepcion capturada"""
    if resultado is not None:
        print("\nExcepcion capturada -->")
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
def pruebasDaoMedicamento(conexion):
    daoDrug = DaoMedicamento(conexion)

    # INSERTAR MEDICAMENTO
    nwDrug = Medicamento("ACR01", 700, "Acetaminofeno (Rectal)",
        """se usa para aliviar el dolor y reducir la fiebre. A diferencia de la
        aspirina, no alivia el enrojecimiento, la rigidez o la hinchazon
        causados por la artritis reumatoidea. Sin embargo, puede aliviar el
        dolor causado por formas leves de artritis.""")
    insertDrug = daoDrug.guardarMedicamento(nwDrug)
    if isinstance(insertDrug, Exception):
        mostrarReturn(insertDrug)
#==============================================================================


#==============================================================================
def main():
    fachada = FachadaDB()
    conexion = fachada.obtenerConexion()

    #pruebasDaoPaciente(conexion)
    #pruebasDaoEnfermera(conexion)
    #pruebasDaoArea(conexion)
    pruebasDaoMedicamento(conexion)

    fachada.cerrarConexion()
#==============================================================================

main()