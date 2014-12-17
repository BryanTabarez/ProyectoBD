
class DaoHistoriaClinica():
    
    def __init__(self, conexion):
        self.conn = conexion

    
    def consultarNumeroHistoria(self, id_paciente):
        try:
            cur = self.conn.cursor()
            sqlConsulta = """SELECT numero_historia 
            FROM Persona 
            NATURAL JOIN Paciente 
            JOIN Historia_Clinica 
            ON Paciente.identificacion = Historia_Clinica.id_paciente
            WHERE id_paciente = %s """ 
            cur.execute(sqlConsulta, (id_paciente,))
            consulta = cur.fetchone()
            if consulta is None:
                cur.close()
                return 1
            else:
                return consulta
            cur.close()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e