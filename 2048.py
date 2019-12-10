#PREPARATION
from tkinter import *
from random import *
from math import log2
fen = Tk()
fen.title("2048")
grille=[]
with open('grille.txt','r') as fichier:
    grille=fichier.read()
    grille=grille.split(',')
for e in range(len(grille)):
    grille[e]=int(grille[e])

grille2=[]
lab=[]
won=0
fusionned=[]
hexa = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

#FONCTION QUI SE LANCE DES QUE L'ON EFFECTUE UN MOUVEMENT
def jouer(event):
    global move,fusionned,grille,grille2
    grille2=grille[:]
    fusionned=[]
    move=0
    #PARTIE QUI GERE LES DEPLACEMENTS VERTICAUX
    if event.keysym =="Up" or event.keysym=="Down":
        for col in range(4):
            for ligne in range(3):
                if event.keysym=="Down":
                    ligne=3-ligne
                # SI IL Y A UN "BLANC" ON DECALE TOUT VERS LE HAUT/BAS ET LE DERNIER ELEMENT DUNE COLONNE DEVIENT UN "BLANC"
                if grille[4*ligne+col]==0:
                    if event.keysym =="Up":
                        total=0
                        while grille[4*ligne+col]==0:
                            for rest in range(3-ligne):
                                #ON AJOUTE A LA VARIABLE total LA VALEUR DE LA CASE CONSIDEREE
                                total=total+grille[4*ligne+col+4*(rest+1)]
                                #DECALAGE
                                grille[4*ligne+col+4*rest]=grille[4*ligne+col+4*(rest+1)]
                            grille[12+col]=0
                            #SI total==0 ALORS RIEN N'A ETE CHANGÉ
                            if total==0:
                                break
                            #SINON DES CASES ONT ETE DECALÉES ET UNE ACTION A ETE EFFECTUEE
                            else:
                                move=1
                        #FUSION AVEC LA CASE DU DESSUS/DESSOUS SI IL Y A BESOIN
                        if ligne>=1 and grille[4*ligne+col]!=0 and grille[4*ligne+col]==grille[4*(ligne-1)+col]:
                            fus=1
                            #VERIFICATION QUE UNE DES 2 CASES NE PROVIENT PAS DEJA DUNE FUSION
                            for number in fusionned:
                                if 4*ligne+col==number or 4*(ligne-1)+col==number:
                                    fus=0
                                    break
                            if fus==1:
                                #FUSION : UNE CASE DOUBLE DE VALEUR ALORS QUE L'AUTRE DEVIENT NULLE
                                grille[4*(ligne-1)+col]=2*grille[4*ligne+col]
                                fusionned.append(4*(ligne-1)+col)
                                grille[4*ligne+col]=0
                                total=0
                                #REDECALAGE
                                while grille[4*ligne+col]==0:
                                    for stay in range(3-ligne):
                                        total=total+grille[4*ligne+col+4*(stay+1)]
                                        grille[4*ligne+col+4*stay]=grille[4*ligne+col+4*(stay+1)]
                                        grille[12+col]=0
                                    if total==0:
                                        break


                    elif event.keysym=="Down":
                        total=0
                        while grille[4*ligne+col]==0:
                            for rest in range(ligne):
                                total=total+grille[4*ligne+col-4*(rest+1)]
                                grille[4*ligne+col-4*rest]=grille[4*ligne+col-4*(rest+1)]
                            grille[col]=0
                            if total==0:
                                break
                            else:
                                move=1
                        if ligne<=2 and grille[4*ligne+col]!=0 and grille[4*ligne+col]==grille[4*(ligne+1)+col]:
                            fus=1
                            for number in fusionned:
                                if 4*ligne+col==number or 4*(ligne+1)+col==number:
                                    fus=0
                                    break
                            if fus==1:
                                grille[4*(ligne+1)+col]=2*grille[4*ligne+col]
                                fusionned.append(4*(ligne+1)+col)
                                grille[4*ligne+col]=0
                                total=0
                                while grille[4*ligne+col]==0:
                                    for stay in range(ligne):
                                        total=total+grille[4*ligne+col-4*(stay+1)]
                                        grille[4*ligne+col-4*stay]=grille[4*ligne+col-4*(stay+1)]
                                        grille[col]=0
                                    if total==0:
                                        break

                # SI 2 ELEMENTS CONSECUTIFS SONT EGAUX, ILS FUSIONNENT
                if event.keysym=="Up" and grille[4*ligne+col]!=0 and grille[4*ligne+col]==grille[4*(ligne+1)+col]:
                    #la fusion: le premier double de valeur et le second est laissé blanc
                    grille[4*ligne+col]=2*grille[4*ligne+col]
                    grille[4*(ligne+1)+col]=0
                    fusionned.append(4*ligne+col)
                if event.keysym=="Down" and grille[4*ligne+col]!=0 and grille[4*ligne+col]==grille[4*(ligne-1)+col]:
                    #la fusion: le premier double de valeur et le second est laissé blanc
                    grille[4*ligne+col]=2*grille[4*ligne+col]
                    grille[4*(ligne-1)+col]=0
                    fusionned.append(4*ligne+col)
                    
    #PARTIE POUR LES DEPLACEMENTS HORIZONTAUX
    if event.keysym =="Left" or event.keysym=="Right":
        for ligne in range(4):
            for col in range(3):
                if event.keysym=="Right":
                    col=3-col
                    
                # SI IL Y A UN "BLANC" ON DECALE TOUT VERS LE HAUT/BAS ET LE DERNIER ELEMENT DUNE COLONNE DEVIENT UN "BLANC"
                if grille[4*ligne+col]==0:
                    if event.keysym =="Left":
                        total=0
                        while grille[4*ligne+col]==0:
                            for rest in range(3-col):
                                total=total+grille[4*ligne+col+(rest+1)]
                                grille[4*ligne+col+rest]=grille[4*ligne+col+(rest+1)]
                            grille[3+4*ligne]=0
                            if total==0:
                                break
                            else:
                                move=1
                        if col>=1 and grille[4*ligne+col]!=0 and grille[4*ligne+col]==grille[4*ligne+col-1]:
                            fus=1
                            for number in fusionned:
                                if 4*ligne+col == number or 4*ligne+col-1==number:
                                    fus=0
                                    break
                            if fus==1:
                                grille[4*ligne+col-1]=2*grille[4*ligne+col]
                                fusionned.append(4*ligne+col-1)
                                grille[4*ligne+col]=0
                                total=0
                                while grille[4*ligne+col]==0:
                                    for stay in range(3-col):
                                        total=total+grille[4*ligne+col+(stay+1)]
                                        grille[4*ligne+col+stay]=grille[4*ligne+col+stay+1]
                                        grille[4*ligne+3]=0
                                    if total==0:
                                        break

                    elif event.keysym=="Right":
                        total=0
                        while grille[4*ligne+col]==0:
                            for rest in range(col):
                                total=total+grille[4*ligne+col-(rest+1)]
                                grille[4*ligne+col-rest]=grille[4*ligne+col-(rest+1)]
                            grille[4*ligne]=0
                            if total==0:
                                break
                            else:
                                move=1
                        if col<=2 and grille[4*ligne+col]!=0 and grille[4*ligne+col]==grille[4*ligne+col+1]:
                            fus=1
                            for number in fusionned:
                                if 4*ligne+col==number or 4*ligne+col+1==number:
                                    fus=0
                                    break
                            if fus==1:
                                grille[4*ligne+col+1]=2*grille[4*ligne+col]
                                fusionned.append(4*ligne+col+1)
                                grille[4*ligne+col]=0
                                total=0
                                while grille[4*ligne+col]==0:
                                    for stay in range(col):
                                        total=total+grille[4*ligne+col-(stay+1)]
                                        grille[4*ligne+col-stay]=grille[4*ligne+col-(stay+1)]
                                        grille[4*ligne]=0
                                    if total==0:
                                        break

                # SI 2 ELEMENTS CONSECUTIFS SONT EGAUX, ILS FUSIONNENT
                if event.keysym=="Left" and grille[4*ligne+col]!=0 and grille[4*ligne+col]==grille[4*ligne+col+1]:
                    #la fusion: le premier double de valeur et le second est laissé blanc
                    grille[4*ligne+col]=2*grille[4*ligne+col]
                    grille[4*ligne+col+1]=0
                    fusionned.append(4*ligne+col)
                if event.keysym=="Right" and grille[4*ligne+col]!=0 and grille[4*ligne+col]==grille[4*ligne+col-1]:
                    #la fusion: le premier double de valeur et le second est laissé blanc
                    grille[4*ligne+col]=2*grille[4*ligne+col]
                    grille[4*ligne+col-1]=0
                    fusionned.append(4*ligne+col)
    randomplace()

