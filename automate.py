from boiteOutilsRomain import colortext
from os import system
def AddAutomate():
    f=open("automate.txt","w")
    Etats=input("Entrer les differents Etats de l'automate :").split(",")
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
    print(transition)
    print(colortext('E',"blue")+'\t',end='')
    for transi in transition:
        print("|\t"+colortext(transi,"red")+"\t",end="")
    print("|")
    for line in lines:
        print("-"*len(transition)*18)
        if(line[0]=="1"):
            print(colortext("E ","green") +"|"+line[2]+"\t|\t",end="")
        if(line[0]=="2"):
            print(colortext("S ","lightred") +"|"+line[2]+"\t|\t",end="")
        if(line[0]=="3"):
            print("ES|"+line[2]+"\t|\t",end="")
        if(line[0]=="  \t|\t4"):
            print(line[2],end="")
        for e in transition :
            print(line[line.find(e)+2]+"\t|\t",end="")
        print("")   
    f.close()

def isAutomatefull() :
    f=open("automate.txt","r")
    lines=f.readlines()
    for line in lines:
        if (line.find("-")!=-1):
            return False
    return True

def HowManyEntry():
    compteur=0
    f=open("automate.txt","r")
    lines=f.readlines()
    f.close()
    for line in lines:
        if(line[0]=="1" or line[0]=="3"):
            compteur+=1
    return compteur



if __name__ == "__main__":
    displayTableAutomate()