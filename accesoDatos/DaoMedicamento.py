from logica import Medicamento


class DaoMedicamento():
    """Clase DaoMedicamento"""

    def __init__(self, conexion):
        self.conn = conexion

    #============================== CREATE ====================================
    def guardarMedicamento(self, drug):
        try:
            cur = self.conn.cursor()

            cur.execute("""INSERT INTO Medicamento (codigo, nombre, costo,
            descripcion) VALUES (%s, %s, %s, %s)""",
                (drug.get_codigo(), drug.get_nombre(), drug.get_costo(),
                    drug.get_descripcion()))

            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== READ ======================================
    # CONSULTA UN MEDICAMENTO PARTICULAR
    def consultarMedicamento(self, codigo):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM Medicamento WHERE codigo = %s",
                (codigo,))

            consulta = cur.fetchone()
            if consulta is None:
                cur.close()
                return 1
            else:
                drugResult = Medicamento(consulta[0], consulta[1], consulta[2],
                consulta[3])
                cur.close()
                return drugResult

            cur.close()
            self.conn.commit()
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== UPDATE ====================================
    def modificarMedicamento(self, drug):
        #try:
            #cur = self.conn.cursor()
            #sqlUpdate = """UPDATE Area SET nombre = %s, descripcion = %s
            #WHERE codigo = %s"""
            #cur.execute(sqlUpdate, (area.get_nombre_area(),
            #area.get_descripcion(), area.get_codigo_area()))
            #cur.close()
            #self.conn.commit()
        #except Exception as e:
            #cur.close()
            #self.conn.reset()
            #return e
        pass
    #==========================================================================

    #============================== DELETE ====================================
    def borrarMedicamento(self, codigo):
        #try:
            #cur = self.conn.cursor()

            #cur.execute("DELETE FROM Area WHERE codigo = %s", (codigoArea,))

            #cur.close()
            #self.conn.commit()
        #except Exception as e:
            #cur.close()
            #self.conn.reset()
            #return e
        pass
    #==========================================================================