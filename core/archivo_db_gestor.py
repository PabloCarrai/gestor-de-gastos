from pathlib import Path


class GestorArchivoDb:
    def __init__(self, archivo):
        self.archivo = archivo

    def crear_archivo_db(self):
        """
        Revisa si el archivo existe,
        Si existe no hace nada.
        Si no existe lo crea vacio
        """

        archivo = Path(self.archivo)
        try:
            if not archivo.exists():
                archivo.touch()
                return f"Archivo {archivo} Creado"
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
