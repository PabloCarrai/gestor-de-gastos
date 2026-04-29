from pathlib import Path
import sqlite3, os
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

    def obtener_dump_mas_actual(self):
        #   Objeto Path deldirectorio
        dir_path = Path(self.dump)
        #   Busco los *.sql
        archivos = sorted(dir_path.glob("backup_*.sql"))

        #   Si no hay archivos devuelvo None
        if archivos:
            archivo_reciente = archivos[-1].resolve()
            return str(archivo_reciente)

    def restaurar_dump_mas_nuevo(self):
        #   Aca restauro el ultimo dump al archivo .db
        try:
            #   Necesito boletear la db para que el dump ande
            if os.path.exists(self.archivo):
                os.remove(self.archivo)
            #   Conecto la db
            conexion = sqlite3.connect(self.archivo)
            #   Genero un cursor
            cursor = conexion.cursor()
            #   Leo el ultimo dump
            with open(self.obtener_dump_mas_actual(), "r", encoding="utf-8") as f:
                sql_script = f.read()
            #   Restauro el mismo
            cursor.executescript(sql_script)
            #   Hago efectivo el cambio
            conexion.commit()
            print(f"Restaurando {self.obtener_dump_mas_actual()} en db {self.archivo}")
            #   Si hay algun error aviso
        except sqlite3.Error as e:
            return f"Error Sqlite: {e}"
        finally:
            #   Si la conexion esta abierta la cerramos
            if conexion:
                conexion.close()
                print("Conexion Cerrada")

    def obtener_dump_menos_nuevos(self):
        #   Objeto Path deldirectorio
        dir_path = Path(self.dump)
        #   Obtengo la ruta absoluta de los dump
        archivos = sorted(dir_path.glob("backup_*.sql"))
        #   De esa lista quito el ultimo
        paths_antiguos = archivos[:-1]
        #   Me fijo si hay mucho mas archivos que 1
        if len(paths_antiguos) > 1:            
            try:
                for path in paths_antiguos:
                    #   Elimino esos archivos
                    path.unlink()
                    print("Archivos viejos eliminados")
            except OSError as e:
                print(f"Error al eliminar {path}: {e}")
        else:
            print("No hay archivos a eliminar")