def randomplace():
    global grille,move,fusionned,won,fen,grille2,grilleprec
    b=[]
    for element in range(16):
        if grille[element]==0:
            b.append(element)
        if grille[element]==2048 and won==0:
            winlab=Label(fen,text="Bravo, vous avez gagné !!!",font='Arial 14')
            winlab.grid(row=3,column=2,padx=3,pady=2)
            won=1
    if (fusionned!=[] or move==1) and len(b)>=1:
        grilleprec=grille2[:]
        if random()>=0.75:
            n=4
        else:
            n=2
        grille[b[randint(0,len(b)-1)]]=n
        affichage()
    elif len(b)==0:
        affichage()
        fin()

def affichage():
    global grille,fen,lab,hexa
    for l in lab:
        l.destroy()
    for i in range(16):
        if grille[i]!=0:
            if grille[i]<=32:
                back1=255
                back2=255
                back3=int(255-63.75*log2(grille[i]/2))
            elif grille[i]<=512:
                back1=255
                back2=int(255-63.75*log2(grille[i]/32))
                back3=0
            elif grille[i]<=8192:
                back1=255
                back2=0
                back3=int(63.75*log2(grille[i]/512))
            elif grille[i]<=131072:
                back1=int(256-63.75*log2(grille[i]/8196))
                back2=0
                back3=256
            r=str(hexa[int(back1/16)]+hexa[int(back1)%16])
            g=str(hexa[int(back2/16)]+hexa[int(back2)%16])
            b=str(hexa[int(back3/16)]+hexa[int(back3)%16])

            lab.append(Label(canevas,text=str(grille[i]),bg='#'+r+g+b))
            lab[-1].place(y=15+((i-i%4)*12.5),x=20+(i%4)*50)

