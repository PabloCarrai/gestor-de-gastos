import sqlite3
from sqlite3 import Error


class GestorDB:
    """
    Esta clase se encarga de la gestion de la db
    Pero mas que nada para los registros de
    insercion, eliminacion, edicion de la db con
    los registros de la db para los datos de la aplicacion
    """

    def __init__(self, db_name):
        self.db = db_name

    def insertar(self, sql_insert, datos):
        try:
            with sqlite3.connect(self.db) as conexion:
                cursor = conexion.cursor()
                cursor.execute(sql_insert, datos)
                print(f"Datos ingresados {datos}")
        except sqlite3.Error as e:
            print(f"Ocurrio un error general de Sqlite: {e}")
        except Exception as e:
            print(f"Ocurrio un error inesperado fuera  de la db: {e}")
