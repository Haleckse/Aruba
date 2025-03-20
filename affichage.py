1 # -*- coding: utf-8 -*- ## Pour s’assurer de la compatiblite entre correcteurs
2
3 #### REPRESENTATION DES DONNEES
4 ###initialisation des grilles et autres variables de jeu
6

n = 'x '
b = 'o '
e = '  '

grille_debut = [
    [n, n, n, n, n, n, b], 
    [n, n, n, n, n, b, b],
    [n, n, n, n, b, b, b], 
    [n, n, n, e, b, b, b],
    [n, n, n, b, b, b, b], 
    [n, n, b, b, b, b, b],
    [n, b, b, b, b, b, b]     
]

overlay = ['A', 'B', 'C', 'D', 'E', 'F', 'G']



# ---- Affichage ----
def afficher_grille(grille):
 
    print('    1  2  3  4  5  6  7') 
    print('------------------------')
    for i in range(7):
        print(overlay[i] + ' | ', end="") 
        for y in range(7):
            print(grille_debut[i][y], end=" ")  # Affiche sur la même ligne
        print()  # Change de ligne après chaque ligne du plateau


# # ---- Saisie ----
# def test_est_dans_grille():
#     assert ...

# def est_dans_grille(ligne, colonne, grille):
#     ...

# def saisir_coordonnees():
#     ...

# # ---- Code Principal ----
afficher_grille(grille_debut)
# afficher_grille(grille_milieu)
# afficher_grille(grille_fin)

# test_est_dans_grille()

# print(saisir_coordonnees())
