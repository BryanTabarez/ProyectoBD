<<<<<<< HEAD
from logica.Cama import Cama

class DaoCama():

    def __init__(self, conexion):
        self.conn = conexion

    def guardarCama(self, c):
        try:
            #Abrir un cursor para realizar operaciones con la base de datos
            cur = self.conn.cursor()

            cur.execute("INSERT INTO Cama (estado, descripcion, codigo_area)
            VALUES (%s, %s, %s), (c.get_estado(), c.get_descripcion(),
            c.get_cod_area()))

            # Cerrar el cursor
            cur.close()

            # Hacer que los cambios en la base de datos sean permanentes
            self.conn.commit()

    def borrarCama(self, id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM Cama WHERE num_cama = %s", (id,))
        cur.close()
        self.conn.commit()

    def consultarCama(self, id):
        try:
            cur = self.conn.cursor()
            sqlConsulta = """SELECT * FORM Cama NATURAL JOIN Area WHERE num_cama = %s"""
            cur.execute()(sqlConsulta, (id,))
            consulta = cur.fetchone()
            if consulta is None:
=======
# -*- coding: utf-8 -*-
>>>>>>> a888028e12e4810ec34a2e033fa6c9247a6273cb
