BEGIN TRANSACTION;
CREATE TABLE Gastos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha DATE DEFAULT CURRENT_DATE,
    descripcion TEXT NOT NULL,
    monto DECIMAL(10, 2) NOT NULL,
    categoria TEXT
);
INSERT INTO "Gastos" VALUES(1,'2026-04-23','Papa',34.6,'verduleria');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('Gastos',1);
COMMIT;
