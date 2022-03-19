import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
def play():
    global n,g,r,lc,lr,win,regi,root
    root=tk.Tk()
    root.title('Tic-Tac-Toe')
    n=g=r=0
    imgf=tk.PhotoImage(file="bg.png")
    tbg=tk.Label(root,image=imgf,bd=-7)
    tbg.image=imgf
    tbg.grid(row=0,column=0,rowspan=6,columnspan=5)
    lc=[['','',''],['','',''],['','','']]
    lr=[[1,2,3],[1,2,3],[1,2,3]]
    win={'x':[0,'X'],'o':[0,'O']}
    def namcha():
        global win,r,g,root,regi
        messagebox.showinfo('Alert','Current game will be lost')
        g-=1
        r=0
        win['x'][1],win['o'][1]='X','O'
        nextgame()
        regi.grid_forget()
        regi=tk.Button(root,text='Register \nNames',command=sta)
        regi.grid(row=2,column=3,columnspan=2)
        regi.config(height=3,width=11)
    def click(r,c):                                                 
        global n,win,lc,lr
        wd=0                                                        
        if lr[r-1][c-1]==c:                                        
            if n%2==0:
               bt=tk.Label(root,text='X',width=4,height=2,font=15)
               bt.grid(row=r-1,column=c-1)
               lc[r-1][c-1]='x'
            elif n%2==1:
               bt=tk.Label(root,text='O',width=4,height=2,font=15)
               bt.grid(row=r-1,column=c-1)
               lc[r-1][c-1]='o'
            n+=1
            lr[r-1][c-1]=None
            
            #checking for win
            if lc[r-1][0]==lc[r-1][1]==lc[r-1][2]!='':
                win[lc[r-1][0]][0]+=1
                messagebox.showinfo('Hurray',(win[lc[r-1][0]][1]+' has won'))
                wd=1
                nextgame()
            elif lc[0][c-1]==lc[1][c-1]==lc[2][c-1]!='':
                messagebox.showinfo('Hurray',(win[lc[0][c-1]][1]+' has won'))
                win[lc[0][c-1]][0]+=1
                wd=1
                nextgame()
            elif lc[0][0]==lc[1][1]==lc[2][2]!='':
                messagebox.showinfo('Hurray',(win[lc[0][0]][1]+' has won'))
                win[lc[0][0]][0]+=1
                nextgame()
            elif lc[0][2]==lc[1][1]==lc[2][0]!='':
                messagebox.showinfo('Hurray',(win[lc[1][1]][1]+' has won'))
                win[lc[1][1]][0]+=1
                nextgame()
            if n==9:
                messagebox.showinfo('Next Time',"It's a draw!")
                nextgame()

    def nextgame():
        global n,win,lc,lr,name1,name2,r,g
        lc=[['','',''],['','',''],['','','']]
        lr=[[1,2,3],[1,2,3],[1,2,3]]
        wd=0 
        g=g+1
        n=0
        label=tk.Label(root,text='Game No.='+str(g)+'\nGames Won:\n'+str(win['x'][1])+':'+str(win['x'][0])+'\n'+str(win['o'][1])+':'+str(win['o'][0]))
        label.grid(row=3,column=0,rowspan=3,columnspan=3)
        bt=tk.Button(root,text=' ',command=lambda:click(1,1),width=7,height=3)
        bt.grid(row=0,column=0,sticky='se')

        bt=tk.Button(root,text=' ',command=lambda:click(1,2),width=7,height=3)
        bt.grid(row=0,column=1,sticky='sew')

        bt=tk.Button(root,text=' ',command=lambda:click(1,3),width=7,height=3)
        bt.grid(row=0,column=2,sticky='sw')

        bt=tk.Button(root,text=' ',command=lambda:click(2,1),width=7,height=3)
        bt.grid(row=1,column=0,sticky='nse')

        bt=tk.Button(root,text=' ',command=lambda:click(2,2),width=7,height=3)
        bt.grid(row=1,column=1,sticky='nsew')

        bt=tk.Button(root,text=' ',command=lambda:click(2,3),width=7,height=3)
        bt.grid(row=1,column=2,sticky='nsw')

        bt=tk.Button(root,text=' ',command=lambda:click(3,1),width=7,height=3)
        bt.grid(row=2,column=0,sticky='ne')

        bt=tk.Button(root,text=' ',command=lambda:click(3,2),width=7,height=3)
        bt.grid(row=2,column=1,sticky='new')

        bt=tk.Button(root,text=' ',command=lambda:click(3,3),width=7,height=3)
        bt.grid(row=2,column=2,sticky='nw')
        if r==0:
            name=tk.Label(root,text='Player \nwith X',width=5)
            name.grid(row=0,column=3)
            name1=tk.Entry(root,width=10)
            name1.grid(row=0,column=4)

            name=tk.Label(root,text='Player \nwith O',width=5)
            name.grid(row=1,column=3)
            name2=tk.Entry(root,width=10)
            name2.grid(row=1,column=4)

        nxtgame=tk.Button(root,text='Next Game\n(Mutual Draw)',width=10,height=2,command=nextgame)
        nxtgame.grid(row=3,column=3,rowspan=2,columnspan=2,sticky='ns')
        nxtgame.config(height=3,width=11)
        sc=tk.Button(root,text='Interchange\nSigns',command=signchange)
        sc.grid(row=5,column=3,rowspan=2,columnspan=2,sticky='n')
        sc.config(height=3,width=11)

    def signchange():
        global g,win
        if win['x'][1]!='X' and win['o'][1]!='O':
            win['x'],win['o']=win['o'],win['x']
            g-=1
            nextgame()
        elif win['x'][1]!='X' and win['o'][1]=='O':
            win['x'],win['o']=win['o'],win['x']
            win['x'][1]='X'
            g-=1
            nextgame()
        elif win['x'][1]=='X' and win['o'][1]!='O':
            win['x'],win['o']=win['o'],win['x']
            win['o'][1]='O'
            g-=1
            nextgame()
        else:
            win['x'],win['o']=win['o'],win['x']
            win['o'][1]='O'
            win['x'][1]='X'
            g-=1
            nextgame()
        name1=tk.Label(root,text=win['x'][1])
        name1.grid(row=0,column=4)
        name2=tk.Label(root,text=win['o'][1])
        name2.grid(row=1,column=4)  

    def sta():
        global win,name1,name2,r,regi
        if r==0:
            name1.grid_forget()
            name2.grid_forget()
            if name1.get()=='' or name2.get()=='':
                if win['x'][1]=='' and win['o'][1]!='':
                    win['o'][1]=name2.get()
                if win['x'][1]!='' and win['o'][1]=='':
                    win['x'][1]=name1.get()
            else:
                win['x'][1]=name1.get()
                win['o'][1]=name2.get()
                
            name1=tk.Label(root,text=win['x'][1])
            name1.grid(row=0,column=4)
            name2=tk.Label(root,text=win['o'][1])
            name2.grid(row=1,column=4)
            label=tk.Label(root,text='Game No.='+str(g)+'\nGames Won:\n'+str(win['x'][1])+':'+str(win['x'][0])+'\n'+str(win['o'][1])+':'+str(win['o'][0]))
            label.grid(row=3,column=0,rowspan=3,columnspan=3)

            regi.grid_forget()
            registered=tk.Button(root,text='Change Names',command=namcha)
            registered.grid(row=2,column=3,columnspan=2)
            r=1
        else:
            name1=tk.Label(root,text=win['x'][1])
            name1.grid(row=0,column=4)
            name2=tk.Label(root,text=win['o'][1])
            name2.grid(row=1,column=4)
            label=tk.Label(root,text='Game No.='+str(g)+'\nGames Won:\n'+str(win['x'][1])+':'+str(win['x'][0])+'\n'+str(win['o'][1])+':'+str(win['o'][0]))
            label.grid(row=3,column=0,rowspan=3,columnspan=3)
    regi=tk.Button(root,text='Register \nNames',command=sta)
    regi.grid(row=2,column=3,columnspan=2,sticky='s')
    regi.config(height=3,width=11)
    nextgame()
    root.mainloop()
play()
