from dicionarios import dicionario_decript, dicionario_encript

def encriptando(m, e, n):
    cript = ""
    print(m)
    for i in range(len(m)):
        res = int(dicionario_encript[m[i]])**e % n
        cript += str(res) + " "
    return cript


def decriptando(m, d, n):
    decript = ""
    for i in range(len(m)):
        res = dicionario_decript[int(m[i])**d % n]
        decript += res
    return decript