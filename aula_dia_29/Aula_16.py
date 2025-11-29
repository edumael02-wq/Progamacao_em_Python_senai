# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

import pygame

# Inicializa o Pygame
pygame.init()


# o que a estrutura(sintaticamente)? para que serve(contexto)? 
# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/




# 2 variáveis para definir a altura e a largura da tela 
largura, altura = 400, 400

# 1 variável que atribuida a ela a função que cria a tela 
tela = pygame.display.set_mode((largura, altura))

# Chamada do módulo acompanhado da função que add um título a tela  
pygame.display.set_caption("Labirinto")

# 3  variáveis que atribui a elas o rgb da cores  
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# 1  variável que atrbui a ela o largura/ altura da celula 

tamanho_celula = 40

# lista bidimensional que esta definindo o tabuleiro 

labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 2 variáveis posicionandi as celulas 
x, y = 1 * tamanho_celula, 1 * tamanho_celula


# 1  variável que defini a velocidade da celula
velocidade = 40


# criação de uma função, para criar o labirinto 

def desenhar_labirinto():
    # acessando a primeira dimensão da lista, [0-9]
    for linha in range(len(labirinto)):
        # caessando a segunda dimensão da lista trazendo os indices
        # atribuidos a variavel coluna 
        for coluna in range(len(labirinto[linha])):
            # variavel  que defini uma condição, 
            # condição pinta as estruturas do código de acordo com o os indices 
            cor = preto if labirinto[linha][coluna] == 1 else branco
            # modulo que desenha um retangulo, e pinta cada um do quadrados na tela
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))

# 1  variável  que defini o loop inicial da tela
executando = True
# estrutura de fluxo de controle que defini o loop infinito
while executando:
    # estrutura de fluxo de controle que defini o loop parar o código de acordo com a condição
    for evento in pygame.event.get():
        #  estrutura de fluxo de controle, condicional que defini tipos
        #  de eventos capturados na tela   
        if evento.type == pygame.QUIT:
            # 1 varivael que retorna false caso o evento seja de quit() 
            executando = False
  
# lista,  atribuido a ela todos os possiveis eventos no teclado 
    teclas = pygame.key.get_pressed()
    # estrutura de fluxo de controle, verifica se a seta da esqueda
    # foi clicada 
    if teclas[pygame.K_LEFT]:
        # 1 variável que declara dentro da condicional, velocidadepara esquerda 
        novo_x = x - velocidade
        # estrtura de fluxo de controle que defini as posições do personagem
        # defini que anda pelo 0
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x

     # estrtura de fluxo de controle que defini as posições do personagem
     # defini que anda pelo 0        
    if teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
   
     # estrtura de fluxo de controle que defini as posições do personagem
    # defini que anda pelo 0
    if teclas[pygame.K_UP]:
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    # estrtura de fluxo de controle que defini as posições do personagem
    # defini que anda pelo 0        
    if teclas[pygame.K_DOWN]:
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y

    # 1 objeto.metodo()

    tela.fill(branco)

    # função, chamada da função 
    desenhar_labirinto()
    # modulo pygame.submodulo draw, desenho do personagem vermelho
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))

    # modulo pygame.submodulo display(tela), atauliza
    pygame.display.flip()

    # modulo pygame.submodulo time, definir a velocidade fps  
    pygame.time.Clock().tick(10)

# modulo pygame com o metodo quit -  fechar o pygame
pygame.quit()
