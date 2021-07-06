import adivicao
import forca

print("*************************")
print("Escolha seu jogo")
print("*************************")

print("(1)Forca (2)Adivinhação")

jogo = int(input("Qual o jogo?"))

if(jogo == 1):
    print("Iniciando jogo da forca")
    forca.jogar()

elif(jogo == 2):
    print("Iniciando jogo da Adivinhação")
    adivicao.jogar()

if __name__ != "__main__":
    pass
else:
    jogar()
