def ehPrimo(num):
  p = 0
  x = 1
  while x <= num:
    x += 1
    if num%x == 0:
      p += 1
  if p >= 2:
    return False
  else:
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