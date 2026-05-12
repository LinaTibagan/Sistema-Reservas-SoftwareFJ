# Archivo principal para realizar pruebas del sistema
# y verificar el funcionamiento de las clases y excepciones.

from cliente import Cliente
from excepciones import (
    ClienteInvalidoError,
    guardar_error
)

from servicio import ReservaSala
from reserva import Reserva

print("\n--- INICIO DEL SISTEMA ---\n")

try:

    cliente1 = Cliente(
        "Natalia",
        123456,
        "3000000000"
    )

    print(cliente1.mostrar_datos())

    cliente2 = Cliente(
        "",
        456,
        "3111111111"
    )

except ClienteInvalidoError as e:

    print("Error:", e)

    guardar_error(e)

try:

    servicio1 = ReservaSala(2)

    reserva1 = Reserva(
        cliente1,
        servicio1
    )

    reserva1.confirmar()

    print(
        reserva1.mostrar_reserva()
    )

except Exception as e:

    print("Error:", e)

    guardar_error(e)

print("\n--- FIN DEL SISTEMA ---")