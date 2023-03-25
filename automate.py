from boiteOutilsRomain import colortext
from os import system

def convertAutomateToDict():
    """
    Cette fonction transforme le doc txt en format dict python
    la syntaxe est la suivante :
    dict = {"A":[1,['a','2'],['b','3','2'],['c','-1']],
            "B":[4,['a','2'],['b','3','2'],['c','-1']]} 
    le tout premier element de la liste dit si c une E/S/ES/rien
    """
    dico = {}
    f=open("automate.txt","r")
    lines=f.readlines()
    f.close()
    #recuperation des transitions ['a','b',...]
    transition=[]
    checkTransitions=lines[0].split(":")[1].split("(") 
    for e in checkTransitions: # hop recyclage
        if(e!=""):
            transition+=e[0]
    for line in lines :
        listeCle = [] # liste cle est la liste de la valeur du dico et la sous liste est la liste des transition et des etats d'arrivé dans l'ex c'est [a,2]
        listeCle.append(int(line[0])) # ajout de l'info E/S/ES
        for i in range (len(transition)):
            sousliste = []
            if line[line.find(transition[i])+3] != ')' :  # cas ou il y a plusieurs etat d'arrivée 
                ligneRaccouci = line[line.find(transition[i]):] # si il y a plrs etat d'arrive alors je raccourci la ligne pour que ce soit plus simple ex : b,2,3)(c,-)(d,-)
                for j in range(ligneRaccouci.find(')')): # enfin dans cette ligne raccourcie les etats sont en position 2,4,6,... et je vais jusquau prochain ')'(qui est le premier de la ligne raccouci)
                    if j%2 == 0 :
                        sousliste.append(ligneRaccouci[j]) # a noter que a l'index zero on prend le 'b' de l'exemple du dessus
            else : # cas ou il y a que 1 etat d'arrivé ou aucun (-1)
                sousliste.append(transition[i])
                sousliste.append(line[line.find(transition[i])+2] if line[line.find(transition[i])+2] != '-' else "-1"  )
            listeCle.append(sousliste)
        dico[line[2]] =listeCle
    return dico

def afficherDicoPropre(dico):
    for ele in dico:
        print(ele,'\t',dico[ele])

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
            temp=line.split(e)[1]
            if (temp[2]==")"):
                print(temp[1]+"\t|\t",end="")
            else:
                while(temp[2]!=")"):
                    print(temp[1],end="")
                    temp=temp[2:]
                print(temp[1]+"\t|\t",end="")
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

def isDeterminist():
    if(HowManyEntry()>1):
        return False
    if(AreTransitionWithMoreThanOneState()):
        return False
    return True

def isStandard():
    if(HowManyEntry()>1):
        return False
    if(AreTransitionToEntry()):
        return False
    return True



def Standardisation():
    if(isStandard()):
        print("L'automate est déjà standard")
        return 
    automateDico = convertAutomateToDict()
    listeDesEntrees = WhatAreEntry()
    Etat_i = {"I":[[ele,'-1'] for ele in WhatAreTransitions() ]}
    #Etat_i["I"].insert(0,1)
    print(Etat_i)
    afficherDicoPropre(automateDico)
    listeDesValeursDesEtatsEntree = [] #isoler les cles qui nous interesse
    
    for etat in listeDesEntrees:
        listeDesValeursDesEtatsEntree.append(automateDico[etat]) # on recup que les values des E et E/S de dico
    print('--')
    for listeDesTransition in listeDesValeursDesEtatsEntree: # pour chaque [['a', '-1'], ['b', '-1'], ['c', '-1'], ['d', '-1']] dans la liste
        listeDesTransition = listeDesTransition[1:]
        print(listeDesTransition)
        for i in range(len(listeDesTransition)):
            print("listes des transitions ",listeDesTransition[i])
            print("etat i :",Etat_i["I"])
            if listeDesTransition[i][1:][0] != '-1': # si ça mene nul part pas besoin de copier
                print("pasVide")
                if Etat_i["I"][i][1] == '-1':
                    print("i est vide")
                    Etat_i["I"][i].remove("-1")
            
                for ele in listeDesTransition[i][1:] :
                    if ele not in Etat_i["I"][i] :
                        Etat_i["I"][i].append(ele)
                    print("ele =",ele)

                    
                


            print("apres if ",Etat_i["I"])
    print("final ",Etat_i)
            
