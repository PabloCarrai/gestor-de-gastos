import sqlite3
from sqlite3 import Error


class GestorDB:
    """
    Esta clase se encarga de la gestion de la db
    Pero mas que nada para los registros de
    insercion, eliminacion, edicion de la db con
    los registros de la db para los datos de la aplicacion
    """

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
