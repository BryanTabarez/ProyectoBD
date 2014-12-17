
class DaoLogin():
   
    def __init__(self, conexion):
        self.conn = conexion

 
    #============================== READ ======================================
    # CONSULTA UNA CAMA PARTICULAR
    def iniciarSesionAdministrador(self, identificacion, nombre):
        try:
            cur = self.conn.cursor()
            sqlConsulta = """SELECT COUNT(*) 
            FROM Persona NATURAL JOIN Medico
            WHERE identificacion = %s  AND nombre ILIKE %s """
            cur.execute(sqlConsulta, (identificacion,nombre))
            consulta = cur.fetchone()
            if consulta is None:
                cur.close()
                return 1
            else:
                cur.close()
                return consulta
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    def iniciarSesionEnfermera(self, identificacion, nombre):
        try:
            cur = self.conn.cursor()
            sqlConsulta = """SELECT COUNT(*) 
            FROM Persona NATURAL JOIN Enfermera
            WHERE identificacion = %s  AND nombre ILIKE %s """
            cur.execute(sqlConsulta, (identificacion,nombre))
            consulta = cur.fetchone()
            if consulta is None:
                cur.close()
                return 1
            else:
                cur.close()
                return consulta
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e



          