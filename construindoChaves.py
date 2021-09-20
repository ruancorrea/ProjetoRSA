from verificacao import MDC

def totiente(p, q):
    return (p - 1) * (q - 1)
  

def achandoE(n, i):
    if MDC(n, i, [])[0] == 1:
        return i
    return -1


def buscando_st(coef, st):
    for i in range(2, len(coef)):
        st.append(st[i-2] + st[i-1] * coef[i])
    if len(coef) % 2 == 0:
        st[-1] = -1 * st[-1]
    else:
        st[-2] = -1 * st[-2]
    return st[-2], st[-1]



def inverso_mob(a, b):
    mdc, coef = MDC(a, b, [])
    return (-1 if mdc!=1 or len(coef) < 2 else buscando_st(coef, [1,coef[1]])[0])



def InfoChaves(p, q):
    funcTotiente = totiente(p,q)
    n = p*q
    i = 1
    d = -1
    #print(f"totiente - {funcTotiente}")
    while d < 2 and i < funcTotiente:
        e = achandoE(funcTotiente, i)
        d = inverso_mob(e,funcTotiente)
        i += 1
    #print(f"e - {e}")
    #print(f"d - {d}")

    return n, e , d, funcTotiente