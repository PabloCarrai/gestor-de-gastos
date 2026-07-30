import tkinter as tk


def verificar_entradas_vacias(entradas):
    """
    Recibo una lista de las entradas.
    Valido que no esten vacias
    Si estan vacias devuelvo False, sino True
    """
    for entrada in entradas:
        if not entrada.get().strip():
            return False
        else:
            return True


def validar_entradas_entero(entrada):
    """
    Obtengo una entrada y reviso si es un numero
    Si es un numero devuelvo el mismo,
    Sino devuelvo False
    """
    valor = entrada.get()
    try:
        valor_entero = float(valor)
        if type(valor_entero) == float:
            return True
        else:
            return False
    except ValueError:
        print("Error con el valor, no es un numero")


def validar_formulario(entradas, entrada):
    """
    Devuelve true o false.
    En el caso de que devuelva True es porque
    los elementos del formularios esta ok
    """
    if (verificar_entradas_vacias(entradas)) and (validar_entradas_entero(entrada)):
        return True
    else:
        return False


def vaciar_entradas(entradas):
    """
    Esta funcion recibe una lista de entrys
    y me encargo de vaciarlo
    """
    for entrada in entradas:
        entrada.delete(0, tk.END)


def verificar_opciones_seleccionada(combobox):
    seleccion = combobox.get()
    if seleccion:
        return seleccion
    else:
        return False
