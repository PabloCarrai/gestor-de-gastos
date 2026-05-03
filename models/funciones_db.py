import sqlite3
from sqlite3 import Error


class GestorDB:
    def __init__(self, db_name, consulta, datos):
        self.db = db_name
        self.consulta = consulta
        self.datos = datos

    def insertar(self):
        with sqlite3.connect(self.db) as conexion:
            try:
                cursor = conexion.execute(self.consulta, self.datos)
                return cursor.fetchall()
            except Exception as e:
                print("Error, volviendo atras: {e}")
