import random

def jogar():

    imprimirabertura()
    palavra_secreta = gerar_palavra()
    letras_acertadas = substitui_letrasecreta(palavra_secreta)

    encerar = 0
    enforcou = False
    acertou = False
    erros = 0

#Enquanto nao enforca ou acerta a palavra, o ciclo "while" continua#
    while(not enforcou and not acertou):

        chute = pedir_chute()

        if(chute in palavra_secreta):
            marcar_chute_correto(chute, letras_acertadas, palavra_secreta)

        else:
            erros = erros + 1
            desenha_forca(erros)
        enforcou = erros == 7
        print (letras_acertadas)

        letras_faltando = int(letras_acertadas.count('_'))
        print( 'Ainda faltam acertar {} letras'.format(letras_faltando))

        if (letras_faltando == encerar):
            print("Parabéns, você ganhou!")
            print("       ___________      ")
            print("      '._==_==_=_.'     ")
            print("      .-\\:      /-.    ")
            print("     | (|:.     |) |    ")
            print("      '-|:.     |-'     ")
            print("        \\::.    /      ")
            print("         '::. .'        ")
            print("           ) (          ")
            print("         _.' '._        ")
            print("        '-------'       ")

            break

    else:
        imprime_mensagem_perdedor(palavra_secreta)


    print("FIM DO JOGO")


#Funções do projeto
def imprimirabertura():
    print("*************************")
    print("Bem vindo ao jogo da Forca!")
    print("*************************")


def gerar_palavra():
    arquivo = open(r'C:\Users\Editor\Desktop\Python Alura\Modulo1 (Jogo da advinhação)/frutas.txt')
    palavra = []
    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)
        
    arquivo.close()
    
    numero = random.randrange(0, len(palavra))
    palavra_secreta = palavra[numero].upper()
    return palavra_secreta


def substitui_letrasecreta(palavra):
    return ["_" for letra in palavra]

def pedir_chute():
    chute = input("Qual a letra?").upper()
    chute = chute.strip()
    return chute


def marcar_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute.lower() == letra.lower()):
            letras_acertadas[index] = letra
        index = index + 1

    return letra

def imprime_mensagem_perdedor(palavra_secreta):
    print ("Voce Perdeu!")
    print(palavra_secreta)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    jogar()