def AddAutomate():
    f=open("automate.txt","w")
    Etats=input("Entrer les diffrents Etats de l'automate :").split(",")
    transitions=input("Entrer les diffentes transitions de l'alphabet :").split(",")
    for etat in Etats:
        entresortie=input("Si Etat "+etat+" initial,entrer 1,si Etat final,entrer 2,si Etat initial et final,entrer 3,si Etat normal,entrer 4 :")
        f.write(entresortie+"*"+etat+":")
        for e in transitions:
            f.write("(")
            etatSuivant=input("Entrer Etat de la transition: "+e)
            print(e,etatSuivant)
            f.write(e+","+etatSuivant)
            f.write(')')
        f.write("\n")
    f.close()






def displayTableAutomate():
    f=open("automate.txt","r")
    lines=f.readlines()
    for line in lines:
        print("---------------------")
        if(line[0]=="1"):
            print("E |"+line[2])
        if(line[0]=="2"):
            print("F |"+line[2])
        if(line[0]=="3"):
            print("EF|"+line[2])
        if(line[0]=="  |4"):
            print(line[2])
    f.close()

displayTableAutomate()