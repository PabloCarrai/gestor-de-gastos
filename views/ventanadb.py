import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms
from database.db_Gestor import crear_db, eliminar_db


class VentanaSecundaria(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Gestion de la db")
        self.geometry("180x300")
        self.lbf_principal = tk.LabelFrame(self, text="ABM-DB")
        self.lbf_principal.grid(column=0, row=0, padx=10, pady=10)

        self.btn_crear_db = tk.Button(
            self.lbf_principal, text="Crear DB", command=self.crear_db
        )
        self.btn_crear_db.grid(column=0, row=0, padx=10, pady=10)

        self.btn_eliminar_db = tk.Button(
            self.lbf_principal, text="Eliminar DB", command=self.eliminar_db
        )
        self.btn_eliminar_db.grid(column=0, row=1, padx=10, pady=10)

        self.btn_hacer_dump = tk.Button(self.lbf_principal, text="Hacer Dump DB")
        self.btn_hacer_dump.grid(column=0, row=2, padx=10, pady=10)

        self.btn_salir = tk.Button(self, text="Salir", command=self.salir)
        self.btn_salir.grid(column=0, row=1, padx=10, pady=10)

    def salir(self):
        self.destroy()

    def crear_db(self):
        crear_db()
        ms.showinfo("Ok", "Archivo sqlite de la db Creado")

    def eliminar_db(self):
        respuesta = ms.askyesno(
            "Confirmacion", "Esta seguro de querer eliminar la db actual?"
        )
        if respuesta:
            eliminar_db()
            ms.showinfo("Ok", "Archivo de la db sqlite Eliminado")
        else:
            ms.showinfo("Ok", "Aca no paso nada")
