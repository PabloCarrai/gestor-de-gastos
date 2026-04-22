from config import ruta_db
from core.archivo_db_gestor import crear_archivo_db


def main():
    print(crear_archivo_db(ruta_db))


if __name__ == "__main__":
    main()
