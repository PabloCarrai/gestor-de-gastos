import sys
import os
import tkinter as tk

# Agrega la carpeta padre al sistema de rutas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
#   Importo la ruta de la db, y la ruta del archivo que crea la tabla productos
from config import ruta_db, ruta_sql, ruta_dump

#   Importo la clase que gestiona la db
from core.archivo_db_gestor import GestorArchivoDb


def crear_db():
    db = GestorArchivoDb(ruta_db, ruta_sql, ruta_dump)
    db.crear_archivo_db()
    db.correr_sql()


def eliminar_db():
    db = GestorArchivoDb(ruta_db, ruta_sql, ruta_dump)
    db.eliminar_archivo_db()


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


