from config import ruta_db
from core.archivo_db_gestor import GestorArchivoDb


def main():
    db = GestorArchivoDb(ruta_db)   
    db1= db.crear_archivo_db()
    print(db1)


if __name__ == "__main__":
    main()
