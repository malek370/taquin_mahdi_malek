import copy
from cProfile import label
from cgitb import text
from glob import glob
from re import L
from struct import pack
from tkinter import *
from random import shuffle
import tkinter

graph=[]
res=""
lim=1
def affich(t):
    for i in range(3):
        for j in range(3):
            print(t[i][j])
        print("\n")

def etat_depart():
    return [[1,2,3],[8,6,0],[7,5,4]]
    
def etat_final(t):
    l=[[1,2,3],[8,0,4],[7,6,5]]
    ok=True
    for i in range(3):
        for j in range(3):
           if (t[i][j]!=l[i][j]):
               return False
    return ok 

def position_case_vide(t):
    for i in range(3):
        for j in range(3):
            if (t[i][j]==0):
                return i,j

def numero(t,x,y):
    return t[x][y]

def permuter(t,c1,c2):
    x1=c1[0]
    y1=c1[1]
    x2=c2[0]
    y2=c2[1]
    aux=t[x1][y1]
    t[x1][y1]=t[x2][y2]
    t[x2][y2]=aux
    return t

def transitions(etat):
    l=[]
    l.append(etat)
    x,y=position_case_vide(etat)
    if (x!=0):
        cop=copy.deepcopy(etat)
        cop=permuter(cop,[x,y],[x-1,y])
        l.append(cop)
    if (x!=2):
        cop=copy.deepcopy(etat)
        cop=permuter(cop,[x,y],[x+1,y])
        l.append(cop)
    if (y!=0):
        cop=copy.deepcopy(etat)
        cop=permuter(cop,[x,y],[x,y-1])
        l.append(cop)
    if (y!=2):
        cop=copy.deepcopy(etat)
        cop=permuter(cop,[x,y],[x,y+1])
        l.append(cop)
    return l


#bfs
def bfs():
    global res
    global graph
    etat=etat_depart()
    l=[etat]
    visites=[]
    graph.append(l[0])
    k=1
    while l:
        node=l.pop(0)
        k=k+1
        visites.append(node)
        graph.append(copy.deepcopy(node))
        if (etat_final(node)):
            graph.append(copy.deepcopy(node))
            res="nombre d'etats visités: {}\nnombre de clos: {}".format(len(visites),k)
            print(res)
            return 0
        possiblepaths=transitions(node)
        lis=[]
        print("noeud a derive",node)
        for i in possiblepaths:
            if i not in visites:
                l.append(i)
                graph.append(i)
                lis.append(i)
        for j in lis:
            print(j)
            graph.append(j)
            graph.append(copy.deepcopy(node))

#dfs_l
def inp():
    global lim
    lim=tk.get()
    
def dfs_l():
    global lim
    global res
    global graph
    etat=etat_depart()
    l=[etat]
    visites=[]
    print("droit gauche en haut en bas")
    print('etat initiale',l[0])
    graph.append(l[0])
    limite=int(lim)
    p=1
    while l and (p<=limite):
        node=l.pop(0)
        visites.append(node)
        if (etat_final(node)):
            res=" etat visite: {}".format(len(visites))
            return 0
        possiblepaths=transitions(node)
        lis=[]
        x=[]
        print("noeud a derive",node)
        graph.append(copy.deepcopy(node))
        for i in possiblepaths:
            if i not in visites:
                x.append(i)
                graph.append(i)
                graph.append(copy.deepcopy(node))
                visites.append(i)
                if (etat_final(i)):
                    print("fin",i)
                    graph.append(i)
                    print("nombre d'etats visités",len(visites))
                    res="nombre d'etat visite: {}".format(len(visites))
                    return 0
                else:
                    lis.append(i)
        l=x+l
        p=p+1
##        for i in reversed (range(0,len(possiblepaths))):
##            if possiblepaths[i] not in visites:
##                l.insert(0,possiblepaths[i])
            
        for j in lis:
            print(j)
        
    if (p>limite):
         print("pas de solution dans ce limite")
         res="pas de solution dans ce limite"
         return 0


        
