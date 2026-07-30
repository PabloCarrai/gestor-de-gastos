#   Importacion de los modulos necesarios
import tkinter as tk
from tkinter import ttk

from tkcalendar import DateEntry
from config import ruta_categorias

# from tkinter import messagebox as ms
# from models.funciones_auxiliares import validar_formulario
# from models.funciones_auxiliares import vaciar_entradas
# from models.funciones_db import GestorDB
# from config import ruta_db
# from config import ruta_categorias
# from views.ventanadb import VentanaSecundaria


class VentanaIngresoDatosDetallada:
    """ """

    def __init__(self):
        #   Ventana principal
        self.ventana_principal = tk.Toplevel()
        #   Titulo de la ventana
        self.ventana_principal.title("Carga de Gastos")
        self.lbf_ventana_principal = tk.LabelFrame(
            self.ventana_principal, text="Detalle"
        )
        self.lbf_ventana_principal.grid(row=0, column=0, padx=10, pady=10)

        self.lbl_calendarioinicio = tk.Label(
            self.lbf_ventana_principal, text="Fecha Inicio:"
        )
        self.lbl_calendarioinicio.grid(row=0, column=0, padx=10, pady=10)

        self.dte_calendarioinicio = DateEntry(
            self.lbf_ventana_principal, date_pattern="dd/mm/yyyy"
        )
        self.dte_calendarioinicio.grid(row=0, column=1, padx=10, pady=10)

        self.lbl_calendariofin = tk.Label(self.lbf_ventana_principal, text="Fecha Fin:")
        self.lbl_calendariofin.grid(row=2, column=0, padx=10, pady=10)

        self.dte_calendariofin = DateEntry(
            self.lbf_ventana_principal, date_pattern="dd/mm/yyyy"
        )
        self.dte_calendariofin.grid(row=2, column=1, padx=10, pady=10)

        self.lbl_categorias = tk.Label(self.lbf_ventana_principal, text="Categoria")
        self.lbl_categorias.grid(row=3, column=0, padx=10, pady=10)

        self.cb_categorias = ttk.Combobox(
            self.lbf_ventana_principal,
            values=self.devolver_categorias(),
            state="readonly",
        )
        self.cb_categorias.grid(row=3, column=1, padx=10, pady=10)

        self.lbl_descripcion = tk.Label(self.lbf_ventana_principal, text="Descripcion")
        self.lbl_descripcion.grid(row=4, column=0, padx=10, pady=10)

        self.stv_descripcion = tk.StringVar()

        self.ent_descripcion = tk.Entry(
            self.lbf_ventana_principal, textvariable=self.stv_descripcion
        )
        self.ent_descripcion.grid(row=4, column=1, padx=10, pady=10)

    def devolver_categorias(self):
        try:
            with open(ruta_categorias, "r", encoding="utf-8") as archivo:
                items = [
                    linea.strip().title() for linea in archivo if linea.strip().title()
                ]
                return items
        except FileNotFoundError:
            print("Hay problemas con el archivo")
