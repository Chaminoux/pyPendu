#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# Jeu du Pendu (test)
# Test
# Import
from random import randint
#from donnees import *
import donnees
#import pendu
import pickle
#
global chance

# intro bonjour
def PrintHello():
    """ Fonction impression debut de partie"""
    print("\n#############################################\nBonjours et bienvenue au grand Jeux du Pendu!\n#############################################\n")
# Séléction du mot au hazard
#def NmbreRandom():
  #  """Fonction pour donner un chiffre au hazard"""
  #  nmbreRandom = randint(0,5)
  #  
  #  return nmbreRandom
    

def Nouvelle_Partie():
    nouvelle_partie = input("Nouveau Joueur ? ('y' pour oui/ 'n' pour non) :\n")
    if nouvelle_partie.lower() == "y":
        global xpJoueur
        xpJoueur = '0'
        inputJoueur = input('Saisir votre nom :\n')
        nomJoueur = open('ficheJoueur.txt', 'w')
        nomJoueur.write(inputJoueur + ' ' +xpJoueur)
        nomJoueur.close()
    elif nouvelle_partie.lower() == "n":
        with open('ficheJoueur.txt', 'r') as ficheJoueur:
            ficheJoueur = ficheJoueur.read()
            lenJoueur = len(ficheJoueur)
            xpJoueur = ficheJoueur[lenJoueur-1:]
            nomJoueur = ficheJoueur[: -2]
            print("Salut {0}!!! t'es prêt ??\nexpérience -> {1}".format((nomJoueur),(xpJoueur)))

def ChoixMot():
    """Fonction pour choisir le mot a deviner en fonction du nombre random"""
    nmbreRandom = randint(0,5)
    motChoisie = donnees.listeMot[nmbreRandom]
    global motChoisieGlobal
    motChoisieGlobal = str(motChoisie)
    return motChoisie


# On décompose le mot choisie:
def DecomposerMotChoisie():
    """Fonction pour décomposer le mot choisie"""
    global motList
    motList = list(motChoisieGlobal)
    return motList
    
def LongueurMot():
    """Fonction pour indiquer le nombres de lettre a deviner"""
    print("Le mot a deviner est composé de {} lettres.".format(len(motChoisieGlobal)))

def MotCrypter():
    """Fonction pour remplacer les lettre du mot choisie par des etoiles"""
    global motCrypter
    motCrypter = '*'*len(motChoisieGlobal)
    return motCrypter

def CompteurChance():
    global chance
    chance = donnees.nmbreChance
    if LettreCompare() == 'False':
        chance -= 1
        print(chance)
    return chance

def LettreCompare():
    """ Fonction qui compare et remplace la lettre saisie dans le mot a deviner"""
    # global
    global entreLettre
    global chance
    global fichierMot
    global motList
    global suiteMot
    global listMotCrypter
    global indice
    global bonneReponse
    bonneReponse = 'False'
    
    print(motChoisieGlobal)       # Affiche le mot en claire (a supprimer une fois le jeux terminé)
    entreLettre = input("Veuillez entrer une lettre\n-> ")
    
    if ((len(entreLettre) == 1) and (entreLettre.lower() in motList)): # and (CompteurChance() != 0)):
        motCrypter = '*'*len(motChoisieGlobal)
        listMotCrypter = list(motCrypter)     
        indice = int(motList.index(entreLettre))
        listMotCrypter.pop(indice)
        listMotCrypter.insert(indice,entreLettre)  
        print('Bien joué! la lettre {} est bien présente dans le mot a deviner!'.format(entreLettre))
        motDecrypt = (''.join(listMotCrypter))
        fichierMot = motDecrypt
        print('------------->'+ fichierMot)
        motCrypter = fichierMot
        #fichierMot = open('mot.txt', 'w')
        #fichierMot.write(motDecrypt)
        #fichierMot.close()
        bonneReponse = 'True'    
    elif entreLettre != motList:
        print('dommage frommage!\nIl te reste {0} chances'.format(donnees.nmbreChance))
        donnees.nmbreChance -= 1
        bonneReponse = 'False'
        if donnees.nmbreChance == 0 :
            print('PERDU!')
            chance = donnees.nmbreChance
            return chance
        #with open('donner.py', 'wb') as donnes.nmbreChance:

    else:
        print('euuhh ?')
    return [bonneReponse]

#def Update_Word(bonneReponse):
#    if bonneReponse == True:
        
     



            
        



