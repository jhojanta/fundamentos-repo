"""Persistencia.py - Lectura y escritura de expedientes en 'expedientes.txt'."""

ARCHIVO = "expedientes.txt"
SEPARADOR = "|"
CAMPOS = ["codigo", "dni", "nombres", "tipo", "asunto", "folios"]


def leer_desde_archivo():
    """Devuelve la lista de expedientes guardados (vacia si el archivo no existe)."""
    registros = []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    valores = linea.split(SEPARADOR)
                    registro = dict(zip(CAMPOS, valores))
                    registro["folios"] = int(registro["folios"])
                    registros.append(registro)
    except FileNotFoundError:
        pass
    return registros


def guardar_en_archivo(registro):
    """Agrega un expediente al final del archivo."""
    linea = SEPARADOR.join(str(registro[campo]) for campo in CAMPOS)
    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(linea + "\n")

