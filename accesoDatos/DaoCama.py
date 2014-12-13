from logica.Cama import Cama


class DaoCama():

    def __init__(self, conexion):
        self.conn = conexion

    def guardarCama(self, c):
        try:
            #Abrir un cursor para realizar operaciones con la base de datos
            cur = self.conn.cursor()

            cur.execute("""INSERT INTO Cama (estado, descripcion, codigo_area)
            VALUES (%s, %s, %s)""", (c.get_estado(), c.get_descripcion(),
            c.get_cod_area()))

            # Cerrar el cursor
            cur.close()

            # Hacer que los cambios en la base de datos sean permanentes
            self.conn.commit()
        except:
            print("Error!")
            print("No se pudo guardar el registro en la base de datos")

    def borrarCama(self, id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM Cama WHERE num_cama = %s", (id,))
        cur.close()
        self.conn.commit()

    def consultarCama(self, id):
        #try:
            cur = self.conn.cursor()
            sqlConsulta = """SELECT * FORM Cama NATURAL JOIN Area
            WHERE num_cama = %s"""
            cur.execute()(sqlConsulta, (id,))
            consulta = cur.fetchone()
            if consulta is None:
                print("La consulta no arrojo resultados")
                cur.close()
                return 0
            else:
                cama = Cama(consulta[0], consulta[1], consulta[2], consulta[3])
                cur.close()
                return cama
        #except:
            #print("Error en la consulta!")

    def modificarCama(self, c):
        cur = self.conn.cursor()

        sqlUpdate = """UPDATE Cama SET estado = %s, descripcion = %s,
        codigo_area = %s WHERE num_cama = %s"""

        cur.execute(sqlUpdate, (c.get_estado(), c.get_descripcion(),
        c.get_cod_area(), c.get_num_cama(),))

        self.conn.commit()
        cur.close()

