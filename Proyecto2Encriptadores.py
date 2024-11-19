from Proyecto2Modulos import *

def desencriptar(caract_encrip:int, llave_priv:tuple):
    a = llave_priv[0]
    b = llave_priv[1]

    valorOriginal = pow(caract_encrip, a, b)
    return chr(valorOriginal)
