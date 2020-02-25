#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:40:35 2019

@author: 3803192
"""
import Aetoile 
import pygame

#-------------------------------------
#Stratégie deux : Coopérative de base
#-------------------------------------

class Groupe:
    def __init__(self):
        self.positions=[]
        self.long=0

def grouper(chemins):
    groupes=[]
    for i in range (len(chemins)):
        c=chemins[i]
        p=choixGroupe(groupes,chemins,c)
        if(p==None):
            groupes.append(Groupe())
            p=len(groupes)-1
        groupes[p].positions.append(i)
        if(groupes[p].long<len(c)):
            groupes[p].long=len(c)
    return groupes 
 
def choixGroupe(groupes,chemins,chemin):
    indice=None
    long=0
    for i in range(len(groupes)):
        for c in groupes[i].positions:
            s=list(set(chemins[c]).intersection(chemin))
            if(s!=[]):
                break
        if(s== [] and long<groupes[i].long):
            indice=i
            long=groupes[i].long
    return indice

def strategie2(p):
    nbPlayers = len(p.players)
    score = [0]*nbPlayers
    chemins=[] #liste des chemins des joueurs
    iterations=0
   
    for i in range(nbPlayers):# ici on récupére tous les chemins des joueurs 
        chemins.append(Aetoile.Astar(p.init[i],p.but[i],p.wall,p.colonnes,p.lignes))
    print(chemins)
    groupes=grouper(chemins)

    for g in groupes:
        cheminsCourant=g.positions
        print(cheminsCourant)
        for j in range(g.long):
            for pos in cheminsCourant:
                chemin=chemins[pos]
                if(len(chemin)>j): 
                    iterations+=1
                    row,col=chemin[j][0],chemin[j][1]
                    p.players[pos].set_rowcol(row,col)
                    p.game.mainiteration()
                    if (row,col)==p.but[pos]:
                        o = p.players[pos].ramasse(p.game.layers)
                        p.game.mainiteration()
                        score[pos]+=1
                        
    print ("scores:", score)
    print ("Nombre d'iterations:", iterations)
    pygame.quit()
    