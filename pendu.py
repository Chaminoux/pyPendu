#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# Jeux du pendu 

# import 
import fonctions
import donnees
# Affiche Bonjours!
fonctions.PrintHello()
fonctions.Nouvelle_Partie()

# Trouve un nombre au hazard entre 0 et 10
#nmbreRandom = fonctions.NmbreRandom()
#print(nmbreRandom)

# On selectionne un mot a deviner avec le nombreRandom
motChoisie = fonctions.ChoixMot()
#print(motChoisie)


listMot = fonctions.DecomposerMotChoisie()
#print(listMot)
#continuer = 'o'
#while ((continuer != 'n') and (fonctions.CompteurChance() > 0)):
fonctions.LongueurMot()
print("\n---> " + fonctions.MotCrypter()+ "\n")
print(donnees.nmbreChance)
#chance = donnees.nmbreChance
while fonctions.chance != 0:
    fonctions.LettreCompare()
    if fonctions.LettreCompare() == True:
        fonctions.motCrypter = fonctions.fichierMot
    elif fonctions.LettreCompare() == False:
        chance -= 1
    else :
        print("T'es finit!")





#print(fonctions.CompteurChance())
#if ((fonctions.CompteurChance()) > 0) and :
#        continuer = 'o'
#else:
#        continuer = 'n'
#        print('Perdu!')


