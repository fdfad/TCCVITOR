import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
import pygame
import sys
from pygame.locals import *

pygame.init()

#Cria a tabela
tabela = pd.read_csv("Alunos.csv", index_col=0)

materias = ["matematica", "biologia", "portugues", "fisica", "quimica", "filosofia", "sociologia", "geografia", "historia", "ingles"]

#Filtra as informaçoes da tabela
for i in range(9):
    tabela[materias[i]] = pd.to_numeric(tabela[materias[i]], downcast="float")

#Configurações pygame
Tela = pygame.display.set_mode((800, 700))
fonte = pygame.font.SysFont('Roboto', 40, True, False)
clock = pygame.time.Clock()
pygame.display.set_caption("Analise das suas notas em 6 anos")

#Criação dos botões
ProximoIMG = pygame.image.load("button_proximo.png").convert_alpha()
VoltarIMG = pygame.image.load("button_voltar.png").convert_alpha()
GraficosIMG = pygame.image.load("button_graficos.png").convert_alpha()

#Button class
class Button():
    def __init__(self,x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, ((int(width * scale)) ,(int(height * scale))))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        
    def draw(self):
        action = False
        
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        Tela.blit(self.image,(self.rect.x,self.rect.y))
        
        return action
    
Proximo = Button(500,500,ProximoIMG,1)
Voltar = Button(100,500,VoltarIMG,1)    
Graficos = Button(100,600,GraficosIMG,1)  

i = 0

while True:
    clock.tick(60)
    
    Tela.fill((225, 229, 242))
    
    maior = str(tabela[materias[i]].dropna().max())
    menor = str(tabela[materias[i]].dropna().min())
    media = str(tabela[materias[i]].dropna().mean())
    Materia = str(materias[i])
    
    texto = fonte.render("A sua nota media em "+ str(materias[i]) +" foi " + maior, True, (0,0,0))
    texto2 = fonte.render("A sua menor nota em "+ str(materias[i]) +" foi " + menor, True, (0,0,0))
    texto3 = fonte.render("A sua nota media em "+ str(materias[i]) +" foi " + media, True, (0,0,0))
    texto4 = fonte.render(Materia, True, (0,0,0))
    
    Tela.blit(texto, (100, 150))
    Tela.blit(texto2, (100, 250))
    Tela.blit(texto3, (100, 350))
    Tela.blit(texto4, (300, 50))
    
    if Proximo.draw():
        if i != 9:
            i += 1
        
    if Voltar.draw():
        if i != 0:
            i -= 1
        
    if Graficos.draw():
        print(tabela.describe())
        tabela.dropna().plot.area(figsize=(18, 8), subplots=True)
        tabela.dropna().hist()
        plt.show()
        
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    






