#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:31:24 2019

@author: 3802643
"""
import heapq

def heuristique(debut,fin):
     return abs(debut[0]-fin[0]) + abs (debut[1]-fin[1])
 
class Noeud :
    def __init__(self,etat,g,parent):
        self.etat=etat
        self.g=g
        self.parent=parent
    def __str__(self):
        #return np.array_str(self.etat) + "valeur=" + str(self.g)
        return str(self.etat) + "valeur=" + str(self.g)
        
    def __eq__(self, other):
        return str(self) == str(other)
        
    def __lt__(self, other):
        return str(self) < str(other)
    
    def expand (self,wallStates,nbreCol,nbreLig,reservation):
        wall=wallStates
        for r in reservation:
            wall=wall+r
        succ=[]
        indice=([(self.etat[0],self.etat[1]+1,self.etat[2]+1),(self.etat[0],self.etat[1]-1,self.etat[2]+1),(self.etat[0]+1,self.etat[1],self.etat[2]+1),(self.etat[0]-1,self.etat[1],self.etat[2]+1)])
        for e in indice :
            if (not isIn(e,wall)) and (not isIn((e[0],e[1],e[2]+1),wall)) and e[0]>=0 and e[0]<=nbreLig and e[1]>=0 and e[1]<=nbreCol:
                n = Noeud(e,1+self.g,self)
                succ.append(n)
        if succ==[]:
            succ.append(Noeud((self.etat[0],self.etat[1],self.etat[2]+1),1+self.g,self))
        return succ;
    
def immatriculation(i):
    return "i = "+str(i[0])+", j = "+str(i[1])+", t = "+str(i[2])      

def isIn(e,wall):
    for i in wall:
        if e==i:
            return True
        if i[2]==-1 and i[0]==e[0] and i[1]==e[1]:
            return True
    return False
            

def Astar_temporise(init,but,wallStates,nbreCol,nbreLig,reservation):
    chemin=[];
    nodeInit = Noeud(init,0,None)
    frontiere = [(nodeInit.g+heuristique(nodeInit.etat,but),nodeInit)] 
    reserve = {}        
    bestNoeud = nodeInit
    
    while frontiere != [] and not (bestNoeud.etat[0]==but[0] and bestNoeud.etat[1]==but[1]):          
        (min_f,bestNoeud) = heapq.heappop(frontiere)         
    
        if immatriculation(bestNoeud.etat) not in reserve:            
            reserve[immatriculation(bestNoeud.etat)] = bestNoeud.g #maj de reserve
            nouveauxNoeuds = bestNoeud.expand(wallStates,nbreCol,nbreLig,reservation)            
            for n in nouveauxNoeuds:
                f = n.g+heuristique(n.etat,but)
                heapq.heappush(frontiere, (f,n))  
    noeud= bestNoeud
    while (noeud != None):
        chemin.append(noeud.etat)
        noeud=noeud.parent         
    chemin.reverse()
    reservation.append(chemin)
    return chemin
