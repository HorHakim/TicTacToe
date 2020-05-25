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
	#Chargement de l'interface graphique
	interfaceGraphique = open("fichier", "r", encoding='UTF-8')
	contenuInterfaceGraphique = interfaceGraphique.read()
	interfaceGraphique.close()
	#Création d'une interface pour la partie (à partir de l'interface chargée)
	maPartie = open("partieEnCours", "w", encoding='UTF-8')
	maPartie.write(contenuInterfaceGraphique)
	maPartie.close()
	etatPartie = [False]*9

	return etatPartie

def ecrireGrille(nombreCase, symbole):
	interfaceGraphique = open("partieEnCours", "r")
	contenuInterfaceGraphique = interfaceGraphique.read()
	interfaceGraphique.close()
	print(contenuInterfaceGraphique)
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

etatPartie = intialisationPartie()
for k in range(9):
	if k == 0 : 
		contenuInterfaceGraphique = intialisationPartie()
		ecrireGrille(0, "O")
		etatPartie[0] = True
	else :
		if k % 2 == 1 :
			nombreCase = input("entrez la case que vous voulez remplir: ")
			ecrireGrille(nombreCase, "X")
			etatPartie[int(nombreCase)] = True
		else : 
			caseVide = []
			for k in range(9):
				if etatPartie[k] == False:
					caseVide.append(k)

				#nombreCase = random.choice(caseVide)
				#print(nombreCase)
				#ecrireGrille(str(nombreCase), "O")
				#etatPartie[int(nombreCase)] = True





"""Boucle de jeu"""