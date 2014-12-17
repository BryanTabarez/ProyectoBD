

class DaoHorarioMedico():

    def __init__( self, conexion ):

        self.conn = conexion

    #======================== OBTENER MEDICOS POR ESPECIALIDAD ================

    def consultarHorariosMedicosPorEspecialidad(self, especialidad):
        try:
            cur = self.conn.cursor()
            sqlConsulta = """SELECT Persona.identificacion, Persona.nombre,fecha_hora 
            FROM Persona NATURAL JOIN Medico
            NATURAL JOIN Horario_Consulta WHERE especialidad = %s"""

            cur.execute(sqlConsulta, (especialidad,))
            consulta = cur.fetchall()
            if consulta is None:
                cur.close()
                return 1
            else:
                cur.close()
                return consulta
            cur.close()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
