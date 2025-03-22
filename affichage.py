# -*- coding: utf-8 -*-  # Assure la compatibilité avec les correcteurs et gère les caractères spéciaux

import string

#### REPRESENTATION DES DONNEES
### Initialisation des grilles et autres variables de jeu

n = 'x '  # Symbole pour les noirs
b = 'o '  # Symbole pour les blancs
e = '  '  # Symbole pour les espaces vides

# Grille représentant le début de la partie
grille_debut = [
    [n, n, n, n, n, n, b], 
    [n, n, n, n, n, b, b],
    [n, n, n, n, b, b, b], 
    [n, n, n, e, b, b, b],
    [n, n, n, b, b, b, b], 
    [n, n, b, b, b, b, b],
    [n, b, b, b, b, b, b]     
]

# Grille représentant le milieu de la partie
grille_milieu = [
    [n, e, n, e, e, b, e], 
    [e, e, e, e, e, e, e],
    [e, e, n, e, n, e, e], 
    [e, e, e, e, e, b, b],
    [e, e, n, b, e, b, e], 
    [e, e, e, e, e, e, e],
    [e, b, e, e, e, b, e]     
]

# Grille représentant la fin de la partie
grille_fin = [
    [e, e, e, e, e, e, e], 
    [e, e, e, n, e, e, e],
    [e, n, e, e, n, e, e], 
    [e, e, b, e, e, b, e],
    [e, e, e, e, b, e, e], 
    [e, e, e, e, e, e, e],
    [e, e, e, e, e, e, e]     
]

# Légende pour l'affichage des colonnes (A à G)
overlay = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# ---- Affichage ----
def afficher_grille(grille):
    """
    Affiche une grille de jeu avec la numérotation des colonnes et des lignes.
    """
    print('    1  2  3  4  5  6  7') 
    print('------------------------')
    for i in range(7):
        print(overlay[i] + ' | ', end="")  # Affiche la lettre de la ligne
        for y in range(7):
            print(grille[i][y], end=" ")  # Affiche le contenu de la grille
        print()  # Passe à la ligne suivante


# ---- Vérification du format de la saisie ----

def est_au_bon_format(saisie_utilisateur):
    """
    Vérifie si la saisie est bien au format attendu : une lettre (A-G ou a-g) suivie d’un chiffre (1-7).
    """
    if len(saisie_utilisateur) != 2: 
        return False  # La saisie doit être exactement de 2 caractères
    
    lettre = saisie_utilisateur[0].upper()  # Convertit la lettre en majuscule pour éviter les erreurs de casse
    chiffre = saisie_utilisateur[1]  # Récupère le chiffre sous forme de caractère

    if lettre not in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        return False  # Vérifie que la lettre est bien dans l’intervalle valide
    
    if chiffre not in ['1', '2', '3', '4', '5', '6', '7']:
        return False  # Vérifie que le chiffre est compris entre 1 et 7
    
    return True  # Si toutes les conditions sont respectées, la saisie est valide


# ---- Tests de validation ----

def test_est_au_bon_format():
    """
    Teste la fonction est_au_bon_format avec plusieurs cas valides et invalides.
    """
    assert est_au_bon_format("A1") == True  # Cas normal
    assert est_au_bon_format("G7") == True  # Dernière colonne et ligne valides
    assert est_au_bon_format("a3") == True  # Lettre minuscule acceptée
    assert est_au_bon_format("H1") == False  # Lettre hors de la grille
    assert est_au_bon_format("A8") == False  # Chiffre hors de la grille
    assert est_au_bon_format("11") == False  # Deux chiffres (mauvais format)
    assert est_au_bon_format("A") == False  # Manque le chiffre
    assert est_au_bon_format("1A") == False  # Mauvais ordre
    assert est_au_bon_format("A0") == False  # Chiffre 0 non valide
    assert est_au_bon_format("") == False  # Chaîne vide
    assert est_au_bon_format("AB") == False  # Deux lettres
    print("Tous les tests de est_au_bon_format sont réussis !")


# ---- Vérification si une coordonnée est dans la grille ----

def est_dans_grille(ligne, colonne):
    """
    Vérifie si une case est bien dans les limites de la grille (A-G et 1-7).
    """
    try:
        return ligne.upper() <= 'G' and 1 <= int(colonne) <= 7
    except ValueError:
        return False  # Retourne False si colonne ne peut pas être converti en entier


def test_est_dans_grille():
    """
    Teste la fonction est_dans_grille avec plusieurs valeurs limites et erreurs possibles.
    """
    assert est_dans_grille('A', 1) == True  # Coin supérieur gauche
    assert est_dans_grille('G', 7) == True  # Coin inférieur droit
    assert est_dans_grille('H', 1) == False  # Lettre hors grille
    assert est_dans_grille('A', 8) == False  # Chiffre hors grille
    assert est_dans_grille('a', 5) == True   # Minuscule acceptée
    assert est_dans_grille('B', '3') == True # Chiffre sous forme de chaîne
    assert est_dans_grille('D', 'x') == False # Chiffre invalide
    print("Tous les tests de est_dans_grille sont réussis !")


# ---- Affichage du jeu ----

def display(titre, grille, tour_joueur):
    """
    Affiche l'état actuel de la partie et indique à quel joueur de jouer.
    """
    print('\nGrille de ' + titre + ' de partie')
    afficher_grille(grille)
    print('Joueur ' + tour_joueur + ', veuillez jouer')


def saisir_coordonnees () : 
    
    pion_a_bouger = input ('Veuillez saisir les coordonnées du pion à bouger :  ')
    assert est_au_bon_format(pion_a_bouger), "Erreur, le coup joué n'est pas au bon format"
    assert est_dans_grille(pion_a_bouger[0], pion_a_bouger[1]), "Erreur, le coup joué n'est pas dans la grille"
    
    position_joue = input ('Veuillez saisir les coordonnées de la position à jouer :  ')
    assert est_au_bon_format(position_joue), "Erreur, le coup joué n'est pas au bon format"
    assert est_dans_grille(position_joue[0], position_joue[1]), "Erreur, le coup joué n'est pas dans la grille"
    
    print()
    

# ---- Code principal ----

# Affichage des différentes étapes du jeu

display('début', grille_debut, 'blanc')
input("Tapez entrer pour passer à la configuration suivante ")

display('milieu', grille_milieu, 'noir')
input("Tapez entrer pour passer à la configuration suivante ")

display('fin', grille_fin, 'noir')
saisir_coordonnees()

# Exécution des tests
test_est_dans_grille()
test_est_au_bon_format()