def dfs():
    global graph
    global res
    etat=etat_depart()
    l=[etat]
    visites=[]
    print("droit gauche en haut en bas")
    print('etat initiale',l[0])
    graph.append(l[0])
    while l:
        node=l.pop(0)
        visites.append(node)
        if (etat_final(node)):
            graph.append(copy.deepcopy(node))
            res="nombre d'etats visités: {}".format(len(visites))
            print(res)
            return 0
        possiblepaths=transitions(node)
        lis=[]
        print("noeud a derive",node)
        graph.append(copy.deepcopy(node))
        for i in possiblepaths:
            if i not in visites:
                l.insert(0,i)
                graph.append(i)
                lis.append(i)
        for j in lis:
            print(j)
            graph.append(j)
            graph.append(copy.deepcopy(node))

def somme(etat):
    final=[[1,2,3],[8,0,4],[7,6,5]]
    s=0
    for i in range(3):
        for j in range(3):
            if (etat[i][j]!=final[i][j]) and (etat[i][j]!=0):
                s=s+1
    return s

def sort(l):
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            if somme(l[i])>somme(l[j]):
                aux=l[i]
                l[i]=l[j]
                l[j]=aux
##def find_key(v): 
##    for k, val in color_dict.items(): 
##        if v == val: 
##            return k
##def add_value(dict_obj, key, value):
##    if key not in dict_obj:
##        dict_obj[key] = value
##    elif isinstance(dict_obj[key], list):
##        dict_obj[key].append(value)
##    else:
##        dict_obj[key] = [dict_obj[key], value]
##
##def first_value(dic):
##    l=[]
##    for cle in dic.keys():
##        l.append(cle)
####def dfs_l():
##    global graph
##    global res
##    etat=etat_depart()
##    visites=[]
##    l={}
##    l[0]=etat
##    y=0
##    while l:
##        liste = [[item, l[item]] for item in l]
##        node1=liste.pop(0)
##        l = {}
##        for item in liste:
##            if item[0] not in l:
##                l[item[0]] = item[1]
##        visites.append(node1[1])
##        if (etat_final(node1[1])):
##            res="nombre d'etats visités: {}\nnombre de clos: {}".format(len(visites),k)
##            return 0
##        if (node1[0]<3):
##            y=y+1
##            k={}
##            possiblepaths=transitions(node)
##            lis=[]
##            print("noeud a derive",node)
##            for i in possiblepaths:
##                if i not in visites:
##                    visites.append(i)
##                    add_value(k,y,i)
##                    lis.append(i)
##            l={**k,**l}
##            for j in lis:
##                print(j)
##                    
                    
                    
             
            
###res = {**updict, **test_dict}    
##def heuristique():
##    etat=etat_depart()
##    visites=[]
##    l={}
##    l[0]=etat
##    x=list(l.keys())
##    i=x[0]
##    print("droit gauche en haut en bas")
##    print('etat initiale',l[i])
##    m=0
##    while l and m<2:
##        node=l.pop(i)
##        visites.append(node)
##        if (etat_final(node)):
##            return 0
##        possiblepaths=transitions(node)
##        lis=[]
##        print("noeud a derive",node)
##        
##        for i in possiblepaths:
##            if i not in visites:
##                y=somme(i)
##                l[y]=i
##                visites.append(i)
##                if (etat_final(i)):
##                    
##                    print("fin",i)
##                    print("nombre d'etats visités",len(visites))
##                    return 0
##                else:
##                    lis.append(i)
##        for j in lis:
##            print(j)
##            
##        l=dict(sorted(l.items()))
##        x=list(l.keys())
##        i=x[0]
##        m=m+1


def heuristique_1():
    global graph
    global res
    etat=etat_depart()
    visites=[]
    l=[etat]
    k=1
    graph.append(l[0])
    while l:
        node=l.pop(0)
        visites.append(node)
        if (etat_final(node)):
            graph.append(copy.deepcopy(node))
            res="nombre d'etats visités: {}\nnombre de clos: {}".format(len(visites),k)
            print(res)
            return 0
        possiblepaths=transitions(node)
        lis=[]
        print("noeud a derive",node)
        graph.append(copy.deepcopy(node))
        for i in possiblepaths:
            if i not in visites:
                l.append(i)
                k=k+1
                graph.append(i)
                lis.append(i)       
        sort(l)
        for j in lis:
            print(j)
            graph.append(j)
            graph.append(copy.deepcopy(node))


