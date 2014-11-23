import FachadaDB


def main():
    cur = FachadaDB.conectar()
    cur.execute("SELECT * FROM Medicamento;")
    FachadaDB.cerrar_conexion()

main()