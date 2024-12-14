import pygame
from pygame.locals import *
from sys import exit
from random import randint

largura = 700
altura = 700

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('mordida.wav')

tela = pygame.display.set_mode((largura, altura))
tela.fill((255, 255, 255)) 
pygame.display.set_caption('Snake Game')
relogio = pygame.time.Clock()

imagem_fundo = pygame.image.load("grama.jpg")
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

imagem = pygame.image.load("maca.webp")
imagem = pygame.transform.scale(imagem, (40, 40))

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [X, Y]
        #XeY[0] = x
        #XeY[1] = y
        pygame.draw.rect(tela, (139, 69, 19),(XeY[0], XeY[1], 35, 35))

def reiniciar_jogo():
    global pontos, comprimento_da_cobra, x_cobra, y_cobra, lista_cobra, lista_cabeca, lista_cobra, y_maca, x_maca, morreu
    pontos = 0
    comprimento_da_cobra = 5
    x_cobra = int(largura/2)
    y_cobra = int(altura/2) 
    lista_cabeca = []
    lista_cobra = []
    x_maca = randint (80, 620)
    y_maca =  randint (80, 620)
    morreu = False

x_cobra = int(largura/2)
y_cobra = int(altura/2)

velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = randint (80, 620)
y_maca =  randint (80, 620)

font = pygame.font.SysFont('Impact', 40, False, False)
pontos = 0

lista_cobra = []

comprimento_da_cobra = 5

morreu = False

while True:

    relogio.tick(30)

    #tela.fill((255, 255, 255))

    tela.blit(imagem_fundo, (0, 0))

    mensagem = f'Pontos: {pontos}'
    texto_formatado = font.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade
            if event.key == K_UP:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == K_LEFT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_RIGHT:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0  

    x_cobra += x_controle
    y_cobra += y_controle

    cobra = pygame.draw.rect(tela, (139, 69, 19),(x_cobra, y_cobra, 35, 35))
    maca = imagem.get_rect()
    maca.topleft = (x_maca, y_maca)

    tela.blit(imagem, (x_maca, y_maca))
    
    if cobra.colliderect(maca):
        x_maca = randint (80, 620)
        y_maca =  randint (80, 620)
        pontos += 1
        barulho_colisao.play()
        comprimento_da_cobra += 1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)
    if lista_cobra.count(lista_cabeca) > 1: # TÁ DIZENDO QUE JÁ EXISTE UMA POSIÇÃO DA CABEÇA NO TAMANHO DA COBRA | MORTE DA COBRA
        font2 = pygame.font.SysFont('Arial', 20, True, True)
        mensagem2 = 'Game Over! Pressione a tecla Enter para reiniciar o jogo'
        texto_formatado2 = font2.render(mensagem2, True, (0,0,0))
        ret_text = texto_formatado2.get_rect()
        morreu = True
        while morreu:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        reiniciar_jogo()
            ret_text.center = largura//2, altura//2
            tela.blit(texto_formatado2, ret_text)
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra > altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura

    if len(lista_cobra) > comprimento_da_cobra:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)
    tela.blit(texto_formatado, (500, 40))

    pygame.display.update()     
       
    