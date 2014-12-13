from logica import Paciente


class DaoPaciente():

    def __init__(self, conexion):
        self.conn = conexion

    def guardarPaciente(self, p):
        try:
            cur = self.conn.cursor()

            cur.execute("INSERT INTO Persona VALUES (%s, %s, %s, %s)",
                (p.get_identificacion(), p.get_nombre(), p.get_direccion(),
                    p.get_telefono()))

            cur.execute("INSERT INTO Paciente VALUES (%s, %s, %s, %s)",
                (p.get_identificacion(), p.get_fecha_nacimiento(),
                    p.get_actividad_economica(), p.get_num_seg_social()))

            cur.close()
            self.conn.commit()
        except Exception as e:  # mas precisamente deberia usar psycopg2.Error
            cur.close()
            self.conn.reset()
            return e

    def borrarPaciente(self, id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM Paciente WHERE identificacion = %s", (id,))
        cur.execute("DELETE FROM Persona WHERE identificacion = %s", (id,))
        cur.close()
        self.conn.commit()

    def consultarPaciente(self, id):
        try:
            cur = self.conn.cursor()
            sqlConsulta = """SELECT * FROM Persona NATURAL JOIN Paciente  WHERE
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
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e

    def modificarPaciente(self, p):
        try:
            cur = self.conn.cursor()

            sqlUpdate1 = """UPDATE Persona SET nombre = %s, direccion = %s,
            telefono = %s WHERE identificacion = %s"""

            sqlUpdate2 = """UPDATE Paciente SET fecha_nacimiento = %s,
            actividad_economica = %s, num_seguridad_social = %s WHERE
            identificacion = %s"""

            cur.execute(sqlUpdate1, (p.get_nombre(), p.get_direccion(),
            p.get_telefono(), p.get_identificacion(), ))

            cur.execute(sqlUpdate2, (p.get_fecha_nacimiento(),
            p.get_actividad_economica(), p.get_num_seg_social(),
            p.get_identificacion(), ))

            cur.close()
            self.conn.commit()
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e