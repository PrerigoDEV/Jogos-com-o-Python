import random


def jogar():
    print("*************************")
    print("Bem vindo ao jogo da advinhação")
    print("*************************")

    numero_secreto = random.randrange(1, 101)  # Gerando um numero aleatorio#
    total_tentativas = 0
    pontos_totais = 1000

    print("ESCOLHA O NIVEL DE DIFICULDADE?")
    print("(1)Facil (2)Medio (3)Dificil")
    print("*************************")

    nivel = int(input("Defina o nivel da dificuldade:"))
    if nivel == 1:
        total_tentativas = 20

    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):

        print("*************************")
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        print("*************************")

        chute = int(input("Digite seu número entre 1 e 100: "))
        print("Voce digitou: {}".format(chute))

        if chute < 1 or chute > 100:
            print("O numero deve estar entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        numero_menor = chute < numero_secreto
        numero_maior = chute > numero_secreto

        if acertou:
            print("Voce digitou o numero correto! Fez {0}".format(pontos_totais))
            break

        else:
            if numero_menor:
                print("Voce Errou! O numero é menor que o Secreto.")
                print("")
            elif numero_maior:
                print("Voce Errou! O numero é maior que o Secreto")
                print("")
            if rodada == total_tentativas:
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos_totais))
                print("")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos_totais = pontos_totais - pontos_perdidos

    print("FIM DO JOGO")


if __name__ == "__main__":
    jogar()
