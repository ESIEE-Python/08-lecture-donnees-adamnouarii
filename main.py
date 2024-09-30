"""
module permettant de lire un fichier
"""
import csv
#### Imports et définition des variables globales

FILENAME = "listes.csv"
#### Fonctions secondaires
def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode = 'r', encoding ='utf8') as f :
        r = csv.reader(f, delimiter=';')
        l=list(r)
        liste_int=[[int(i) for i in s] for s in l]
    return liste_int

def get_list_k(liste, k):
    """
    retourne la k-ième liste d'une liste
    """
    return liste[k]

def get_first(liste):
    """
    retourne le premier element d'une liste
    """
    return liste[0]

def get_last(liste):
    """
    retourne le dernier element d'une liste
    """
    return liste[-1]

def get_max(liste):
    """
    retourne le maximum d'une liste
    """
    maximum = liste[0]
    for i in liste :
        maximum = max(maximum,i)
    return maximum

def get_min(liste):
    """
    retourne le minimum d'une liste
    """
    minimum = liste[0]
    for i in liste :
        minimum = min(minimum,i)
    return minimum

def get_sum(liste):
    """
    retourne la somme d'une liste
    """
    s = 0
    for k in liste:
        if isinstance(k, (int, float)):
            s+=k
    return s




#### Fonction principale


def main():
    """
    Appels aux fonctions secondaires pour tester le fonctionnement
    """
    liste1 = [1,2,3]
    print(get_sum(liste1))
    print(get_min(liste1))
    filename = 'listes.csv'
    data = read_data(filename)
    print(data)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
