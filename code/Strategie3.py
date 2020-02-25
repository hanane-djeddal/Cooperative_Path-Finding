#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:06:51 2019

@author: 3803192
@author: 3802643
"""
import Aetoile_Revisite
import pygame

#-------------------------------------
#Stratégie trois : Coopérative avancée
#-------------------------------------

def strategie3(p):
    nbPlayers = len(p.players)
    score = [0]*nbPlayers
    chemins=[] #liste des chemins des joueurs
    reservation=[] #liste des chemins déjà calculés
    iterations=0
    for i in range(nbPlayers):# ici on récupére tous les chemins des joueurs en mettant à jour reservations
        itt=(p.init[i][0],p.init[i][1],0)
        chemins.append(Aetoile_Revisite.Astar_temporise(itt,p.but[i],p.wall,p.colonnes,p.lignes,reservation))
    print("les chemins",chemins)  
    joueursRestants =nbPlayers #Nous permet de quitter la boucle principale
    pos=0 # indice pour parcourir les chemins simultanément 
    while(joueursRestants>0 ): # tant qu'il existe un joueur qui n'a pas encore trouvé son objet
        j=-1 # l'indice du joueur courant
        
        for chemin in chemins: #on recupere la position suivante pour chaque joueur  
            j+=1
            if(len(chemin)>pos): 
                iterations+=1
                row,col=chemin[pos][0],chemin[pos][1]
                p.players[j].set_rowcol(row,col)
                p.game.mainiteration()
                
                if (row,col)==p.but[j]:
                    o = p.players[j].ramasse(p.game.layers)
                    p.game.mainiteration()
                    joueursRestants-=1 
                    score[j]+=1
       
             
        pos+=1
    print ("scores:", score)
    print ("Nombre d'iterations:", iterations)
    pygame.quit()