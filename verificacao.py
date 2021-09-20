import numpy as np
import math

def ehPrimo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def MDC(a, b, coef): # algoritmo recursivo de euclides
    if (b == 0):
        return a, coef[::-1]
    else:
        coef.append(int(a/b))
        return MDC(b, a % b, coef)



def verificacaoInicial(p ,q):
    if not ehPrimo(p):
        return [False, "P não é primo."]
    if not ehPrimo(q):
        return [False, "Q não é primo."]
    return [True, f"Verificação feita com sucesso."]


def gerandoNumPrimo():
    num = np.random.randint(2**21,2**27)
    while not ehPrimo(num):
        num = np.random.randint(2**21,2**27)
    return num