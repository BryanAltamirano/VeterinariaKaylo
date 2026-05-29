def validar_texto(texto):
    return texto.strip() != ""


def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) >= 10


def validar_edad(edad):
    return edad.isdigit() and int(edad) > 0


def validar_costo(costo):
    try:
        return float(costo) > 0
    except:
        return False