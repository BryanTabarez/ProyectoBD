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

    #PRUEBA INSERTAR PACIENTE
    paciente = Paciente(110, 'Esteban Quito', 'Calle 5', '018800777',
       '2014-01-01', 'corredor de bolsa', 900)
    result = daoPac.guardarPaciente(paciente)
    if isinstance(result, Exception):
        mostrarReturn(result)

    ##PRUEBA CONSULTAR PACIENTE
    paciente2 = daoPac.consultarPaciente(110)
    if isinstance(paciente2, Exception):
        mostrarReturn(paciente2)
    if paciente2 == 0:
        print("LA CONSULTA NO ARROJO RESULTADOS :(")
    else:
        print((paciente2.get_identificacion()))
        print((paciente2.get_nombre()))
        print((paciente2.get_num_seg_social()))

    ##PRUEBA MODIFICAR PACIENTE --> FALTA

    ##PRUEBA BORRAR PACIENTE
    #daoPac.borrarPaciente(110)
#==============================================================================

#==============================================================================
    ##PRUEBA INSERTAR ENFERMERA
    #daoEnfe = DaoEnfermera(conexion)
    #angely = Enfermera(11145613, "Angelly", "calle 45", "3108304383", 1,
        #"angelly@correo.com", 2000000, 110, 3, [1, 4])
    #daoEnfe.guardarEnfermera(angely)

    #PRUEBA CONSULTAR ENFERMERA --> FALTA

    #PRUEBA BORRAR ENFERMERA --> FALTA
#==============================================================================

#==============================================================================

    #daoCama = DaoCama(conexion)
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
