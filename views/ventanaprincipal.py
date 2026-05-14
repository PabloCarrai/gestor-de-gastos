#   Importacion de los modulos necesarios
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms
from models.funciones_auxiliares import validar_formulario
from models.funciones_auxiliares import vaciar_entradas
from models.funciones_db import GestorDB
from config import ruta_db
from views.ventanadb import VentanaSecundaria


class VentanaPrincipal:
    """
    Clase para el dibujo de la ventana principal
    """

    def __init__(self, root):
        #   Ventana principal
        self.ventana_principal = root
        #   Titulo de la ventana
        self.ventana_principal.title("Carga de Gastos")
        #   LabelFrame de la ventana
        self.lbf_detalles = tk.LabelFrame(self.ventana_principal, text="Detalle")
        #   Su ubicacion
        self.lbf_detalles.grid(column=0, row=0, padx=10, pady=10)
        #   Etiqueta para la descripcion
        self.lbl_descripcion = tk.Label(self.lbf_detalles, text="Descripcion:  ")
        #   Su posicion en la ventana
        self.lbl_descripcion.grid(column=0, row=0, padx=10, pady=10)
        #   Stringvar de la entrada descripcion
        self.stv_descripcion = tk.StringVar()
        #   Entrada de la descripcion
        self.txt_descripcion = tk.Entry(
            self.lbf_detalles, textvariable=self.stv_descripcion
        )
        #   Su ubicacion
        self.txt_descripcion.grid(column=1, row=0, padx=10, pady=10)
        #   Etiqueta para el monto
        self.lbl_monto = tk.Label(self.lbf_detalles, text="Monto:  ")
        #   Su ubicacion
        self.lbl_monto.grid(column=0, row=1, padx=10, pady=10)
        #   Stringvar para el monto
        self.stv_monto = tk.StringVar()
        #   Entrada para el monto
        self.txt_monto = tk.Entry(self.lbf_detalles, textvariable=self.stv_monto)
        #   Su ubicacion
        self.txt_monto.grid(column=1, row=1, padx=10, pady=10)
        #   Etiqueta para categoria
        self.lbl_categoria = tk.Label(self.lbf_detalles, text="Categoria:  ")
        #   Ubicacion para categoria
        self.lbl_categoria.grid(column=0, row=2, padx=10, pady=10)
        #   Categorias del combobox
        categorias = ["Otros", "Comida", "Gustos"]
        #   El combobox
        self.cb_categoria = ttk.Combobox(
            self.lbf_detalles, values=categorias, state="readonly"
        )
        #   Seleccion por defecto
        self.cb_categoria.current(0)
        # Su ubicacion
        self.cb_categoria.grid(column=1, row=2, padx=10, pady=10)
        #   Boton Agregar
        self.btn_agregar = tk.Button(
            self.lbf_detalles, text="Agregar", command=self.agregar
        )
        #   Su ubicacion
        self.btn_agregar.grid(column=0, row=4, padx=10, pady=10)
        #   Boton Cancelar
        self.btn_cancelar = tk.Button(
            self.lbf_detalles, text="Cancelar", command=self.salir
        )
        #   Ubicacion del boton Cancelar
        self.btn_cancelar.grid(column=1, row=4, padx=10, pady=10)

        #   Boton Db
        self.btn_db = tk.Button(
            self.ventana_principal, text="Db", command=self.mostrar_ventana_db
        )
        self.ventana_principal.bind("<Control-d>", self.mostrar_ocultar_boton_db)

    def mostrar_ocultar_boton_db(self, event=None):
        if self.btn_db.winfo_ismapped():
            self.btn_db.grid_forget()
        else:
            self.btn_db.grid(column=0, row=1, padx=10, pady=10)

    def mostrar_ventana_db(self):
        VentanaSecundaria()

    def agregar(self):
        #   Metodo para agregar la info.
        #   Valido con la funcion Validar_formulario
        if validar_formulario(
            [self.txt_descripcion, self.txt_monto, self.cb_categoria], self.txt_monto
        ):
            #   Genero una instancia del gesto de la db
            db = GestorDB(
                ruta_db,
                "insert into Gastos(descripcion,monto,categoria) values(?,?,?)",
                (
                    self.txt_descripcion.get(),
                    self.txt_monto.get(),
                    self.cb_categoria.get(),
                ),
            )
            #   Inserto los datos
            db.insertar()
            #   Vacio las entradas
            vaciar_entradas([self.txt_monto, self.txt_descripcion])
            #   Aviso de que se ingreso el registro
            ms.showinfo(
                "Registro insertado",
                f"Descripcion: {self.txt_descripcion.get()}, Monto: {self.txt_monto.get()}, Categoria: {self.cb_categoria.get()}",
            )
        else:
            #   Sino muestro que hubo problemas
            ms.showerror("Problemas", "Hay algun dato mal cargado o no valido.")

    def salir(self):
        #   Metodo para salir de la aplicacion
        self.ventana_principal.destroy()
