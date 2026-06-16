#   Importacion de los modulos necesarios
import tkinter as tk
from tkinter import ttk
from views.ventanaingresogastos import VentanaIngresoDatos


class VentanaPrincipal:

    def __init__(self):
        self.ventana = tk.Tk()

        self.ventana.title("Ventana Principal")
        self.ventana.geometry("200x200")

        self.lbl_principal = tk.LabelFrame(self.ventana, text="Accesos")
        self.lbl_principal.grid(column=0, row=0, padx=10, pady=10)

        self.btn_ingresar_gasto = tk.Button(
            self.lbl_principal, text="Ingresar Gasto", command=self.ingresar_gasto
        )
        self.btn_ingresar_gasto.grid(column=0, row=0, padx=10, pady=10)

        self.btn_ver_gasto = tk.Button(
            self.lbl_principal, text="Ver Gasto", command=self.ver_gasto
        )
        self.btn_ver_gasto.grid(column=0, row=1, padx=10, pady=10)

        self.btn_salir = tk.Button(self.ventana, text="Salir", command=self.salir)
        self.btn_salir.grid(column=0, row=1, padx=10, pady=10)

    def ingresar_gasto(self):
        self.ventana_ingreso = VentanaIngresoDatos()

    def ver_gasto(self):
        pass

    def salir(self):
        self.ventana.destroy()
