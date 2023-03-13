def AddAutomate():
    f=open("automate.txt","a")
    f.write(";\n")
    finis=0
    Etats=input("Entrer les diffrents Etats de l'automate :").split(",")
    transitions=input("Entrer les diffentes transitions de l'alphabet :").split(",")
    for etat in Etats:
        entresortie=input("Si Etat initial,entrer 1,si Etat final,entrer 2,si Etat initial et final,entrer 3,si Etat normal,entrer 4 :")
        f.write(entresortie+"*"+etat+":")
        for e in transitions:
            f.write("(")
            etatSuivant=input("Entrer Etat de la transition: "+e)
            print(e,etatSuivant)
            f.write(e+","+etatSuivant)
            f.write(')')
        f.write("\n")
    f.write(";")
    f.close()






def displayAutomate():
    f=open("automate.txt","r")
    print(f.read())
    f.close()


AddAutomate()