from logica.Enfermera import Enfermera


class DaoEnfermera():

    def __init__(self, conexion):
        self.conn = conexion

    def guardarEnfermera(self, e):
        try:

            cur = self.conn.cursor()
            #INSERTAR PERSONA, EMPLEADO Y ENFERMERA
            cur.close()

            self.conn.commit()
        except:
            print("Error!")
            print("No se pudo guardar el registro en la base de datos")

    def borrarEnfermera(self, id):
        cur = self.conn.cursor()
        # ELIMINAR EMPLEADO (Y ENFERMERA)
        cur.close()
        self.conn.commit()

    def consultarEnfermera(self, id):
        try:
            cur = self.conn.cursor()
            sqlConsulta = """SELECT * FROM Paciente NATURAL JOIN Persona WHERE
            identificacion = %s"""
            cur.execute(sqlConsulta, (id,))
            consulta = cur.fetchone()
            if consulta is None:
                print("La consulta no arrojo resultados")
                cur.close()
                return 0
            else:
                paciente = Paciente(consulta[0], consulta[1], consulta[2],
                    consulta[3], consulta[4], consulta[5], consulta[6])
                cur.close()
                return paciente
        except:
            print("ERROR en la consulta!")

    def modificarEnfermera(self, id, p):
        cur = self.conn.cursor()

        sqlUpdate1 = """UPDATE Persona SET nombre = %s, direccion = %s,
        telefono = %s WHERE identificacion = %s"""

        sqlUpdate2 = """UPDATE Paciente SET fecha_nacimiento = %s,
        actividad_economica = %s, num_seguridad_social = %s WHERE
        identificacion = %s"""

        cur.execute(sqlUpdate1, (p.get_nombre(), p.get_direccion(),
        p.get_telefono(), id, ))

        cur.execute(sqlUpdate2, (p.get_fecha_nacimiento(),
        p.get_actividad_economica(), p.get_num_seg_social(), id, ))

        self.conn.commit()
        cur.close()