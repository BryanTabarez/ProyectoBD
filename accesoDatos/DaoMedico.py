from logica import Medico


class DaoMedico():

    def __init__(self, conexion):
        self.conn = conexion

    #============================== CREATE ====================================
    def guardarMedico(self, m):
        #Se guarda el medico con los siguientes atributos:
        """(identificacion, nombre, direccion, telefono, codigo_area, email,
        salario, id_jefe, especialidad, universidad, num_licencia)"""
        try:
            cur = self.conn.cursor()
            #guardar persona
            cur.execute("""INSERT INTO Persona (identificacion, nombre, direccion,
                telefono) VALUES (%s, %s, %s, %s)""", (m.get_identificacion(),
                m.get_nombre(), m.get_direccion(), m.get_telefono()))

            #guardar empleado
            cur.execute("""INSERT INTO Empleado (identificacion, codigo_area, email,
                salario, id_jefe) VALUES (%s, %s, %s, %s, %s)""", (m.get_identificacion(),
                m.get_codigo_area(), m.get_email(), m.get_salario(), m.get_id_jefe()))

            #guardar medico
            cur.execute("INSERT INTO Medico VALUES (%s, %s, %s, %s)",
                (m.get_identificacion(), m.get_especialidad(),
                m.get_universidad(), m.get_num_licencia()))

            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== READ ======================================
    def consultarMedico(self, id):
        try:
            cur = self.conn.cursor()
            sqlConsulta = """SELECT * FROM Persona NATURAL JOIN EMPLEADO
            NATURAL JOIN MEDICO WHERE identificacion = %s"""

            cur.execute(sqlConsulta, (id,))
            consulta = cur.fetchone()

            if consulta is None:
                cur.close()
                return 1
            else:
                # medico = Medico(consulta[0], consulta[1], consulta[2],
                #     consulta[3], consulta[4], consulta[5], consulta[6],
                #     consulta[7], consulta[8], consulta[9], consulta[10])
                # cur.close()
                return consulta
            cur.close()
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== UPDATE ====================================
    def modificarMedico(self, id, m):
        try:
            cur = self.conn.cursor()

            sqlUpdate1 = """UPDATE Persona SET nombre = %s, direccion = %s,
            telefono = %s WHERE identificacion = %s"""

            sqlUpdate2 = """UPDATE Empleado SET codigo_area = %s,
            salario = %s, id_jefe = %s WHERE
            identificacion = %s"""

            sqlUpdate3 = """UPDATE Medico SET especialidad = %s,
            universidad = %s, num_licencia = %s WHERE
            identificacion = %s"""

            cur.execute(sqlUpdate1, (m.get_nombre(), m.get_direccion(),
            m.get_telefono(), id, ))

            cur.execute(sqlUpdate2, (m.get_codigo_area(), m.get_email(),
            m.get_salario(), m.get_id_jefe(), id, ))

            cur.execute(sqlUpdate3, (m.get_especialidad(), m.get_universidad(),
                    m.get_num_licencia(), id))

            self.conn.commit()
            cur.close()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== DELETE ====================================
    def borrarMedico(self, id):
        """Para borrar una enfermera -> Eliminar registros Medico y Empleado
        Dejar Persona si es necesario"""
        try:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM Medico WHERE identificacion=%s", (id,))
            cur.execute("DELETE FROM Empleado WHERE identificacion = %s", (id,))

            sqlConsulta = "SELECT * FROM Paciente WHERE identificacion = %s"
            cur.execute(sqlConsulta, (id,))

            consulta = cur.fetchone()
            if consulta is None:
                cur.execute("DELETE FROM Persona WHERE identificacion = %s", (id,))
            self.conn.commit()
            
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================= AURELIO ====================================

    #================= OBTENER ESPECIALIDADES MEDICO ==========================

    def listarEspecialidades(self):
        try:
            cur = self.conn.cursor()
            sqlConsulta = """SELECT DISTINCT(especialidad) FROM Medico """

            cur.execute(sqlConsulta, (id,))
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

    


