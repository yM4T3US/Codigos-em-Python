from random import randint
# sugestão de resolução
"""num = randint(0, 10)
palpite = int(input("Digite um número de 0 a 10: "))
while palpite != num:
    palpite = int(input("Você errou! Tente novamente: "))
print(f"Você acertou! O número escolhido foi o {num}.")"""
computador = randint(0, 10)
acertou = False
while not acertou:
    jogador = int(input("Digite um número de 0 a 10: "))
    if jogador == computador:
        acertou = True
print("Acertou!")
    