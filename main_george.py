from accesoDatos import *
from logica import *


def mostrarReturn(resultado):
    """Este metodo por ahora es el que se encarga de "controlar" las
    excepciones a nivel de la base de datos (psycopg2).
    Lo que hace es simplemente mostrar el mensaje de la excepcion capturada"""
    if resultado is not None:
        print("\nExcepcion capturada! Falta Implementar juemadre!!")
        print((resultado.pgerror))


def pruebaDaoCama(conexion):
    daoCama = DaoCama(conexion)

    ##Prueba insertar cama
    #cama = Cama('true', "cama doble", 1)
    #ingresarCama = daoCama.guardarCama(cama)
    #if isinstance(ingresarCama, Exception):
        #mostrarReturn(ingresarCama)

    ##Prueba Modificar Cama
    #cama = Cama(1, 'true', "cama doble reclinable", 1)
    #modificacionCama = daoCama.modificarCama(cama)
    #if isinstance(modificacionCama, Exception):
        #mostrarReturn(modificacionCama)

    ##Prueba consultar cama
    cama = daoCama.consultarCama(1)
    if isinstance(cama, Exception):
        mostararReturn(cama)
    if cama == 1:
        print("la consulta no arrojo resultados")
    else:
        print "numero de la cama es: ", (cama.get_num_cama())
        print "el estado de la cama es: ", (cama.get_estado())
        print "esta es la descripcion de la cama: ", (cama.get_descripcion())
        print "el codigo de area de pertenecia: ", (cama.get_cod_area())

    ##Prueba borrar cama
    #borradoCama = daoCama.borrarCama(2)
    #if isinstance(borradoCama, Exception):
        #mostrarReturn(borradoCama)


def main():
    fachada = FachadaDB()
    conexion = fachada.obtenerConexion()

    pruebaDaoCama(conexion)

    fachada.cerrarConexion()


main()

