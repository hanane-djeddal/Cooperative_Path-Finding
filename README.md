# Méthodes et outils de l'IA et de la RO
Dans ce projet, on considère en compétition que plusieurs personnages doivent chacun atteindre un objectif qui leur propre (une fiole donnée).
On souhaite éviter les collisions entre personnages, ce qui signifie que l'on souhaite que les agents possèdent des algorithmes qui leurs permettent de s'éviter. Sont considérées comme collisions les situations où les personnages:


* se trouvent au même moment sur la même case, ou bien
* deux personnages se "croisent"
L'objectif est de minimiser le temps total (donc, le max) nécessaire à la récupération de toutes les fioles. On peut noter qu'il est facile d'avoir une borne inf et une borne sup pour cette valeur:

* une borne inf est le coût max des chemins optimaux calculés de manière individuelle (i.e. sans se préoccuper des autres agents)
* une borne sup est la somme des coûts des max: en effet, une stratégie toujours garantie de ne générer aucune collision consiste à donner un ordre sur les agents, et à leur demander tour à tour d'effectuer leur chemin.

le module PySpriteWorld qui élabore pygame et permet de manipuler simplement des personnages, cartes, et autres objets à l'écran. Ce module a été développé par Yann Chevaleyre.

On propose trois stratégies: 


* stratégie opportuniste de portionnement de chemins ("path slicing", voir ici). Il s'agit, lorsqu'un conflit est constaté, de recalculer une petite partie du chemin actuel en prenant en compte l'obstacle détecté.
* stratégie coopérative de base: il s'agit d'identifier des chemins qui ne partagent aucune case. De manière évidente, ces chemins peuvent alors être éxécutés en parallèle par les personnages en étant certain de ne pas entrer en collision. Reste alors à organiser l'ordre de passage.
* stratégie coopérative avancée: l'idée générale est d'utiliser une structure partagée, une table de réservation spatio-temporelle, où les cases sont désormais un triplet $(x,y,t)$. Il faut alors planifier dans cette nouvelle dimension.





# Methods and means of AI and OR
In this project, we consider a competition between different game characters where each player tries to find their own treasure.

We wish to avoid collision between characters, i.e we wish that every agent has an algorithm that allows them to avoid other characters. These following situations are considered collisions:

* Being in the same place at the same time, or
* Two characters "cross paths"

We propose three strategies: 


* Opportunist.
* Cooperative.
* Advanced Cooperative


