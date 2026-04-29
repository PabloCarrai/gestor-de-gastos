import tkinter as tk

#   Importo la ruta de la db, y la ruta del archivo que crea la tabla productos
from config import ruta_db, ruta_sql, ruta_dump

#   Importo la clase que gestiona la db
from core.archivo_db_gestor import GestorArchivoDb

from views.ventanaprincipal import VentanaPrincipal


def crear_db():
    db = GestorArchivoDb(ruta_db, ruta_sql, ruta_dump)
    db.crear_archivo_db()
    db.correr_sql()


def hacer_dump():
    db = GestorArchivoDb(ruta_db, ruta_sql, ruta_dump)
    db.hacer_dump_db()


def obtener_dump_mas_nuevo():
    db = GestorArchivoDb(ruta_db, ruta_sql, ruta_dump)
    return db.obtener_dump_mas_actual()


def hacer_restore_dump():
    db = GestorArchivoDb(ruta_db, ruta_sql, ruta_dump)
    return db.restaurar_dump_mas_nuevo()


def eliminar_dump():
    db = GestorArchivoDb(ruta_db, ruta_sql, ruta_dump)
    return db.eliminar_dump_viejos()


def ventana():
    root = tk.Tk()
    ventana = VentanaPrincipal(root)
    root.mainloop()


def main():
    ventana()


if __name__ == "__main__":
    main()
