import math
"""=======================================ALGO DE MATH======================================= """
def aire_cube(cote):
    return cote**3

def aire_parallélogramme(base,hauteur):
    return base * hauteur

def  aire_rectangle(longeur,largeur):
    return largeur*longeur

def aire_cercle(rayon):
    return rayon**2*math.pi

def racine_trinome(a,b,c):
    delta = b**2-4*a*c
    if delta < 0:
        return'Erreur, Type Error = Delta négatif'
    elif delta ==0:
        return -b/2*a
    else:
        x1 = (-b+math.isqrt(delta))/(2*a)
        x2 = (-b-math.isqrt(delta))/(2*a)
        return delta,x1,x2
    
def calcul_trinome(a,b,c,x):
    return a*x**2+b*x+c

def maximum(tableau):
    maxi = tableau[0]
    for i in tableau:
        if i > maxi :
            maxi = i 
    return maxi

def dexToBin(nombre):
    quotient = None
    liste = []
    while quotient != 0:
        reste = nombre % 2 
        quotient = nombre // 2 
        nombre = quotient
        liste.append(reste)
    return "".join([str(ele) for ele in liste])
"""=======================================ALGO DE TRI======================================= """
def tri_rapide(tableau):
    if not tableau:
        return []
    else:
        pivot = tableau[-1]
        plus_petit = [x for x in tableau     if x <  pivot]
        plus_grand = [x for x in tableau[:-1] if x >= pivot]
        return tri_rapide(plus_petit) + [pivot] + tri_rapide(plus_grand)

def algo_tri_basique(liste): # Fait un tour de la liste et choisi le plus petit...
    liste_triee = []
    mini = liste[0]
    nb_element_ini = len(liste)
    while len(liste_triee)<nb_element_ini:
        for i in liste :
            if i < mini:
                mini = i 
        liste_triee.append(mini)
        liste.remove(mini) 
        if len(liste) >= 1 :
            mini = liste[0]
    return liste_triee
"""=======================================ALGO NB PREMIERS======================================= """
def nombre_premierQ(nombre):
    compteur = 0
    for i in range(1,nombre+1):
        if nombre % i == 0 :
            compteur += 1 
        if compteur > 2 :
            return False
    if compteur == 2 :
        return True 
    else :
        return False 
def test_nb_premier(nb):
    listeNombrePremier = []
    for i in range(1,nb):
        if nombre_premierQ(i) == True :
            listeNombrePremier.append(i)
    return listeNombrePremier
"""=======================================Fonction sur liste======================================= """
def maxi_liste(liste):  # PAS TESTE !!!
    liste.sort()
    return liste[-1]
def positionDeValDansListe(liste,val):
    trouve = False
    for i in range(len(liste)):
        if liste[i] == val and trouve == False:
            trouve = True
            return i
def inverserChaineCaractère(chaineCaractere):
    t = []
    for i in chaineCaractere:
        t.append(i)
    t.reverse()
    chaineCaractereRenverse = ''.join(t)
    print(chaineCaractereRenverse)
"""======================================= Couleur ======================================= """
def colortext(text,color):
    basicolor="\033[0m"
    if color=="red":
        return("\033[91m"+text+basicolor)
    elif color=="blue":
        return("\033[34m"+text+basicolor)
    elif color=="black":
        return("\033[30m"+text+basicolor)
    elif color=="white":
        return("\033[37m"+text+basicolor)
    elif color=="green":
        return("\033[32m"+text+basicolor)
    elif color=="yellow":
        return("\033[33m"+text+basicolor)
    elif color=="lightred":
        return("\033[31m"+text+basicolor)

if __name__ == "__main__":
    print(racine_trinome(1,-5,6))