def getTransitionOfOneState(state):
    f=open("automate.txt","r")
    lines=f.readlines()
    f.close()
    newlines=[]
    if ("/"not in state[0]) :
        for w in state:
            for line in lines:
                if line[2] == state[0]:    
                    newlines=line.split(":")[1].split("(")[1:]
                    return [e.replace(")","").replace("\n","") for e in newlines]
    else:
        print("2/1?",state)
        states=state[0].split("/")
        transition=""
        for state in states:
            print(state)
            for line in lines:
                if line[2] == state[0]:
                    newlines=line.split(":")[1].split("(")[1:]
                    tempTransition=[e.replace(")","").replace("\n","") for e in newlines]
            transition=addTwoStateTransition(transition,tempTransition)
            print(transition)
        return transition

def addTwoStateTransition(transitions1,transitions2):
    if(len(transitions1)==0):
        return transitions2
    if(len(transitions2)==0):
        return transitions1
    newTransitions=[]
    tempTransi1=""
    tempTransi2=""
    temp=[] #Recupere les transitions qui sont dans les deux etats avant de les stringify
    for i in range (len(transitions1)):
        if (transitions1[i]==transitions2[i]):
            newTransitions.append(transitions1[i])
        else:
            tempTransi1=transitions1[i].split(",")
            temp=tempTransi1
            tempTransi2=transitions2[i].split(",")
            for e in tempTransi2:
                if e not in temp:
                    temp.append(e)
            if (len(temp)>2 and "-" in temp):
                for e in temp:
                    if "-" in e:
                        temp.remove(e)
            newTransitions.append(",".join(temp)) #Veut pas join si "-"  dans la liste car devient null
    return newTransitions
            

        



   
            
def Determinisation(nomFichier):
    if(isDeterminist()):
        print("L'automate est déjà déterministe")
        return
    EtatsDone=[]
    EtatsToDo=[]
    newEtat=[] 
    fichier=open(nomFichier,"r")
    lines=fichier.readlines()
    fichier.close()
    Etat1=lines[0][0]
    transitionEtat1=getTransitionOfOneState(Etat1)
    for i in range(len(transitionEtat1)):
        if(len(transitionEtat1[i])>3):
            transitionEtat1[i]=CreateNewTransitionForDeter(transitionEtat1[i])
    print(transitionEtat1)
    newEtat+=Etat1,transitionEtat1
    EtatsDone+=Etat1
    for e in transitionEtat1:
        if(e.split(",")[1:] not in EtatsToDo):
            EtatsToDo.append(e.split(",")[1:])
            for e in EtatsToDo:
                if("-" in e):
                    if("/"not in e):
                        EtatsToDo.remove(e)
                    else :
                        e=e.replace("-","").replace("/","")
    print("EtatsToDo1",EtatsToDo)

    while(len(EtatsToDo)>0):
        Etat=EtatsToDo[0]
        EtatsDone.append(Etat)
        EtatsToDo.remove(Etat)
        transitionEtat=getTransitionOfOneState(Etat)
        print("HERE",Etat)
        for i in range(len(transitionEtat)):
            if(len(transitionEtat[i])>3):
                transitionEtat[i]=CreateNewTransitionForDeter(transitionEtat[i])
        newEtat+=Etat,transitionEtat
        for e in transitionEtat:
            if(e.split(",")[1:] not in EtatsDone and e.split(",")[1:] not in EtatsToDo):
                EtatsToDo.append(e.split(",")[1:])
                for e in EtatsToDo:
                    if("-" in e):
                        if("/"not in e):
                            EtatsToDo.remove(e)
                        else :
                            e=e.replace("-","").replace("/","")
                print("EtatsToDo2",EtatsToDo)
    convertnewEtatToTxt(newEtat,nomFichier)  
    return

