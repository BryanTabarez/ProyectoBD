

class DaoArea():

    def __init__(self, conexion):
        self.conn = conexion

    def guardarArea(self, a):
        cur = self.conn.cursor()

        cur.execute("INSERT INTO Area(nombre, descripcion) VALUES (%s, %s)",
            (a.get_nombre_area(), a.get_descripcion()))

        cur.close()
        self.conn.commit()

    def borrarArea(self, codigo):
        cur = self.conn.cursor()

        cur.execute("DELETE FROM Area WHERE codigo = %s", (codigo,))

        cur.close()
        self.conn.commit()

    def consultarArea(self, codigo):
        cur = self.conn.cursor()

        cur.close()
        self.conn.commit()