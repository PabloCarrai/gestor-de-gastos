import tkinter as tk
from views.ventanaprincipal import VentanaPrincipal


def ventana():
    #   Aca llamo a la ventana principal
    root = tk.Tk()
    ventana = VentanaPrincipal(root)
    root.mainloop()


def main():
    ventana()


if __name__ == "__main__":
    main()
