#author : Louis Bonamy - start : 5/12/2024 - end : 
#coding utf-8

"""
Challenge : contrôler le framerate
"""
import pygame
from pygame.locals import *
import matplotlib.pyplot as plt
import os

def plot_x_carré(numéro):
    x, y = [], []
    for i in range(numéro):
        x.append(i)
        y.append(i**2)
    
    # Créer le plot
    plt.figure(figsize=(200/300, 150/300))
    plt.plot(x, y)
    plt.xlim(0, 20)  # Limites pour l'axe des x : de 0 à 6
    plt.ylim(-10, 400)

    # Ajouter des légendes et titres
    plt.xlabel('x', fontsize=1)
    plt.ylabel('y', fontsize=1)
    plt.axis('off')
    plt.grid(color='gray', linestyle='--', linewidth=0.1)
    
    # Définir le chemin et le nom du fichier
    chemin_dossier = "interface/ARGOS/"  # Remplacez par le chemin souhaité
    nom_fichier = "x_carre.png"
    chemin_complet = os.path.join(chemin_dossier, nom_fichier)

    # Créer le répertoire si nécessaire
    os.makedirs(chemin_dossier, exist_ok=True)

    # Sauvegarder le plot
    plt.savefig(chemin_complet, dpi=300, bbox_inches='tight')
    plt.close()

pygame.init()
fenetre = pygame.display.set_mode((1080,720), RESIZABLE)#FULLSCREEN pour plein écran (à éviter pour l'instant)

fond = pygame.image.load("interface/ARGOS/logo2.png").convert()
fenetre.blit(fond, (0,0))
frame = 0

pygame.display.flip()

boucle = 1
while boucle:
    for event in pygame.event.get():
        if event.type == QUIT :
            boucle = 0
            
        if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)) and frame == 0:
            boucle = 0
            
        if (event.type == KEYDOWN and event.key == K_ESCAPE) and frame == 1:
            fond = pygame.image.load("interface/ARGOS/logo2.png").convert()
            fenetre.blit(fond, (0,0))
            pygame.display.flip()
            frame = 0
            
        if event.type == KEYDOWN and event.key == K_SPACE:
            
            fond = pygame.image.load("interface/ARGOS/page_principale.png").convert()
            fenetre.blit(fond, (0,0))
            pygame.display.flip()
            
            #impossible de retourner en arrière pendant la boucle for
            for i in range(20):
                #marche pas
                if (event.type == KEYDOWN and event.key == K_ESCAPE):
                    print('ta gueule')
                    fond = pygame.image.load("interface/ARGOS/logo2.png").convert()
                    fenetre.blit(fond, (0,0))
                    pygame.display.flip()
                    frame = 0
                else :
                    plot_x_carré(i)
                    plot = pygame.image.load("interface/ARGOS/x_carre.png").convert()
                    fenetre.blit(plot, (150,120))
                    pygame.display.flip()
                
                    
            print("j'ai fini batard")
                        
            frame = 1
            
