from logica.Paciente import Paciente


class DaoPaciente():

    def __init__(self, conexion):
        self.conn = conexion

    def guardarPaciente(self, p):
        # Abrir un cursor para realizar operaciones con la base de datos
        cur = self.conn.cursor()

        cur.execute("INSERT INTO Persona VALUES (%s, %s, %s, %s)",
            (p.get_identificacion(), p.get_nombre(), p.get_direccion(),
                p.get_telefono()))

        cur.execute("INSERT INTO Paciente VALUES (%s, %s, %s, %s)",
            (p.get_identificacion(), p.get_fecha_nacimiento(),
                p.get_actividad_economica(), p.get_num_seg_social()))

        # Cerrar el cursor
        cur.close()

        # Hacer que los cambios en la base de datos sean permanentes
        self.conn.commit()

    def borrarPaciente(self, id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM Paciente WHERE identificacion = %s", (id,))
        cur.close()
        self.conn.commit()

    def consultarPaciente(self, id):
        cur = self.conn.cursor()
        sqlConsulta = "SELECT * FROM Paciente NATURAL JOIN Persona WHERE"
        sqlConsulta += " identificacion = %s"
        cur.execute(sqlConsulta, (id,))
        consulta = cur.fetchone()
        paciente = Paciente(consulta[0], consulta[1], consulta[2], consulta[3],
            consulta[4], consulta[5], consulta[6])
        cur.close()
        return paciente

    #def modificarPaciente(self, codigo, p):