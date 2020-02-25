# -*- coding: utf-8 -*-

# Nicolas, 2015-11-18
#Modifier par DJEDDAL TOUZARI 2018-03

from __future__ import absolute_import, print_function, unicode_literals
from gameclass import Game,check_init_game_done
from spritebuilder import SpriteBuilder
from players import Player
from sprite import MovingSprite
from ontology import Ontology
from itertools import chain
import glo
import random 
import numpy as np
import sys
import pygame
import donnees
import Strategie1
import Strategie2    
import Strategie3
# ---- ---- ---- ---- ---- ----
# ---- Main                ----
# ---- ---- ---- ---- ---- ----

game = Game()


def init(_boardname=None):
    global player,game,nbreCol,nbreLig
    # pathfindingWorld_MultiPlayer4
    name = _boardname if _boardname is not None else 'pathfindingWorld_MultiPlayer5'
    game = Game('Cartes/' + name + '.json', SpriteBuilder)
    game.O = Ontology(True, 'SpriteSheet-32x32/tiny_spritesheet_ontology.csv')
    game.populate_sprite_names(game.O)
    game.fps = 5  # frames per second
    game.mainiteration()
    game.mask.allow_overlaping_players = True
    nbreCol = game.spriteBuilder.colsize-1
    nbreLig =game.spriteBuilder.rowsize-1
    player = game.player
    
def main():

    #for arg in sys.argv:
    iterations = 50 # default
    if len(sys.argv) == 2:
        iterations = int(sys.argv[1])

    init()
    
    
    

    
    #-------------------------------
    # Initialisation
    #-------------------------------
       
    players = [o for o in game.layers['joueur']]
    
    # on localise tous les états initiaux (loc du joueur)
    initStates = [o.get_rowcol() for o in game.layers['joueur']]
    print ("Init states:", initStates)
    
    
    # on localise tous les objets ramassables
    #joeur d'indice i dans players ramasse la fiole d'indice i dans goalStates
    goalStates = [o.get_rowcol() for o in game.layers['ramassable']]
    random.shuffle(goalStates)
    print ("Goal states:", goalStates)
    while( len(goalStates) < len (initStates)):
        goalStates.append(initStates[len(goalStates)])
   
    # on localise tous les murs
    wallStates = [w.get_rowcol() for w in game.layers['obstacle']]
    
    #on cree un objet espace
    p= donnees.Espace(initStates,goalStates,nbreLig,nbreCol,wallStates,game,players)
    
  
    # on donne a chaque joueur une fiole a ramasser
    # en essayant de faire correspondre les couleurs pour que ce soit plus simple à suivre
    
    
    #-------------------------------
    # Première Stratégie
    #-------------------------------
    #Strategie1.strategie1(p)
    
    #-------------------------------
    # Deuxiéme Stratégie
    #-------------------------------
    #Strategie2.strategie2(p)
    
    #-------------------------------
    # Troisieme Stratégie
    #-------------------------------
    #Transformation du monde en un monde 3D qui prend en consideration le temps 
    
    wall3D=[]
    for i in wallStates:
        wall3D.append((i[0],i[1],-1))
    p= donnees.Espace(initStates,goalStates,nbreLig,nbreCol,wall3D,game,players)
    
    Strategie3.strategie3(p)   
    
      
          
if __name__ == '__main__':
    main()
    


