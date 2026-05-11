from cliente import Cliente
from excepciones import ClienteInvalidoError
from servicio import ReservaSala
from reserva import Reserva

try:

    cliente1 = Cliente("Natalia", 123456, "3000000000")

    print(cliente1.mostrar_datos())

    cliente2 = Cliente("", 456, "3111111111")

except ClienteInvalidoError as e:

    print("Error:", e)
