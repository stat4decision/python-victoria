# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def moyennes_listes(liste1,liste2):
    """ cette fonction calcule la moyenne de deux listes"""
    somme=0
    for val in liste1+liste2:
        somme+=val
    return somme/len(liste1+liste2)

x=4