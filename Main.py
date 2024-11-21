from Modulos import *
from Rsa import *


if __name__ == "__main__":

    if __name__ == "__main__":
        print("----RSA----")
        while True:
            try:
                inf = int(input("Primer número (límite inferior): "))
                sup = int(input("Segundo número (límite superior): "))
                
                if (inf >= 6 and sup > 38) and sup <= inf:
                    print("Error: Los valores son inválidos o no están dentro de los límites (6 ≤ inf < sup ≤ 38).")
                    continue
                
                mensaje = int(input("Mensaje a encriptar (número): "))
                if mensaje <= 0:
                    print("Error: El mensaje debe ser un número positivo. Intente de nuevo.")
                    continue
                
                rsaFunction(mensaje, inf, sup)
            except ValueError as e:
                print(f"Error de tipo de valor: {e}")
                continue
