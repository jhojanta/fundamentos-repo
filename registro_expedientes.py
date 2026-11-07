"""Registro de Expediente - Mesa de Partes Digital (MPC)
Commit 2: version mejorada con persistencia en archivo, validacion robusta,
codigo correlativo con ceros y ordenamiento de los registros.
"""

ARCHIVO = "expedientes.txt"
ANIO = 2026
SEPARADOR = "|"
CAMPOS = ["codigo", "dni", "nombres", "tipo", "asunto", "folios"]


# ---------- Validaciones ----------
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


# ---------- Persistencia ----------
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


# ---------- Logica de expedientes ----------
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


def registrar_expediente(registros, dni, nombres, tipo, asunto, folios_texto):
    """Valida, genera el codigo, guarda y ordena. Devuelve el registro o None."""
    if not datos_validos(dni, folios_texto):
        return None

    numero = siguiente_numero(registros, ANIO)
    registro = {
        "codigo": f"{ANIO}-{numero:04d}",
        "dni": dni,
        "nombres": nombres,
        "tipo": tipo,
        "asunto": asunto,
        "folios": int(folios_texto),
    }
    registros.append(registro)
    registros.sort(key=lambda r: r["codigo"])
    guardar_en_archivo(registro)
    return registro


# ---------- Programa principal ----------
def mostrar_encabezado():
    print("=" * 50)
    print(" REGISTRO DE EXPEDIENTE - MESA DE PARTES DIGITAL")
    print("=" * 50)


def main():
    registros = leer_desde_archivo()
    continuar = "S"

    while continuar == "S":
        mostrar_encabezado()
        dni = input("Ingrese DNI (8 digitos numericos): ").strip()
        nombres = input("Ingrese Nombres y Apellidos: ").strip()
        tipo = input("Ingrese Tipo de documento (FUT, Carta, Oficio): ").strip()
        asunto = input("Ingrese Asunto del tramite: ").strip()
        folios = input("Ingrese cantidad de folios: ").strip()

        registro = registrar_expediente(registros, dni, nombres, tipo, asunto, folios)

        if registro is not None:
            print("\nExpediente registrado correctamente.")
            print("Codigo generado:", registro["codigo"])
            print("Cargo digital emitido para:", registro["nombres"])
        else:
            print("\nERROR: verifique que el DNI tenga 8 digitos numericos")
            print("y que la cantidad de folios sea un numero entero mayor a 0.")

        continuar = input("\nDesea registrar otro expediente? (S/N): ").strip().upper()
        print()

    print("Fin del registro. Gracias.")


if __name__ == "__main__":
    main()
