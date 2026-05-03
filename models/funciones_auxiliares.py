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
        return True
    except ValueError:
        return False


def validar_formulario(entradas, entrada):
    if (verificar_entradas_vacias(entradas)) and (validar_entradas_entero(entrada)):
        return True
    else:
        return False
