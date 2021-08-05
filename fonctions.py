from os import system, name
from pickle import Pickler, Unpickler


def affiche(nbVies, mot, motAffiche, listeTentatives):
    chaine = str()
    trouve = True

    for elt in mot:
        if elt in listeTentatives:
            chaine += elt
        else:
            chaine += '*'
            trouve = False

    if len(listeTentatives) > 0 and motAffiche == chaine:
        nbVies -= 1

    print(f'Vies Restantes: {nbVies}')
    print(chaine, end='\n\n')

    return [trouve, nbVies, chaine]


def clear():
    _ = system('cls') if name == 'nt' else system('clear')


def charger_score():
    with open('scores', 'rb') as scoresFile:
        p = Unpickler(scoresFile)
        scores = p.load()
    return scores


def enregistrer_score(scores):
    with open('scores', 'wb') as scoresFile:
        p = Pickler(scoresFile)
        p.dump(scores)


def bienvenue(username, scores):
    if username in scores.keys():
        # afficher le meilleur score si le joueur est connu
        print(f'Rebonjour {username}! Votre meilleur score est de {scores[username]} pts\n')
    else:
        # souhaiter la bienvenue au nouveau joueur et initialiser son score à 0
        print(f'Bienvenue {username}!\n')
        scores[username] = 0
        enregistrer_score(scores)