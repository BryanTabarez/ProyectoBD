from logica.Enfermera import Enfermera


class DaoEnfermera():
    """Clase Dao Enfermera"""
    def __init__(self, conexion):
        self.conn = conexion

    #============================== CREATE ====================================
    def guardarEnfermera(self, e):
        try:
            cur = self.conn.cursor()
            #guardar persona
            cur.execute("INSERT INTO Persona VALUES (%s, %s, %s, %s)",
                (e.get_identificacion(), e.get_nombre(), e.get_direccion(),
                    e.get_telefono()))

            #guardar empleado
            cur.execute("INSERT INTO Empleado VALUES (%s, %s, %s, %s, %s)",
                (e.get_identificacion(), e.get_codigo_area(), e.get_email(),
                    e.get_salario(), e.get_id_jefe()))

            #guardar enfermera
            cur.execute("INSERT INTO Enfermera VALUES (%s, %s)",
                (e.get_identificacion(), e.get_anhos_experiencia()))

            #guardar habilidades enfermera
            habilidades = e.get_habilidades()
            for i in habilidades:
                cur.execute("INSERT INTO Enfermera_Habilidad VALUES (%s, %s)",
                    (e.get_identificacion(), i))

            cur.close()
            self.conn.commit()
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== READ ======================================
    def consultarEnfermera(self, id):
        try:
            cur = self.conn.cursor()
            sqlConsulta = """SELECT * FROM Persona NATURAL JOIN EMPLEADO
            NATURAL JOIN ENFERMERA WHERE identificacion = %s"""

            cur.execute(sqlConsulta, (id,))
            consulta = cur.fetchone()
            if consulta is None:
                print("La consulta no arrojo resultados")
                cur.close()
                return 0
            else:
                cur.execute("""SELECT habilidad FROM Habilidades_Enfermera WHERE
                id_enfermera = %s""", (id,))
                habilidades = cur.fetchall()
                enfermera = Enfermera(consulta[0], consulta[1], consulta[2],
                    consulta[3], consulta[4], consulta[5], consulta[6],
                    consulta[7], consulta[8], habilidades)
                cur.close()
                return enfermera
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== UPDATE ====================================
    # FALTA  PROBAR/CORREGIR ESTO
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
    #==========================================================================

    #============================== DELETE ====================================
    # OJO PENDIENTE REVISION
    def borrarEnfermera(self, id):
        """Para borrar una enfermera -> Eliminar registros Enfermera y Empleado
        Dejar Persona si es necesario"""
        try:
            cur = self.conn.cursor()
            cur.execute("""DELETE FROM Enfermera_habilidad WHERE
            id_enfermera = %s""", (id,))
            cur.execute("DELETE FROM Enfermera WHERE identificacion=%s", (id,))
            cur.execute("DELETE FROM Empleado WHERE identificacion = %s", (id,))
            cur.execute("DELETE FROM Persona WHERE identificacion = %s", (id,))
            cur.close()
            self.conn.commit()
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================
