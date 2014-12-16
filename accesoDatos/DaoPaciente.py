from logica import Paciente


class DaoPaciente():
    """Clase DaoPaciente"""
    def __init__(self, conexion):
        self.conn = conexion

    #============================== CREATE ====================================
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
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== READ ======================================
    def consultarPaciente(self, id):
        try:
            cur = self.conn.cursor()
            sqlConsulta = """SELECT * FROM Persona NATURAL JOIN Paciente  WHERE
            identificacion = %s"""
            cur.execute(sqlConsulta, (id,))
            consulta = cur.fetchone()
            if consulta is None:
                cur.close()
                return 1
            else:
                paciente = Paciente(consulta[0], consulta[1], consulta[2],
                    consulta[3], consulta[4], consulta[5], consulta[6])
                cur.close()
                return paciente
            cur.close()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== UPDATE ====================================
    def modificarPaciente(self, p):
        try:
            cur = self.conn.cursor()

            sqlUpdate1 = """UPDATE Persona SET nombre = %s, direccion = %s,
            telefono = %s WHERE identificacion = %s"""

            sqlUpdate2 = """UPDATE Paciente SET fecha_nacimiento = %s,
            actividad_economica = %s, num_seguridad_social = %s WHERE
            identificacion = %s"""

            # Actualizar datos en Persona
            cur.execute(sqlUpdate1, (p.get_nombre(), p.get_direccion(),
            p.get_telefono(), p.get_identificacion(), ))

            # Actualizar datos en Paciente
            cur.execute(sqlUpdate2, (p.get_fecha_nacimiento(),
            p.get_actividad_economica(), p.get_num_seg_social(),
            p.get_identificacion(), ))

            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== DELETE ====================================
    # OJO: TENER EN CUENTA EL REGISTRO EN LA HISTORIA CLINICA /  TRIGGER ?
    def borrarPaciente(self, id):
        try:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM Paciente WHERE identificacion = %s", (id,))
            cur.execute("DELETE FROM Persona WHERE identificacion = %s", (id,))
            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================
    #============================== LIST ======================================
    def listarPacientes(self):
        try:
            cur = self.conn.cursor()
            sqlConsulta = """SELECT * FROM Persona NATURAL JOIN Paciente """
            cur.execute(sqlConsulta)
            consulta = cur.fetchall()
            if consulta is None:
                cur.close()
                return 1
            else:
                cur.close()
                return consulta
            cur.close()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================