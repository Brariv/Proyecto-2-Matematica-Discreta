import random as rd


def mcd(x:int, y:int)->int:
    if x < y: 
        a = y
        b = x
    else:
        a = x
        b = y

    while b != 0: #Mientras b no sea 0, se continua el algoritmo
        n = a // b #Cantidad de veces que cabe b en a
        c = a - (n * b)
        a = b
        b = c
    
    return a #El mcd es el ultimo valor de a


def criba(n:int)->list:
    primes = [] #Vamos a crear una lista donde vamos a meter los primos
    not_primes = set() #tambien un set, para tener todo los numeros de la criba

    for i in range(2, n+1):#vamos a empezar desde el primer primo, hasta el limite superior, incluido con el

        if i in not_primes: #Primero mira si no esta en la lista de la criba
            continue

        # Agarramos desde el primer multiplo, hasta el numero limite,
        # Y empieza a a iterar, de multiplo en multiplo
        for j in range(i*2, n+1, i): 
            not_primes.add(j) # pone el numero

        primes.append(i) # mete el numero, mientras no este en primos

    return primes



#Mario, no me pegue porfavor
def generar_primo(rango_inf:int, rango_sup:int)->int: #no le puse valor de retorno, porque va a devolver o un None o el numero
    try:
        cribHastaSup = criba(rango_sup) #genera hasta el primo mas cerca al higher bound
        
        cribDesdeInf = [prime for prime in cribHastaSup if prime >= rango_inf] #quitar todo los valores mas bajos que el limite inferior

        return cribDesdeInf[rd.randint(0,len(cribDesdeInf)-1)] #retorna desde el indice 0 al tamano de la cribFromLower

    except Exception as e:
        raise ValueError(f"Error: {e}")



    
def inverso_modular(a:int, b:int):
    x = 0
    y = 1
    u = b
    v = a

    existe = mcd(a,b)
    if existe != 1: #no existe un inverso modular si su mcd no es 1
        return None
    
    while v != 0:
        q = u // v 
        r = u - (q * v)
        s = x - (q * y)
        u = v
        x = y
        v = r
        y = s
    
    return x % b

def generar_llaves(rango_inf:int, rango_sup:int)->tuple:
    a = generar_primo(rango_inf, rango_sup)
    b = generar_primo(rango_inf, rango_sup)

    n = a * b

    if n < 256:
        return generar_llaves(rango_inf, rango_sup)
    else: 
        euler = (a-1)*(b-1)
        e = generar_primo(rango_inf, rango_sup)
        d = inverso_modular(e, euler)
        if d == None:
            return generar_llaves(rango_inf, rango_sup)
        else:
            return (e,n), (d,n)


