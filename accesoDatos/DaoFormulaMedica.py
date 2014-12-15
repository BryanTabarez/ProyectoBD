from logica.FormulaMedica import FormulaMedica


class DaoFormulaMedica():
    "Clase DaoFormulaMedica"

    def __init__(self, conexion):
        self.conn = conexion

    #============================== CREATE ====================================
    def guardarFormulaMedica(self, fm):
        try:
            cur = self.conn.cursor()

            cur.execute("""INSERT INTO FormulaMedica VALUES (%s, %s, %s)""",
            (fm.get_num_registro(), fm.get_cod_medicamento(),
            fm.get_cantidad()))

            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== READ ======================================
    # CONSULTA UNA CAMA PARTICULAR
    def consultarFormulaMedica(self, id):
        try:
            cur = self.conn.cursor()
            sqlConsulta = """SELECT * FROM FormulaMedica WHERE
            numero_registro = %s"""
            cur.execute(sqlConsulta, (id,))
            consulta = cur.fetchall()
            if consulta is None:
                cur.close()
                return 1
            else:
                fm = FormulaMedica(consulta[0][0], consulta[0][1],
                consulta[0][2])
                cur.close()
                return fm
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== UPDATE ====================================
    def modificarFormulaMedica(self, fm):
        try:
            cur = self.conn.cursor()

            sqlUpdate = """UPDATE FormulaMedica SET cantidad = %s
            WHERE numero_registro = %s AND codigo_medicamento = %s"""

            cur.execute(sqlUpdate, (fm.get_cantidad(), fm.get_num_registro(),
            fm.get_cod_medicamento()))

            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== DELETE ====================================
    def borrarCama(self, fm):
        try:
            cur = self.conn.cursor()
            cur.execute("""DELETE FROM FormulaMedica
            WHERE numero_registro = %s AND codigo_medicamento = %s""",
            (fm.get_num_registro(), fm.get_cod_medicamento()))
            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================