def convertnewEtatToTxt(newEtat,fichiertxt):
    print("NEW ETAT",newEtat)
    fonctions=[]
    for i in range (len(newEtat)):
        if(i%2==0):
            fonctions.append(getFonctionOfAState(fichiertxt,newEtat[i]))
    print(fonctions)
    f=open(fichiertxt,"w")
    for i in range(len(newEtat)):
        if(i%2==0):
            if("/" not in newEtat[i]):
                print("index",i,fonctions) #fonctions[i] ressort un trois au lieu d'un 2
                if (i!=0):
                    f.write(fonctions[int(i/2)]+"*")
                else:
                    f.write(fonctions[i]+"*")
                if(type(newEtat[i])==list):
                    f.write(newEtat[i][0]+":")
                else:
                    f.write(newEtat[i]+":")
        else:
            for e in newEtat[i]:
                f.write("("+e+")")            
            f.write("\n")
    f.close()

def getFonctionOfAState(fichier,e):
    f=open(fichier,"r")
    lines=f.readlines()
    f.close()
    if("/" in e[0]):
        allfonction=[]
        if(type(e)==list):
            e=e[0].split("/")
        else:
            e=e.split("/")
        for y in e :
            allfonction.append(getFonctionOfAState(fichier,y))
        print("ALL FONCTION",e,allfonction)
        if ("3" in allfonction) :
            return "3"
        if ("2" and "4" in allfonction):
            return "2"
        if ("1" and "4" in allfonction):
            return "1"
        if("1" and "2" in allfonction):
            return "3"
        if("1" in allfonction):
            return "1"
        if("2" in allfonction):
            return "2"
        else :
            return "4"
    
    for line in lines:
        if(type(e)==list):
            if line[2]==e[0]:
                return str(line[0])
        else: 
            if line[2]==e:
                return str(line[0])


def CreateNewTransitionForDeter(transition):
    newTransition=""
    elements=transition.split(",")
    newTransition+=elements[0]+","
    for e in elements[1:]:
        if (len(newTransition)<3):
            newTransition+=e
        else :
            newTransition+="/"+e
    return newTransition

    


def CompleteAutomate(): 
    if(isAutomatefull()):
        print("L'automate est déjà complet")
        return
    transitions=WhatAreTransitions()
    f=open("automate.txt","r")
    newline=[]
    lines=f.readlines()
    for line in lines:
        line=line.replace("-","P")
        newline.append(line)       
    f.close()
    f=open("automate.txt","w")
    for e in newline :     
        f.write(e)
    f.write("\n4*P:")
    for y in transitions:
        f.write("("+y+",P)")
    f.close()




def WhatAreEntry():
    entry=[]
    f=open("automate.txt","r")
    lines=f.readlines()
    f.close()
    for line in lines:
        if(line[0]=="1" or line[0]=="3"):
            entry.append(line[2])
    return entry

def WhatAreEtat():
    etat = []
    f=open("automate.txt","r")
    lines=f.readlines()
    f.close()
    for line in lines:
        etat.append(line[2])
    return etat        

def WhatAreTransitions():
    f=open("automate.txt","r")
    lines=f.readlines()
    f.close()
    #recuperation des transitions ['a','b',...]
    transition=[]
    checkTransitions=lines[0].split(":")[1].split("(") 
    for e in checkTransitions: # hop recyclage
        if(e!=""):
            transition+=e[0]
    return transition

def AreTransitionToEntry():
    entry=WhatAreEntry()
    f=open("automate.txt","r")
    lines=f.readlines()
    f.close()
    for line in lines:
        line=line.split(":")[1]
        for e in entry:
            if(line.find(e)!=-1):
                return True
    return False

def AreTransitionWithMoreThanOneState():
    f=open("automate.txt","r")
    lines=f.readlines()
    f.close()
    for line in lines:
        line=line.split(":")[1]
        line=line.split("(")
        for e in line:
            if(e.count(",")>1):
                return True
    return False




if __name__ == "__main__":
    system("cls")
    print("Transition de 21",getTransitionOfOneState("2/1"))
    print("Transition de 3",getTransitionOfOneState("3"))
    Determinisation("automate.txt")
    #print(Determinisation("automate.txt"))

  
   