from Modulos import *
from Rsa import *

def encriptardor(mensaje:int, llaves:tuple):
    a = llaves[0]
    b = llaves[1]

    return pow(mensaje, a, b)


def rsaFunction(mensaje:int):

    inferior = 200
    
    superior = 300

    llaves = generar_llaves(inferior,superior)

    encriptado = encriptardor(mensaje,llaves[0])
    print(f"encriptado: {encriptado}")
        
    descriptado = encriptardor(encriptado,llaves[1])

    print(f"desincriptado: {descriptado}")

