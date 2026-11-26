"""expedientes.py - Logica de expedientes: codigo, ordenamiento y registro."""

from validaciones import datos_validos
from persistencia import guardar_en_archivo

ANIO = 2026


def siguiente_numero(registros, anio):
    """Mayor correlativo ya registrado en el anio, mas 1.
    Asi, al reiniciar el programa no se repite un codigo."""
    prefijo = str(anio) + "-"
    numeros = [
        int(r["codigo"].split("-")[1])
        for r in registros
        if r["codigo"].startswith(prefijo)
    ]
    return max(numeros, default=0) + 1


def generar_codigo(registros, anio=ANIO):
    """Codigo correlativo con formato AAAA-NNNN (ej. 2026-0001)."""
    return f"{anio}-{siguiente_numero(registros, anio):04d}"


def ordenar_expedientes(registros):
    """Ordena la lista de expedientes por codigo (en el mismo lugar)."""
    registros.sort(key=lambda r: r["codigo"])


def registrar_expediente(registros, dni, nombres, tipo, asunto, folios_texto):
    """Valida, genera el codigo, guarda y ordena. Devuelve el registro o None."""
    if not datos_validos(dni, folios_texto):
        return None

    registro = {
        "codigo": generar_codigo(registros),
        "dni": dni,
        "nombres": nombres,
        "tipo": tipo,
        "asunto": asunto,
        "folios": int(folios_texto),
    }
    registros.append(registro)
    ordenar_expedientes(registros)
    guardar_en_archivo(registro)
    return registro

