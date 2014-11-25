from accesoDatos.DaoPaciente import DaoPaciente
from accesoDatos.FachadaDB import FachadaDB
from logica.Paciente import Paciente


def main():
    fachada = FachadaDB()
    conexion = fachada.obtenerConexion()
    daoPac = DaoPaciente(conexion)

    ##PRUEBA INSERTAR PACIENTE
    paciente = Paciente(110, 'Esteban Quito', 'Calle 5', '018800777',
       '2014-01-01', 'corredor de bolsa', 900)
    daoPac.guardarPaciente(paciente)

    ##PRUEBA BORRAR PACIENTE
    #daoPac.borrarPaciente(110)

    ##PRUEBA CONSULTAR PACIENTE
    #paciente = daoPac.consultarPaciente(110)
    #print((paciente.get_identificacion()))
    #print((paciente.get_nombre()))
    #print((paciente.get_num_seg_social()))

    ##PRUEBA MODIFICAR PACIENTE

    fachada.cerrarConexion()

main()