def fin():
    global fen,grille,won,fusionned,move
    fen2=Tk()
    fen2.title("Perdu")
    
    def quitter():
        global fen,fen2
        with open('grille.txt','w') as fichier:
            fichier.write("0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
        fen2.destroy()
        fen.destroy()

    def play():
        global fen2,grille,won,fusionned,move
        fen2.destroy()
        grille=[0,0,0,0,
                0,0,0,0,
                0,0,0,0,
                0,0,0,0]
        won=0
        fusionned=[]
        move=1
        randomplace()
        randomplace()

    Label(fen2,text="Vous avez perdu",font="Arial 14").grid(row=1,column=1,columnspan=2,padx=3,pady=2)
    Button(fen2,text="Quitter",font="Arial 12",command=quitter).grid(row=2,column=1,padx=2,pady=1)
    Button(fen2,text="Rejouer",font="Arial 12",command=play).grid(row=2,column=2,padx=2,pady=1)

def undo():
    global grille,grilleprec
    grille=grilleprec
    affichage()
    
def savequit():
    global grille
    grid=""
    for elnt in grille:
        grid=grid+str(elnt)+","
    with open('grille.txt','w') as fichier:
        fichier.write(grid[:-1])
    fen.destroy()
    

#PROGRAMME PRINCIPAL
canevas = Canvas(fen,width=200,height=200,bg='light grey')
canevas.grid(row=1,column=1,rowspan=3,padx=10,pady=10)
canevas.create_line(100,0,100,200)
canevas.create_line(50,0,50,200)
canevas.create_line(150,0,150,200)
canevas.create_line(0,100,200,100)
canevas.create_line(0,50,200,50)
canevas.create_line(0,150,200,150)
Button(fen,text="Annuler la\nderniere action",command=undo).grid(row=1,column=2,padx=3,pady=2)
Button(fen,text="Sauver et\nquitter",command=savequit).grid(row=2,column=2,padx=3,pady=2)
if grille==[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
    move=1
    randomplace()
    randomplace()
else:
    affichage()
fen.bind('<Left>',jouer)
fen.bind('<Right>',jouer)
fen.bind('<Up>',jouer)
fen.bind('<Down>',jouer)
fen.mainloop()