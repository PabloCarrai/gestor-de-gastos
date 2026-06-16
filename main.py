import tkinter as tk
from views.ventanaprincipal import VentanaPrincipal


def ventana():
    app = VentanaPrincipal()
    app.ventana.mainloop()


def main():
    ventana()


if __name__ == "__main__":
    main()
