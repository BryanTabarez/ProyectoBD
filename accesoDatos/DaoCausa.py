from logica import Causa


class DaoCausa():

    def __init__(self, conexion):
        self.conn = conexion

    #============================== CREATE ====================================
    def guardarCausa(self, cause):
        try:
            cur = self.conn.cursor()

            cur.execute("INSERT INTO Causa(nombre, descripcion) VALUES(%s, %s)",
                (cause.get_nombre(), cause.get_descripcion()))

            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== READ ======================================
    # CONSULTA UNA CAUSA PARTICULAR POR CODIGO
    def consultarCausa(self, codigo):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM Causa WHERE codigo = %s",
                (codigo,))

            consulta = cur.fetchone()
            if consulta is None:
                cur.close()
                return 1
            else:
                cause = Causa(consulta[0], consulta[1], consulta[2])
                cur.close()
                return cause

            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== UPDATE ====================================
    def modificarCausa(self, cause):
        try:
            cur = self.conn.cursor()
            sqlUpdate = """UPDATE Causa SET nombre = %s, descripcion = %s
            WHERE codigo = %s"""
            cur.execute(sqlUpdate, (cause.get_nombre(), cause.get_descripcion(),
            cause.get_codigo()))
            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== DELETE ====================================
    def borrarCausa(self, codigo):
        try:
            cur = self.conn.cursor()

            cur.execute("DELETE FROM Causa WHERE codigo = %s", (codigo,))

            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================