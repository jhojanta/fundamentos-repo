"""Validaciones.py - Reglas de formato del DNI y los folios."""


def es_numerico(cadena):
    """True si la cadena tiene solo caracteres entre '0' y '9' (cadena vacia: False)."""
    if cadena == "":
        return False
    for caracter in cadena:
        if not ("0" <= caracter <= "9"):
            return False
    return True


def datos_validos(dni, folios_texto):
    """Registro valido: DNI de 8 digitos y folios como entero mayor a 0.
    Los folios llegan como texto para rechazar 'dos' sin que el programa falle."""
    return (
        len(dni) == 8
        and es_numerico(dni)
        and es_numerico(folios_texto)
        and int(folios_texto) > 0
    )
