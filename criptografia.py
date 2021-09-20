# dicionarios para criptografia

dicionario_encript = {"a": "2", "b": "3", "c": "4", "d": "5",
              "e": "6", "f": "7", "g": "8", "h": "9",
              "i": "10", "j": "11", "k": "12", "l": "13",
              "m": "14", "n": "15", "o": "16", "p": "17",
              "q": "18", "r": "19", "s": "20", "t": "21",
              "u": "22", "v": "23", "w": "24", "x": "25",
              "y": "26", "z": "27", " ": "28"}

dicionario_decript = {2: "a", 3: "b", 4: "c", 5: "d",
              6: "e", 7: "f", 8: "g", 9: "h",
              10: "i", 11: "j", 12: "k", 13: "l",
              14: "m", 15: "n", 16: "o", 17: "p",
              18: "q", 19: "r", 20: "s", 21: "t",
              22: "u", 23: "v", 24: "w", 25: "25",
              26: "y", 27: "z", 28: " "}

def pot(x, y, p):
    res = 1
    x = x % p
    if (x == 0):
        return 0
    while (y > 0):
        if ((y & 1) == 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
         
    return res


def encriptando(m, e, n):
    cript = ""
    print(m)
    for i in range(len(m)):
        res = pot(int(dicionario_encript[m[i]]), e, n)
        cript += str(res) + " "
    return cript


def decriptando(m, d, n):
    decript = ""
    for i in range(len(m)):
        res = dicionario_decript[pot(int(m[i]),d,n)]
        decript += res
    return decript