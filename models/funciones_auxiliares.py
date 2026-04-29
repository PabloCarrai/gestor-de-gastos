from tkinter import messagebox as ms


def verificar_vacios(entradas):
    for entrada in entradas:
        if not entrada.get().strip():
            ms.showerror("Error", "Hay entradas vacias")
        else:
            #   Aca tendria que llamar a la db e insertar los registros
            print(f"{entrada.get()}")
