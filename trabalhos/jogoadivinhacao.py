import random
numero_secreto = random.randint(1,100)
print(numero_secreto)

print("bem vindo")
print("tente adivinha 1 e 100")
tentativas = 0
adivinhou = False
while not adivinhou:
    tentativa=int(input("Digite um numero de 1 a 100"))
    tentativas+=1
    if tentativa==numero_secreto:
        print("parabens voce acerto", tentativas, "tentativas")
        adivinhou = True
    elif tentativa < numero_secreto:
        print("tente um numero maior")
    else:
        print("tente um numero menor")
print("fim do jogo seu bosta")    
