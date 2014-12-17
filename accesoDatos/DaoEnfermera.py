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
            return 0
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
                cur.close()
                return 1
            else:
                cur.execute("""SELECT codigo, descripcion FROM Enfermera_habilidad JOIN
                    Habilidad ON codigo = habilidad WHERE id_enfermera = %s""", (id,))
                habilidades = cur.fetchall()
                enfermera = Enfermera(consulta[0], consulta[1], consulta[2],
                    consulta[3], consulta[4], consulta[5], consulta[6],
                    consulta[7], consulta[8], habilidades)
                cur.close()
                return enfermera
            cur.close()
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    #============================== UPDATE ====================================
    def modificarEnfermera(self, p):
        try:
            cur = self.conn.cursor()

            sqlUpdate1 = """UPDATE Persona SET nombre = %s, direccion = %s,
            telefono = %s WHERE identificacion = %s"""

            sqlUpdate2 = """UPDATE Empleado SET codigo_area = %s,
            email = %s, salario = %s, id_jefe = %s WHERE
            identificacion = %s"""

            sqlUpdate3 = "UPDATE Enfermera SET anos_experiencia = %s WHERE identificacion = %s"


            cur.execute(sqlUpdate1, (p.get_nombre(), p.get_direccion(),
            p.get_telefono(), p.get_identificacion()))

            cur.execute(sqlUpdate2, (p.get_codigo_area(),
            p.get_email(), p.get_salario(), p.get_id_jefe(), p.get_identificacion() ))

            cur.execute(sqlUpdate3, (p.get_anhos_experiencia(), p.get_identificacion() ))

            self.conn.commit()
            cur.close()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
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
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================