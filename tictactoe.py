#include:utf-8
"""
Author : Horairy Hakim

"""

###fonctions utiles
import os
import random

def rechercher(mot , lettre):
	"""Cet recherche un caractère dans un string et renvoie une liste contenant les positions du caractère dans le string"""
	compteur = 0
	Positions = []
	for element in mot:
		if element != lettre :
			compteur += 1
		else :	
			Positions.append(compteur)
	return Positions


def intialisationPartie() :
	"""Cette fonction permet d'initialiser la partie en chargant l'interface graphique dans un fichier temporaire : "PartieEnCours".
		Elle affiche la grille de début de partie sur le terminal.
		Elle renvoit une liste de booléen décrivant l'état du damier :
				True : Case occupée
				False : Case vide
		La partie étant initialisée la liste de contient donc que des False"""
	interfaceGraphique = open("fichier", "r", encoding='UTF-8')
	contenuInterfaceGraphique = interfaceGraphique.read()
	interfaceGraphique.close()
	print(contenuInterfaceGraphique)
	maPartie = open("partieEnCours", "w", encoding='UTF-8')
	maPartie.write(contenuInterfaceGraphique)
	maPartie.close()
	etatPartie = [False]*9

	return etatPartie

def caseVide(etatPartie):
	""" Cette fonction prendre en entrée l'été des case du damier
		et renvoie une liste contenant le numéro des cases vides du damier."""
	caseVide = []
	for k in range(9):
		if etatPartie[k] == False:
			caseVide.append(k)
	return caseVide

def ecrireGrille(nombreCase, symbole):
	"""Cette fonction prends
	"""
	interfaceGraphique = open("partieEnCours", "r")
	contenuInterfaceGraphique = interfaceGraphique.read()
	interfaceGraphique.close()
	case = rechercher(contenuInterfaceGraphique, (str(nombreCase)))
	tailleLigne = rechercher(contenuInterfaceGraphique, ("\n"))[0]
	inte = list(contenuInterfaceGraphique)
	inte[int(case[0])] = " "
	inte[int(case[0] - 2*tailleLigne - 4)] = symbole
	contenuInterfaceGraphique = "".join(inte)
	os.system('cls' if os.name == 'nt' else 'clear')
	print(contenuInterfaceGraphique)
	maPartie = open("partieEnCours", "w", encoding='UTF-8')
	maPartie.write(contenuInterfaceGraphique)
	maPartie.close()
	return None


"""Boucle de jeu"""
os.system('cls' if os.name == 'nt' else 'clear')
etatPartie = intialisationPartie()
for k in range(9):
	if k % 2 == 0 :
		nombreCase = input("entrez la case que vous voulez remplir (Joueur 1) : ")
		ecrireGrille(nombreCase, "X")
		etatPartie[int(nombreCase)] = True
	else : 
		nombreCase = input("entrez la case que vous voulez remplir (Joueur 2) : ")
		ecrireGrille(nombreCase, "O")
		etatPartie[int(nombreCase)] = True





