import donnees
from random import randrange
from os import path
from fonctions import *

if __name__ == '__main__':

    rejouer = True
    clear()

    if path.isfile('scores'):
        # on recupere les scores si le fichier existe
        scores = charger_score()

    else:
        # on cree le fichier de scores s'il n'existait pas puis, on initialise les scores
        with open('scores', 'w'):
            scores = {}

    username = input('Quel est votre nom d\'utilisateur ? ').lower().strip()
    bienvenue(username, scores)

    while rejouer:
        listeLettres = []
        mots, nbVies = donnees.mots, donnees.nbVies
        mot = mots[randrange(len(mots))].lower()  # choix d'un mot dans le fichier de données
        motAffiche = '*' * len(mot)
        trouve, reponse = False, 'z'

        while nbVies > 0 and not trouve:
            resultat = affiche(nbVies, mot, motAffiche, listeLettres)
            trouve = resultat[0]
            nbVies = resultat[1]
            motAffiche = resultat[2]

            if trouve:
                print(f'Bravo, vous avez gagné!\nVotre Score : {nbVies}\n')
                scores[username] = nbVies
                enregistrer_score(scores)
                break

            elif nbVies == 0:
                print('Dommage, vous avez perdu!')
                print(f'Il fallait deviner le mot {mot}\n')
                break

            try:
                lettre = input('Entrez une lettre... ').strip().lower()[0]
            except:
                print('Erreur: Vous devez entrer une lettre!')

            if lettre in listeLettres:
                clear()
                nbVies += 1
                print(f'Vous avez déjà entré la lettre {lettre}\n')
                continue

            listeLettres.append(lettre)
            clear()

        while reponse not in 'on':
            try:
                reponse = input('Voulez-vous rejouer ? O/N ').strip().lower()[0]
            except:
                print('Erreur: Vous devez entrer une lettre!')

        rejouer = reponse == 'o'
        clear() if rejouer else print('\nBye, Bye!')
