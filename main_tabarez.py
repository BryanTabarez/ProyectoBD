from logica import *
from accesoDatos import *


def mostrarReturn(resultado):
    """Este metodo por ahora es el que se encarga de "controlar" las
    excepciones a nivel de la base de datos (psycopg2).
    Lo que hace es simplemente mostrar el mensaje de la excepcion capturada"""
    if resultado is not None:
        print("\nExcepcion controlada :) -->")
        print((resultado.pgerror))


def main():
    fachada = FachadaDB()
    conexion = fachada.obtenerConexion()

# PRUEBAS DAO PACIENTE
    daoPac = DaoPaciente(conexion)
#==============================================================================

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

# PRUEBAS DAO ENFERMERA
    daoEnfe = DaoEnfermera(conexion)
#==============================================================================
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

# PRUEBAS DAO AREA
    #daoArea = DaoArea(conexion)
#==============================================================================
    ## INSERTAR AREA
    """Como la llave primaria es codigo y este es un serial, se puede ingresar
    varias veces la misma area y va cambiando solo el codigo de area"""
    #area = Area("Urgencias", """Atencion integral del paciente que requiere
    #atencion medica de emergencia.""")
    #insertArea = daoArea.guardarArea(area)
    #if isinstance(insertArea, Exception):
        #mostrarReturn(insertArea)
#==============================================================================

# PRUEBAS DAO CAMA
#daoCama = DaoCama(conexion)
#==============================================================================

    ##Prueba insertar cama
    #cama = Cama("", "t", "Cama reclinable", 1)
    #daoCama.guardarCama(cama)

    ##Prueba consultar cama
    #cama = daoCama.consultarCama(2)
    #print("Codigo paciente = ")
    #print(cama.get_num_cama())

    ##Prueba borrar cama
    #daoCama.borrarCama(2)

#==============================================================================
    fachada.cerrarConexion()

main()