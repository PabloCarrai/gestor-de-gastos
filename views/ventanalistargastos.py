#   Importacion de los modulos necesarios
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms
from models.funciones_db import GestorDB


class VentanaListarDatos:
    """
    Clase para la ventana que lista los gastos
    """

    def __init__(self):
        #   Ventana principal
        self.ventana_listado_gasto = tk.Toplevel()
        #   Titulo de la ventana
        self.ventana_listado_gasto.title("Listado de Gastos")

        self.lbl_detalle_listado_gasto = tk.LabelFrame(
            self.ventana_listado_gasto, text="Detalle"
        )
        self.lbl_detalle_listado_gasto.grid(column=0, row=1, padx=10, pady=10)

        columnas = ("Fecha", "Descripcion", "Monto", "Categoria")
        self.tv_listado_datos = ttk.Treeview(
            self.lbl_detalle_listado_gasto, columns=columnas, show="headings"
        )
        self.tv_listado_datos.grid(column=0, row=1, padx=10, pady=10)
        for columna in columnas:
            self.tv_listado_datos.heading(columna, text=columna)
            self.tv_listado_datos.column(columna, anchor=tk.CENTER)

        self.btn_mostrar_datos = tk.Button(
            self.ventana_listado_gasto,
            text="Mostrar Info",
            command=self.cargar_registros,
        )
        self.btn_mostrar_datos.grid(column=0, row=5, padx=10, pady=10)

    def cargar_registros(self):
        pass


"""
    fecha DATE DEFAULT CURRENT_DATE,
    descripcion TEXT NOT NULL,
    monto DECIMAL(10, 2) NOT NULL,
    categoria TEXT
"""
