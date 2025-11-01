import random

pergunta = [

'O que é o que é? Quanto mais se tira, maior fica?',
'Por que o livro foi ao médico?',
'Por que o computador foi preso?',
'O que é o que é que cai em pé e corre deitado?',
'O que é um pontinho vermelho no jardim?',
'O que o tomate foi fazer no banco?',
'O que é o que é que tem asa, mas não voa, e canta sem ter boca?',
'Por que o lápis se deu mal na prova?',
'O que é o que é que quanto mais quente fica, mais frio deixa o ambiente?',

]

respotas = [

    'Um buraco!',
    'Porque ele estava com muitas “histórias” pra contar!',
    'O pente!',
    'Porque ele executou um programa!',
    'A chuva!',
    'Uma formiga com batom!',
    'Tirar extrato!',
    'O ventilador!',
    'Porque estava sem ponta!',
    'O ar-condicionado!',
]

pergunta_escolhida = random.choice(pergunta)
print(pergunta_escolhida)

escolha = int(input(f'''
0 - { respotas[0]}
1 - { respotas[1]}
2 - { respotas[2]}
3 - { respotas[3]}
4 - { respotas[4]}
5 - { respotas[5]}
6 - { respotas[6]}
7 - { respotas[7]}
8 - { respotas[8]}
9 - { respotas[9]}
'''))

indice_pergunta = pergunta.index(pergunta_escolhida)

if indice_pergunta == escolha:
    print('Acerto em cheio 👌😂😍!!!')
    print('Você ganhou um 🌽🌽🌽🌽🌽')

else:
    print('ERROU FEIO 🤦‍♂️🤦‍♀️😖😖🤡🤡')
    print('Pague R$ 1.000.00 🤬😡👿')