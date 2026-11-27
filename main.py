"""Registro de Expediente - Mesa de Partes Digital (MPC)
main.py: punto de entrada; controla el flujo principal e interactua con el usuario.
"""

from persistencia import leer_desde_archivo
from expedientes import registrar_expediente


def mostrar_encabezado():
    print("=" * 50)
    print(" REGISTRO DE EXPEDIENTE - MESA DE PARTES DIGITAL")
    print("=" * 50)


def mostrar_cargo(registro):
    """Comprobante digital equivalente al cargo entregado en ventanilla."""
    print("\nExpediente registrado correctamente.")
    print("Codigo generado:", registro["codigo"])
    print("Fecha de ingreso:", registro["fecha"])
    print("Cargo digital emitido para:", registro["nombres"])


def mostrar_error():
    print("\nERROR: verifique que el DNI tenga 8 digitos numericos")
    print("y que la cantidad de folios sea un numero entero mayor a 0.")


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
            mostrar_cargo(registro)
        else:
            mostrar_error()

        continuar = input("\nDesea registrar otro expediente? (S/N): ").strip().upper()
        print()

    print("Fin del registro. Gracias.")


if __name__ == "__main__":
    main()

