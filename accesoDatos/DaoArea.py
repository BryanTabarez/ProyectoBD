from logica import Area


class DaoArea():
    """Clase DaoArea"""

    def __init__(self, conexion):
        self.conn = conexion

    #============================== CREATE ====================================
    def guardarArea(self, a):
        try:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO Area (nombre, descripcion) VALUES(%s, %s)",
                (a.get_nombre_area(), a.get_descripcion()))

            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== READ ======================================
    # CONSULTA UN AREA PARTICULAR
    def consultarArea(self, codigo):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM Area WHERE codigo = %s",
                (codigo,))

            consulta = cur.fetchone()
            if consulta is None:
                cur.close()
                return 1
            else:
                areaConsultada = Area(consulta[0], consulta[1], consulta[2])
                cur.close()
                return areaConsultada

            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== UPDATE ====================================
    def modificarArea(self, area):
        try:
            cur = self.conn.cursor()
            sqlUpdate = """UPDATE Area SET nombre = %s, descripcion = %s
            WHERE codigo = %s"""
            cur.execute(sqlUpdate, (area.get_nombre_area(),
            area.get_descripcion(), area.get_codigo_area()))
            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== DELETE ====================================
    def borrarArea(self, codigoArea):
        try:
            cur = self.conn.cursor()

            cur.execute("DELETE FROM Area WHERE codigo = %s", (codigoArea,))

            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================
