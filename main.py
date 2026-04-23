#   Importo la ruta de la db, y la ruta del archivo que crea la tabla productos
from config import ruta_db, ruta_sql

#   Importo la clase que gestiona la db
from core.archivo_db_gestor import GestorArchivoDb


def crear_db():
    db = GestorArchivoDb(ruta_db, ruta_sql)
    db.crear_archivo_db()
    db.correr_sql()


def main():
    crear_db()
    # print(ruta_sql)


if __name__ == "__main__":
    main()
