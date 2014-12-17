

class DaoHabilidades():
    def __init__(self, conexion):
        self.conn = conexion

    #============================= CONSULTAR TODAS LAS HABILIDADES =============
    def consultarHabilidades(self):
        try:
            cur = self.conn.cursor()
            sqlConsulta = "SELECT * FROM Habilidad"

            cur.execute(sqlConsulta)
            consulta = cur.fetchall()

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