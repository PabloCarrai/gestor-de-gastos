import tkinter as tk
from tkinter import ttk


class VentanaPrincipal:
    def __init__(self, root):
        self.ventana_principal = root
        self.ventana_principal.title("Carga de Gastos")

        self.lbf_detalles = tk.LabelFrame(self.ventana_principal, text="Detalle")
        self.lbf_detalles.grid(column=0, row=0, padx=10, pady=10)

        self.lbl_descripcion = tk.Label(self.lbf_detalles, text="Descripcion:  ")
        self.lbl_descripcion.grid(column=0, row=0, padx=10, pady=10)

        self.stv_descripcion = tk.StringVar()
        self.txt_descripcion = tk.Entry(
            self.lbf_detalles, textvariable=self.stv_descripcion
        )
        self.txt_descripcion.grid(column=1, row=0, padx=10, pady=10)

        self.lbl_monto = tk.Label(self.lbf_detalles, text="Monto:  ")
        self.lbl_monto.grid(column=0, row=1, padx=10, pady=10)

        self.stv_monto = tk.StringVar()
        self.txt_monto = tk.Entry(self.lbf_detalles, textvariable=self.stv_monto)
        self.txt_monto.grid(column=1, row=1, padx=10, pady=10)

        self.lbl_categoria = tk.Label(self.lbf_detalles, text="Categoria:  ")
        self.lbl_categoria.grid(column=0, row=2, padx=10, pady=10)

        categorias = ["Otros", "Comida", "Gustos"]
        self.cb_categoria = ttk.Combobox(
            self.lbf_detalles, values=categorias, state="readonly"
        )
        self.cb_categoria.set("Elija una opcion")
        self.cb_categoria.grid(column=1, row=2, padx=10, pady=10)

        self.btn_agregar = tk.Button(self.lbf_detalles, text="Agregar")
        self.btn_agregar.grid(column=0, row=4, padx=10, pady=10)

        self.btn_cancelar = tk.Button(self.lbf_detalles, text="Cancelar")
        self.btn_cancelar.grid(column=1, row=4, padx=10, pady=10)
