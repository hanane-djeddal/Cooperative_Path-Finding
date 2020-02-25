#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:12:04 2019

@author: 3803192
"""
#--------------------------------------------------------------------
#Un objet qui contient les données necessaires pour chaque stratégie
#--------------------------------------------------------------------
class Espace :
    def __init__(self,init,but,lignes,colonnes,wall,game,players):
        self.init=init
        self.but=but
        self.lignes=lignes
        self.colonnes=colonnes
        self.wall=wall
        self.game=game
        self.players=players
    
    def estBut(self,e):
        return (self.but==e)