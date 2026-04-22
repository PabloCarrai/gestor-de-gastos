from pathlib import Path


def crear_archivo_db(archivo):
    """
    Revisa si el archivo existe,
    Si existe no hace nada.
    Si no existe lo crea vacio
    """

    ruta = Path(archivo)
    if not ruta.exists():
        ruta.touch()
        return f"Archivo {ruta} Creado"
    else:
        return f"El archivo ya existe"
