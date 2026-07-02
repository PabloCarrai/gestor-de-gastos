#   Importacion de los modulos necesarios
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms


class VentanaListarDatos:
    """
    Clase para la venta que lista los gastos
    """

    def __init__(self):
        #   Ventana principal
        self.ventana_listado_gasto = tk.Toplevel()
        #   Titulo de la ventana
        self.ventana_listado_gasto.title("Listado de Gastos")
        self.ventana_listado_gasto.geometry("400x500")
        self.lbl_detalle_listado_gasto = tk.LabelFrame(
            self.ventana_listado_gasto, text="Detalle"
        )
        self.lbl_detalle_listado_gasto.grid(column=0, row=0, padx=10, pady=10)
        self.txt_prueba = tk.Label(self.lbl_detalle_listado_gasto, text="Probando")
        self.txt_prueba.grid(column=0, row=1, padx=10, pady=10)

        columnas = ("Nombre", "Edad", "Cargo")
        self.tv_listado_datos = ttk.Treeview(
            self.lbl_detalle_listado_gasto, columns=columnas, show="headings"
        )
        self.tv_listado_datos.grid(column=0, row=1, padx=10, pady=10)
        for columna in columnas:
            self.tv_listado_datos.heading(columna, text=columna)
            self.tv_listado_datos.column(columna, anchor=tk.CENTER)
