from Modulos import *
from Rsa import *

def encriptador(mensaje:int, llaves:tuple) -> int:
    a = llaves[0]
    b = llaves[1]

    return pow(mensaje, a, b)


def rsaFunction(mensaje:int) -> None:

    inferior:int = 329
    
    superior:int = 923

    llaves:tuple = generar_llaves(inferior,superior)

    encriptado:int = encriptador(mensaje,llaves[0])
    print(f"encriptado: {encriptado}\n")
        
    descriptado:int = encriptador(encriptado,llaves[1])

    print(f"desincriptado: {descriptado}n")


def stringMessage(mensaje:str) -> None:
   
    inferior:int = 329
    
    superior:int = 923

    llaves:tuple = generar_llaves(inferior,superior)

    caracteresEncriptados:list = [encriptador(ord(caracter),llaves[0]) for caracter in mensaje ]

    print(f"{caracteresEncriptados}\n")

    caracteresDesincriptados:list = [chr(encriptador(caracter,llaves[1])) for caracter in caracteresEncriptados ]
    
    print(f"{"".join(caracteresDesincriptados)}\n")

