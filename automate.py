def AddAutomate():
    f=open("automate.txt","a")
    f.write(";\n")
    finis=0
    while finis==0:
        Etat=input("Entrer le nom de l'Etat :")
        f.write(Etat+":(")
        NoMoreTransitions=0
        while NoMoreTransitions==0:
            transition,etatSuivant=input("Entrer transition,Etat :").split(",")
            print(transition,etatSuivant)
            f.write(transition+","+etatSuivant)
            NoMoreTransitions=int(input("finis ?,0=non,1=oui :"))
            f.write(')')
        finis=int(input("finis ?,0=non,1=oui :"))
        f.write("\n")
    f.write(";")
    f.close()

AddAutomate()