from Modulos import *
from Rsa import *


if __name__ == "__main__":
  
    pruebas = [3242,953,90]

    for i in range(3):
        print(f"Prueba {i+1}: {pruebas[i]}")
        rsaFunction(pruebas[i])

