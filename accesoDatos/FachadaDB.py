import psycopg2

# FALTA IMPLEMENTAR CONTROL DE ERRORES y EXCEPCIONES

conn = None
cur = None


#  Conectarse a la base de datos
def conectar():
    global conn
    global cur
    conn = psycopg2.connect("dbname=clinica user=bryanstm")
    print("CONEXION ESTABLECIDA")

    # Abrir un cursor para realizar las operaciones con la base de datos
    cur = conn.cursor()
    return cur


# Hacer que los cambios en la base de datos sean permanentes
def guardar_cambios():
    conn.commit()


# Cerrar la comunicacion con la base de datos
def cerrar_conexion():
    cur.close()
    conn.close()
    print("CONEXION CERRADA")