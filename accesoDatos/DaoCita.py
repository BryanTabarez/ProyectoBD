#from logica import Cita


class DaoCita():
    """Clase DaoCita"""

    def __init__(self, conexion):
        self.conn = conexion

    #============================== CREATE ====================================
    def guardarCita(self, cita):
        try:
            cur = self.conn.cursor()

            cur.execute("INSERT INTO Cita (id_horario,numero_historia,tipo_solicitud) VALUES (%s, %s, %s)",
                (cita.get_id_horario(), cita.get_numero_historia(), cita.get_tipo_solicitud()))

            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================
    #============================== DELETE ====================================
    def cancelarCita(self, id_horario):
        try:
            cur = self.conn.cursor()

            cur.execute("DELETE FROM Cita WHERE id_horario = %s", (id_horario,))

            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e

    #============================== READ ======================================
    
    def listarCitasPaciente(self, id_paciente):
        try:
            cur = self.conn.cursor()
            cur.execute("""SELECT Cita.id_horario, Persona.nombre ,Horario_Consulta.fecha_hora
            FROM Cita 
            NATURAL JOIN Historia_Clinica  
            NATURAL JOIN Horario_Consulta
            JOIN Medico ON Horario_Consulta.id_medico = Medico.identificacion
            JOIN Persona ON Persona.identificacion = Medico.identificacion
            WHERE Historia_Clinica.id_paciente = %s """,
            (id_paciente,))

            consulta = cur.fetchall()
            if consulta is None:
                cur.close()
                return 1
            else:
                cur.close()
                return consulta

            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    # #============================== READ ======================================
    # # CONSULTA UN AREA PARTICULAR
    # def consultarArea(self, codigo):
    #     try:
    #         cur = self.conn.cursor()
    #         cur.execute("SELECT * FROM Area WHERE codigo = %s",
    #             (codigo,))

    #         consulta = cur.fetchone()
    #         if consulta is None:
    #             cur.close()
    #             return 1
    #         else:
    #             areaConsultada = Area(consulta[0], consulta[1], consulta[2])
    #             cur.close()
    #             return areaConsultada

    #         cur.close()
    #         self.conn.commit()
    #         return 0
    #     except Exception as e:
    #         cur.close()
    #         self.conn.reset()
    #         return e
    # #==========================================================================

    # #============================== UPDATE ====================================
    # def modificarArea(self, area):
    #     try:
    #         cur = self.conn.cursor()
    #         sqlUpdate = """UPDATE Area SET nombre = %s, descripcion = %s
    #         WHERE codigo = %s"""
    #         cur.execute(sqlUpdate, (area.get_nombre_area(),
    #         area.get_descripcion(), area.get_codigo_area()))
    #         cur.close()
    #         self.conn.commit()
    #         return 0
    #     except Exception as e:
    #         cur.close()
    #         self.conn.reset()
    #         return e
    # #==========================================================================

    # #============================== DELETE ====================================
    # def borrarArea(self, codigoArea):
    #     try:
    #         cur = self.conn.cursor()

    #         cur.execute("DELETE FROM Area WHERE codigo = %s", (codigoArea,))

    #         cur.close()
    #         self.conn.commit()
    #         return 0
    #     except Exception as e:
    #         cur.close()
    #         self.conn.reset()
    #         return e
    # #==========================================================================
