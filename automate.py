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
    transition=[]
    f=open("automate.txt","r")
    lines=f.readlines()
    checkTransitions=lines[0].split(":")[1].split("(")
    for e in checkTransitions:
        if(e!=""):
            transition+=e[0]
    print("    ",end="")
    for transi in transition:
        print("|"+transi+"|",end="")
    print("")
    for line in lines:
        print("---------------------")
        if(line[0]=="1"):
            print("E |"+line[2]+"|",end="")
        if(line[0]=="2"):
            print("F |"+line[2]+"|",end="")
        if(line[0]=="3"):
            print("EF|"+line[2]+"|",end="")
        if(line[0]=="  |4"):
            print(line[2],end="")
        for e in transition :
            print(line[line.find(e)+2]+"|",end="")
        print("")   
    f.close()

def isAutomatefull() :
    f=open("automate.txt","r")
    lines=f.readlines()
    for line in lines:
        if (line.find("-")!=-1):
            return False
    return True



print(isAutomatefull())