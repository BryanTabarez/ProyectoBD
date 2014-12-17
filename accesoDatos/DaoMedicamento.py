from logica import Medicamento


class DaoMedicamento():
    """Clase DaoMedicamento"""

    def __init__(self, conexion):
        self.conn = conexion

    #============================== CREATE ====================================
    def guardarMedicamento(self, drug):
        try:
            cur = self.conn.cursor()

            cur.execute("""INSERT INTO Medicamento ( costo, nombre,
            descripcion) VALUES (%s, %s, %s)""",
                (drug.get_costo(), drug.get_nombre(), 
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
    def consultarMedicamento(self, nombre):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM Medicamento WHERE nombre = %s",
                (nombre,))

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
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== UPDATE ====================================
    def modificarMedicamento(self, drug):
        try:
            cur = self.conn.cursor()
            sqlUpdate = """UPDATE Medicamento SET costo = %s, nombre = %s,
            descripcion = %s WHERE codigo = %s"""
            cur.execute(sqlUpdate, (drug.get_costo(), drug.get_nombre(),
            drug.get_descripcion(), drug.get_codigo()))
            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== DELETE ====================================
    def borrarMedicamento(self, codigo):
        try:
            cur = self.conn.cursor()

            cur.execute("DELETE FROM Medicamento WHERE codigo = %s", (codigo,))

            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    def mostarMedicamento(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM Medicamento")

            consulta = cur.fetchall()
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