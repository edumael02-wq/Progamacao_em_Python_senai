import random

numero = random.randrange(1,10)
escolha = int(input('escolha um número 1 a 10'))

if numero == escolha:
print('Você ganhou o jogo!! 👍😁')
print('o numero aleatrorio é', numero)

else:
    print('Errou feio! ☠️🧐')    
    print('O numero aleatrorio é ', numero)
