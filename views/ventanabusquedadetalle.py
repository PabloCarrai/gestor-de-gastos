#   Importacion de los modulos necesarios
import tkinter as tk
from tkinter import ttk

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
