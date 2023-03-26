from automate import *

def startMenu():
    print("|-------------Bienvenue--------------|")
    print("|                                    |")
    print("|     Que souhaitez-vous faire ?     |")
    print("|                                    |")
    print("|       1. Voir un automate          |")
    print("|                                    |")
    print("|       2. Sortie                    |")
    print("|------------------------------------|\n")

def controlStartMenu():
    n = controlInput(1,2)
    if (n==1):
        menuAutomate()
        controlAutomate()
    else:
        exit()


def menuAutomate():
    print("|---------Voir un automate-----------|")
    print("|                                    |")
    print("|Choissisez un automate parmis les 44|")
    print("|                                    |")
    print("|------------------------------------|\n")


def controlAutomate():
    global numAutomate
    numAutomate = controlInput(1,44)
    menuAutomate2()
    s = str(numAutomate)
    with open("automateTest/"+s, "r") as f:
        contenu = f.read()
        print(contenu)
    controlAutomate2("automateTest/"+s)



def menuAutomate2():
    print("|-----Que souhaitez-vous faire ?-----|")
    print("|                                    |")
    print("|       1. Voir son type             |")
    print("|                                    |")
    print("|       2. Standardiser l'automate   |")
    print("|                                    |")
    print("|       3. Déterminiser l'automate   |")
    print("|                                    |")
    print("|       4. Completer l'automate      |")
    print("|                                    |")
    print("|       5. Retour                    |")
    print("|------------------------------------|\n")

def controlAutomate2(nomfichier):
    n= controlInput(1,5)
    if (n==1):
        typeAutomate(nomfichier)
        print("")
        menuAutomate2()
        controlAutomate2(nomfichier)
    elif (n==2):
        dico=Standardisation(nomfichier)
        if (dico!=None):
            lignes=dicoToTxt(dico,nomfichier)
            fct(lignes,nomfichier)
            print("")
            menuAutomate2()
            controlAutomate2(nomfichier)
    elif (n==3):
        Determinisation(nomfichier)
        print("")
        menuAutomate2()
        controlAutomate2(nomfichier)
    elif (n==4):
        CompleteAutomate(nomfichier)
        print("")
        menuAutomate2()
        controlAutomate2(nomfichier)
    elif (n == 5):
        startMenu()
        controlStartMenu()


def typeAutomate(nomfichier):
    if isStandard(nomfichier) == True:
        print("L'automate est standard")
    else:
        print("L'automate n'est pas standard")
    if isDeterminist(nomfichier)==True:
        print("L'automate est déterministe")
    else:
        print("L'automate n'est pas déterministe")


def controlInput(min_val, max_val):
    n = int(input("Votre choix : "))

    while (n < min_val or n > max_val):
        print("Erreur, veuillez ressaisir : ")
        n = int(input())

    return n