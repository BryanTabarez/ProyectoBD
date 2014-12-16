from accesoDatos import DaoPaciente
from logica import Paciente


def mostrarReturn(resultado):
    if resultado is not None:
        print("\nExcepcion capturada! Falta Implementar!!")
        print((resultado.pgerror))

class ControlDaoPaciente():

	def __init__( self, conexion ):
		self.daoPaciente = DaoPaciente( conexion )

	def ingresarPaciente( self, identificacion, nombre, direccion, telefono,
		fecha_nacimiento, actividad_economica, num_seg_social ):

		paciente = Paciente( identificacion, nombre, direccion, telefono, 
			fecha_nacimiento, actividad_economica, num_seg_social)

		insertarPaciente = self.daoPaciente.guardarPaciente( paciente )
		if insertarPaciente is 0:
			return "El paciente se ingreso con exito"
		if isinstance (insertarPaciente, Exception):
			return "No fue posible ingresar el paciente a la base de datos"

	def modificarPacinete( self, identificacion, nombre, direccion, 
		telefono, fecha_nacimiento, actividad_economica, num_seg_social ):

		paciente = Paciente( identificacion, nombre, direccion, telefono, 
			fecha_nacimiento, actividad_economica, num_seg_social)

		actualizarPaciente = self.daoPaciente.modificarPaciente( paciente )
		if actualizarPaciente is 0:
			return "El paciente se ingreso con exito"
		if isinstance (actualizarPaciente, Exception):
			return "No fue posible ingresar el paciente a la base de datos"

	def consultar( self, id ):

		paciente = self.daoPaciente.consultarPaciente( id )
		if isinstance (paciente, Paciente):
			return [ 

			paciente.get_identificacion(), paciente.get_nombre(),
			paciente.get_direccion(), paciente.get_telefono(), 
			paciente.get_fecha_nacimiento(), 
			paciente.get_actividad_economica(), paciente.get_num_seg_social()

			]
		else:
			return 0

	def listarPacientes( self ):

		matriz_pacientes = self.daoPaciente.listarPacientes()
		if matriz_pacientes == 0 or matriz_pacientes == 1:
			return 0
		else:
			return matriz_pacientes

	def borrarPaciente( self, id ):

		resultado = self.daoPaciente.borrarPaciente( id )
		if resultado is 0:
			return "El paciente fue eliminado con exito"
		if isinstance (resultado, Exception):
			return "No fue posible eliminar el paciente a la base de datos"

		