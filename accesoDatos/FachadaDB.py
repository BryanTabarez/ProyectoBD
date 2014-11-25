import psycopg2

# FALTA IMPLEMENTAR CONTROL DE ERRORES y EXCEPCIONES


class FachadaDB():

    #  Conectarse a la base de datos
    def obtenerConexion(self):
        self.conn = psycopg2.connect("dbname=clinica user=bryanstm")
        print("CONEXION ESTABLECIDA")
        return self.conn

    # Cerrar la comunicacion con la base de datos
    def cerrarConexion(self):
        self.conn.close()
        print("CONEXION CERRADA")