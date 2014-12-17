from accesoDatos import DaoPaciente
from logica import Paciente


class ControlDaoPaciente():

	def __init__( self, conexion ):
		self.daoPaciente = DaoPaciente( conexion )

	def ingresarPaciente( self, identificacion, nombre, direccion, telefono,
		fecha_nacimiento, actividad_economica, num_seg_social ):

		paciente = Paciente( identificacion, nombre, direccion, telefono, 
			fecha_nacimiento, actividad_economica, num_seg_social)

		insertarPaciente = self.daoPaciente.guardarPaciente( paciente )
		return insertarPaciente

	def modificarPacinete( self, identificacion, nombre, direccion, 
		telefono, fecha_nacimiento, actividad_economica, num_seg_social ):

		paciente = Paciente( identificacion, nombre, direccion, telefono, 
			fecha_nacimiento, actividad_economica, num_seg_social)

		actualizarPaciente = self.daoPaciente.modificarPaciente( paciente )
		return actualizarPaciente


	def consultar( self, id ):
		print "Consultar Paciente: " + id
		paciente = self.daoPaciente.consultarPaciente( id )
		if isinstance (paciente, Paciente):
			return [ 

			paciente.get_identificacion(), paciente.get_nombre(),
			paciente.get_direccion(), paciente.get_telefono(), 
			paciente.get_fecha_nacimiento(), 
			paciente.get_actividad_economica(), paciente.get_num_seg_social()

			]
		else:
			return paciente

	def borrarPaciente( self, id ):
		print "Borrar Paciente: " + id
		resultado = self.daoPaciente.borrarPaciente( id )
		return resultado



	#Borararra
	def listarPacientes( self ):

		matriz_pacientes = self.daoPaciente.listarPacientes()
		if matriz_pacientes == 0 or matriz_pacientes == 1:
			return 0
		else:
			return matriz_pacientes

	

		