window=Tk()
window.title("taquin")
window.geometry("1000x700")
window.minsize(1200,700)
window.config(background="#B82736")
frame=Frame(window,bg="#B82736")
FONT=('Ubuntu', 27, 'bold')
cnv=Canvas(frame, width=300, height=300, bg='red')
cnv.pack(expand=YES)

def reo():
    global graph
    game=graph.pop(0)
    for i in range(3):
        for j in range(3):
            x, y=100*j, 100*i
            A, B, C=(x, y), (x+100, y+100), (x+50, y+50)
            if game[i][j]!=0:
                rect = cnv.create_rectangle(A, B, fill="black")
                txt = cnv.create_text(C, text=game[i][j], fill="red",font=FONT)
            else:
                rect = cnv.create_rectangle(A, B, fill="red")
                txt = cnv.create_text(C, text=game[i][j], fill="red",font=FONT)
    if(graph):
        window.after(500,reo)
    else:
        msg.set(res)
    
def reo_a():
    msg.set('heuristique')
    global graph
    n=heuristique_1()
    reo()    

def reo_dfs():
    global graph
    msg.set("profondeur d abord")
    n=dfs()
    reo()

def reo_bfs():
    global graph
    msg.set("largeur d abord")
    n=bfs()
    reo()

def reo_dfs_l():
    global graph
    msg.set("profondeur d abord limite")
    n=dfs_l()
    reo()

def new_game():
    graph.clear()
    game=etat_depart()
    msg.set("choisir la methode")
    tk.delete(0,'end')
    global lim
    lim =0
    for i in range(3):
        for j in range(3):
            x, y=100*j, 100*i
            A, B, C=(x, y), (x+100, y+100), (x+50, y+50)
            if game[i][j]!=0:
                rect = cnv.create_rectangle(A, B, fill="black")
                txt = cnv.create_text(C, text=game[i][j], fill="red",font=FONT)
            else:
                rect = cnv.create_rectangle(A, B, fill="red")
                txt = cnv.create_text(C, text=game[i][j], fill="red",font=FONT)

tk=Entry(window)
submit=Button(window,text="entrer",bg='#dee5dc',font=("Courrier",25),fg="black",command=inp)  
dfs_bt=Button(frame,text="profondeur d abord",bg='#dee5dc',font=("Courrier",25),fg="black",command=reo_dfs)
dfsl_bt=Button(frame,text="profondeur d abord limite",bg='#dee5dc',font=("Courrier",25),fg="black",command=reo_dfs_l)
bfs_bt=Button(frame,text="largeur d abord",bg='#dee5dc',font=("Courrier",25),fg="black",command=reo_bfs)
astar_bt=Button(frame,text="heuristique",bg='#dee5dc',font=("Courrier",25),fg="black",command=reo_a)
new_bt=Button(frame,text="nouveau jeu",bg='#dee5dc',font=("Courrier",25),fg="black",command=new_game)


#tk.pack(side=RIGHT)
tk.place(x=950,y=200)
submit.place(x=950,y=250)
dfs_bt.pack(side=BOTTOM)
dfsl_bt.pack(side=BOTTOM)
bfs_bt.pack(side=BOTTOM)
astar_bt.pack(side=BOTTOM)
new_bt.pack(side=BOTTOM)
frame.pack(side=BOTTOM)


game=etat_depart()
msg=tkinter.StringVar()
msg.set("choisir la methode")
w = Label(textvariable =msg, font = "90",fg="Navyblue") 
w.pack()
for i in range(3):
    for j in range(3):
        x, y=100*j, 100*i
        A, B, C=(x, y), (x+100, y+100), (x+50, y+50)
        if game[i][j]!=0:
            rect = cnv.create_rectangle(A, B, fill="black")
            txt = cnv.create_text(C, text=game[i][j], fill="red",font=FONT)
        else:
            rect = cnv.create_rectangle(A, B, fill="red")
            txt = cnv.create_text(C, text=game[i][j], fill="red",font=FONT)




window.mainloop()
