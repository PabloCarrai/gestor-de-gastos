import os

#   La carpeta actual del script
base_dir = os.path.dirname(os.path.abspath(__file__))
#   La ruta de data/db_gastos.db
ruta_db = os.path.join(base_dir, "data", "db_gastos.db")

#   Ruta a 1.sql
ruta_sql = os.path.join(base_dir, "sql", "1.sql")
#   Destino del dump de la db
ruta_dump = os.path.join(base_dir, "sql", "dump")