import psycopg2

# FALTA IMPLEMENTAR CONTROL DE ERRORES y EXCEPCIONES


class FachadaDB():

    def obtenerConexion(self):
        #  Conectarse a la base de datos
        self.conn = psycopg2.connect("dbname=clinica user=bryanstm")
        print("CONEXION ESTABLECIDA")
        return self.conn

    # Cerrar la comunicacion con la base de datos
    def cerrarConexion(self):
        self.conn.close()
        print("CONEXION CERRADA")

    # Hacer que los cambios en la base de datos sean permanentes
    def guardar_cambios(self):
        self.conn.commit()