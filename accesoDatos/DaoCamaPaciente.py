from logica import Cama
from logica import Paciente


class DaoCamaPaciente():
    """Clase DaoCamaPaciente"""
    def __init__(self, conexion):
        self.conn = conexion

    #============================== CREATE ====================================
    def guardarCamaPaciente(self, num_cama, id_paciente, fecha):
        try:
            
            cur = self.conn.cursor()

            cur.execute("INSERT INTO Cama_Paciente VALUES (%s, %s, %s)",
                ( num_cama, id_paciente, fecha ))

            cur.close()
            self.conn.commit()
            return 0
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================
    #============================== READ ======================================
    # CONSULTA CAMA PACIENTE
    def consultarCamaPaciente(self, id):
        try:
            
            cur = self.conn.cursor()
            sqlConsulta = """ SELECT DISTINCT(num_cama) , nombre
            FROM cama_paciente 
            NATURAL JOIN cama 
            JOIN area ON area.codigo = cama.codigo_area WHERE id_paciente = %s  AND estado = %s """
            
            cur.execute(sqlConsulta, (id,False))
            consulta = cur.fetchall()

            if consulta is None:
                cur.close()
                return 1
            else:
                cur.close()
                return consulta
        except Exception as e:
            cur.close()
            self.conn.reset()
            return e
    #==========================================================================

    