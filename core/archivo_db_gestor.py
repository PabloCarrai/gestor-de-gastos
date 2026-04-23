from pathlib import Path
import sqlite3
from datetime import datetime


class GestorArchivoDb:
    def __init__(self, archivo, sql, dump):
        self.archivo = archivo
        self.sql = sql
        self.dump = dump

    def crear_archivo_db(self):
        """
        Revisa si el archivo existe,
        Si existe no hace nada.
        Si no existe lo crea vacio
        """

        #   Path del archivo .db
        archivo = Path(self.archivo)
        try:
            #   Reviso si el archivo existe
            if not archivo.exists():
                #   Sino existe lo creo
                archivo.touch()
            else:
                return f"El archivo ya existe"
        except Exception as e:
            return f"Ocurrio un error inesperado: {e}"

    def eliminar_archivo_db(self):
        """
        Intenta eliminar el archivo, sino existe no hace nada
        """
        archivo = Path(self.archivo)
        try:
            archivo.unlink()
            return f"Archivo eliminado con exito"
        except FileNotFoundError:
            return f"El archivo no existia, no se hizo nada"
        except PermissionError:
            return f"No tienes permisos para borrar el archivo"
        except Exception as e:
            return f"Ocurrio un error: {e}"

    def leer_sql(self):
        """
        Aca agarro el archivo sql, lo abro lo leo y devuelvo
        su contenido.
        """
        with open(self.sql, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            return contenido

    def correr_sql(self):
        try:
            sql = self.leer_sql()
            conexion = sqlite3.connect(self.archivo)
            cursor = conexion.cursor()
            cursor.execute(sql)
            conexion.commit()
            #   Si hay algun error aviso
        except sqlite3.Error as e:
            return f"Error Sqlite: {e}"
        finally:
            #   Si la conexion esta abierta la cerramos
            if conexion:
                conexion.close()
                print("Conexion Cerrada")

    def hacer_dump_db(self):
        ahora = datetime.now().strftime("%Y-%m-%d_%H-%M")
        archivo = f"{self.dump}/backup_{ahora}.sql"
        conexion = sqlite3.connect(self.archivo)
        with open(archivo, "w") as f:
            for linea in conexion.iterdump():
                f.write(f"{linea}\n")
        conexion.close()
        print(f"Dump guardado como {self.dump}")
