#from logica.CampanaPrevencion import CampanaPrevencion


class DaoCampanaPrevencion():
    """Clase DaoCampanaPrevencion"""

    def __init__(self, conexion):
        self.conn = conexion

    #============================== CREATE ====================================
    def guardarCampanaPrevencion(self, camp):
        #try:
            #cur = self.conn.cursor()

            #cur.execute("""INSERT INTO Cama (estado, descripcion, codigo_area)
            #VALUES (%s, %s, %s)""", (bed.get_estado(), bed.get_descripcion(),
            #bed.get_cod_area()))

            #cur.close()
            #self.conn.commit()
            #return 0
        #except Exception as e:
            #cur.close()
            #self.conn.reset()
            #return e
        pass
    #==========================================================================

    #============================== READ ======================================
    # CONSULTA UNA CAMPANA DE PREVENCION PARTICULAR
    def consultarCampanaPrevencion(self, codigo):
        pass
        #try:
            #cur = self.conn.cursor()
            #sqlConsulta = """SELECT * FROM Cama WHERE num_cama = %s"""
            #cur.execute(sqlConsulta, (id,))
            #consulta = cur.fetchone()
            #if consulta is None:
                #cur.close()
                #return 1
            #else:
                #cama = Cama(consulta[0], consulta[1], consulta[2], consulta[3])
                #cur.close()
                #return cama
        #except Exception as e:
            #cur.close()
            #self.conn.reset()
            #return e
    #==========================================================================

    #============================== UPDATE ====================================
    def modificarCampanaPrevencion(self, camp):
        pass
        #try:
            #cur = self.conn.cursor()

            #sqlUpdate = """UPDATE Cama SET estado = %s, descripcion = %s,
            #codigo_area = %s WHERE num_cama = %s"""

            #cur.execute(sqlUpdate, (bed.get_estado(), bed.get_descripcion(),
            #bed.get_cod_area(), bed.get_num_cama()))

            #cur.close()
            #self.conn.commit()
            #return 0
        #except Exception as e:
            #cur.close()
            #self.conn.reset()
            #return e
    #==========================================================================

    #============================== DELETE ====================================
        def borrarCampanaPrevencion(self, codigo):
            pass
            #try:
                #cur = self.conn.cursor()
                #cur.execute("DELETE FROM Cama WHERE num_cama = %s", (id,))
                #cur.close()
                #self.conn.commit()
                #return 0
            #except Exception as e:
                #cur.close()
                #self.conn.reset()
                #return e
    #==========================================================================