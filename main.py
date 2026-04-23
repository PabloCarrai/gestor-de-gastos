#   Importo la ruta de la db, y la ruta del archivo que crea la tabla productos
from config import ruta_db, ruta_sql, ruta_dump

#   Importo la clase que gestiona la db
from core.archivo_db_gestor import GestorArchivoDb


def crear_db():
    db = GestorArchivoDb(ruta_db, ruta_sql, ruta_dump)
    db.crear_archivo_db()
    db.correr_sql()


def hacer_dump():
    db = GestorArchivoDb(ruta_db, ruta_sql, ruta_dump)
    db.hacer_dump_db()


def main():
    # crear_db()
    hacer_dump()


if __name__ == "__main__":
    main()
