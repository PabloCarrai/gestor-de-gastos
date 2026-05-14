import tkinter as tk
from tkinter import ttk


class VentanaSecundaria(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Gestion de la db")
        self.geometry("300x300")
        self.lbf_principal = tk.LabelFrame(self, text="ABM-DB")
        self.lbf_principal.grid(column=0, row=0, padx=10, pady=10)
        self.txt_prueba = tk.Label(self.lbf_principal, text="Prueba")
        self.txt_prueba.grid(column=0, row=0, padx=10, pady=10)
