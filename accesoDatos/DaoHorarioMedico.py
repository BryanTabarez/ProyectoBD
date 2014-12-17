

class DaoHorarioMedico():

    def __init__( self, conexion ):

        self.conn = conexion

    #======================== OBTENER MEDICOS POR ESPECIALIDAD ================

    def consultarHorariosMedicosPorEspecialidad(self, especialidad):
        try:
            cur = self.conn.cursor()
            sqlConsulta = """SELECT id_horario, Persona.nombre,fecha_hora 
            FROM Persona NATURAL JOIN Medico
            NATURAL JOIN Horario_Consulta WHERE especialidad = %s  AND disponible = %s"""
            cur.execute(sqlConsulta, (especialidad,True))
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
     #============================== UPDATE ====================================
    def cambiarEstadoHorario(self, id_horario, disponible):
        try:
            cur = self.conn.cursor()
            sqlUpdate = """UPDATE Horario_Consulta SET disponible = %s 
            WHERE id_horario = %s"""
            cur.execute(sqlUpdate, (disponible,id_horario))
            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e

    #============================== INSERTAR HORARIOS ===========================

    def insertarHorarios(self, id_medico, fecha):
        try:
            cur = self.conn.cursor()

            cur.execute("""INSERT INTO Horario_Consulta (id_medico, fecha_hora)
            VALUES (%s, %s)""", (id_medico, fecha))
            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
