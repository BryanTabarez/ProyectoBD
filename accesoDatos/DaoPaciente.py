from logica.Paciente import Paciente


class DaoPaciente():

    def __init__(self, conexion):
        self.conn = conexion

    def guardarPaciente(self, p):
        try:
            # Abrir un cursor para realizar operaciones con la base de datos
            cur = self.conn.cursor()

            cur.execute("INSERT INTO Persona VALUES (%s, %s, %s, %s)",
                (p.get_identificacion(), p.get_nombre(), p.get_direccion(),
                    p.get_telefono()))

            cur.execute("INSERT INTO Paciente VALUES (%s, %s, %s, %s)",
                (p.get_identificacion(), p.get_fecha_nacimiento(),
                    p.get_actividad_economica(), p.get_num_seg_social()))

            # Cerrar el cursor
            cur.close()

            # Hacer que los cambios en la base de datos sean permanentes
            self.conn.commit()
        except:
            print("Error!")
            print("No se pudo guardar el registro en la base de datos")

    def borrarPaciente(self, id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM Paciente WHERE identificacion = %s", (id,))
        cur.close()
        self.conn.commit()

    def consultarPaciente(self, id):
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

    def modificarPaciente(self, id, p):
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