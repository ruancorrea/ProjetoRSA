from construindoChaves import InfoChaves
from criptografia import encriptando, decriptando
from verificacao import verificacaoInicial, gerandoNumPrimo

entrada = -1
while(entrada != 0):
    print("\n(1) Gerar chaves / (2) Encriptar mensagem / (3) Desencriptar mensagem / (0) Sair")
    entrada = int(input("Digite a opção: "))
    
    if entrada == 1:
        while True:
            print("Caso p=0 ou q=0, então será gerado um número primo no intervalo 2^9 a 2^10 tal p=0 ou q=0")
            p = int(input("Digite um número primo P: "))
            q = int(input("Digite um número primo Q: "))

            if p == 0:
                p = gerandoNumPrimo()
            if q == 0:
                q = gerandoNumPrimo()
            verificacao = verificacaoInicial(p,q)
            if verificacao[0]:
                break
            else: print(verificacao[1])
        print(f"p={p} / q={q}")
        n, e, d, totiente = InfoChaves(p,q)

        chavePublica = open("chavePublica.txt", "w")
        chavePublica.write(f"{n},{e}")
        chavePublica.close()

        chavePrivada = open("chavePrivada.txt", "w")
        chavePrivada.write(f"{n},{d}")
        chavePrivada.close()

        print("Chaves criadas com sucesso.")
    
    elif entrada == 2:
        chavePublica = open("chavePublica.txt",'r')
        for linha in chavePublica:
            n,e = linha.split(",") 
        chavePublica.close()       
        print("Chave pública encontrada.", f"n = {n}, e = {e}")
        m = input("Digite o texto a ser criptografado: ")

        # criptografando mensagem
        mensagemCriptografada = open("mensagemCriptografada.txt", "w")
        encript = encriptando(m, int(e), int(n))
        mensagemCriptografada.write(encript)
        mensagemCriptografada.close()
        print("Mensagem criptografada com sucesso! Armazenada no arquivo mensagemCriptografada.txt.")

    elif entrada == 3:
        chavePrivada = open("chavePrivada.txt",'r')
        for linha in chavePrivada:
            n,d = linha.split(",")
        chavePrivada.close()        
        print("Chave pública encontrada.")
        m = open("mensagemCriptografada.txt",'r')
        for linha in m:
            encript = linha.split()
        decript = decriptando(encript, int(d), int(n))
        mensagemDecriptografada = open("mensagemDecriptografada.txt", "w")
        mensagemDecriptografada.write(decript)
        mensagemDecriptografada.close()
        print("Mensagem criptografada com sucesso! Armazenada no arquivo mensagemDecriptografada.txt.")