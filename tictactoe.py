import tkinter as tk
from tkinter import messagebox
import sys
root=tk.Tk()
root.geometry()
root.title('Tic-Tac-Toe')
n=c11=c12=c13=c21=c22=c23=c31=c32=c33=g=xwin=owin=win=0
def click11():
    global n,c11,xwin,owin,xp,op,win
    if int(c11)==0:
       if n%2==0:
           bt=tk.Label(root,text='X',width=4,height=2,font=15)
           bt.grid(row=0,column=0)
           c11='x'
       elif n%2==1:
           bt=tk.Label(root,text='O',width=4,height=2,font=15)
           bt.grid(row=0,column=0)
           c11='o'
       n+=1
    if c11==c12==c13!=0:
        if c11=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c11=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame()       
    if c11==c22==c33!=0:
        if c11=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c11=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame()
    if c11==c21==c31!=0:
        if c11=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c11=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame()
    if n==9:
        messagebox.showinfo('NExt Time',"It's a Draw")
        nextgame()
def click12():
    global n,c12,owin,xwin,op,xp  
    if int(c12)==0:
       if n%2==0:
           bt=tk.Label(root,text='X',width=4,height=2,font=15)
           bt.grid(row=0,column=1)
           c12='x'
       elif n%2==1:
           bt=tk.Label(root,text='O',width=4,height=2,font=15)
           bt.grid(row=0,column=1)
           c12='o' 
    n+=1
    if c11==c12==c13!=0:
        if c11=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c11=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame()    
    elif c22==c12==c32!=0:
        if c12=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c12=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame()
    if n==9:
        messagebox.showinfo('NExt Time',"It's a Draw")
        nextgame()
def click13():
    global n,c13,owin,xwin,op,xp
    if int(c13)==0:
       if n%2==0:
           bt=tk.Label(root,text='X',width=4,height=2,font=15)
           bt.grid(row=0,column=2)
           c13='x'
       elif n%2==1:
           bt=tk.Label(root,text='O',width=4,height=2,font=15)
           bt.grid(row=0,column=2)
           c13='o' 
       n+=1
    if c11==c12==c13!=0:
        if c11=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c11=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame()    
    elif c13==c22==c31!=0:
        if c13=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c11=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame() 
    if c23==c33==c13!=0:
        if c13=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c13=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame()
    if n==9:
        messagebox.showinfo('NExt Time',"It's a Draw")
        nextgame()
def click21():
    global n,c21,owin,xwin
    if int(c21)==0:
       if n%2==0:
           bt=tk.Label(root,text='X',width=4,height=2,font=15)
           bt.grid(row=1,column=0)
           c21='x'
       elif n%2==1:
           bt=tk.Label(root,text='O',width=4,height=2,font=15)
           bt.grid(row=1,column=0)
           c21='o' 
       n+=1    
    if c21==c22==c23!=0:
        if c21=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c21=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame()
    if c11==c21==c31!=0:
        if c21=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c21=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame()
    if n==9:
        messagebox.showinfo('NExt Time',"It's a Draw")
        nextgame()
def click22():
    global n,c22,owin,xwin
    if int(c22)==0:
       if n%2==0:
           bt=tk.Label(root,text='X',width=4,height=2,font=15)
           bt.grid(row=1,column=1)
           c22='x'
       elif n%2==1:
           bt=tk.Label(root,text='O',width=4,height=2,font=15)
           bt.grid(row=1,column=1)
           c22='o' 
       n+=1    
    if c21==c22==c23!=0:
        if c21=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c21=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame()
    if c11==c22==c33!=0:
        if c11=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c11=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame()
    if c13==c22==c31!=0:
        if c13=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c13=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame() 
    if c32==c12==c22!=0:
        if c21=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c21=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame()
    if n==9:
        messagebox.showinfo('NExt Time',"It's a Draw")
        nextgame()
def click23():
    global n,c23,owin,xwin
    if int(c23)==0:
       if n%2==0:
           bt=tk.Label(root,text='X',width=4,height=2,font=15)
           bt.grid(row=1,column=2)
           c23='x'
       elif n%2==1:
           bt=tk.Label(root,text='O',width=4,height=2,font=15)
           bt.grid(row=1,column=2)
           c23='o' 
       n+=1    
    if c21==c22==c23!=0:
        if c21=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c21=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame()  
    if c13==c33==c23!=0:
        if c21=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c21=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame()
    if n==9:
        messagebox.showinfo('NExt Time',"It's a Draw")
        nextgame()
def click31():
    global n,c31,owin,xwin
    if int(c31)==0:
       if n%2==0:
           bt=tk.Label(root,text='X',width=4,height=2,font=15)
           bt.grid(row=2,column=0)
           c31='x'
       elif n%2==1:
           bt=tk.Label(root,text='O',width=4,height=2,font=15)
           bt.grid(row=2,column=0)
           c31='o' 
       n+=1
    
    if c11==c21==c31!=0:
        if c11=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c11=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame()    
    if c31==c32==c33!=0:
        if c31=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c31=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame()
    if c13==c22==c31!=0:
        if c31=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c31=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame()

    if n==9:
        messagebox.showinfo('NExt Time',"It's a Draw")
        nextgame()
    
def click32():
    global n,c32,owin,xwin
    if int(c32)==0:
       if n%2==0:
           bt=tk.Label(root,text='X',width=4,height=2,font=15)
           bt.grid(row=2,column=1)
           c32='x'
       elif n%2==1:
           bt=tk.Label(root,text='O',width=4,height=2,font=15)
           bt.grid(row=2,column=1)
           c32='o' 
       n+=1    
    if c31==c32==c33!=0:
        if c31=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c31=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame()
    if c12==c22==c32!=0:
        if c32=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c32=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')        
        nextgame()  
    if n==9:
        messagebox.showinfo('NExt Time',"It's a Draw")
        nextgame()

def click33():
    global n,c33,owin,xwin
    if int(c33)==0:
       if n%2==0:
           bt=tk.Label(root,text='X',width=4,height=2,font=15)
           bt.grid(row=2,column=2)
           c33='x'
       elif n%2==1:
           bt=tk.Label(root,text='O',width=4,height=2,font=15)
           bt.grid(row=2,column=2)
           c33='o'
       n+=1
    if c31==c32==c33!=0:
        if c31=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c31=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame()
    if c11==c22==c33!=0:
        if c11=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c11=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')
        nextgame()
    if c13==c23==c33!=0:
        if c13=='x':
            xwin+=1
            messagebox.showinfo('Hurray',str(xp)+' has won the game')
        elif c13=='o':
            owin+=1
            messagebox.showinfo('Hurray',str(op)+' has won the game')        
        nextgame()
    print(n)  
    if n==9:
        messagebox.showinfo('NExt Time',"It's a Draw")
        nextgame()
xp=tk.StringVar()
op=tk.StringVar()

    
def nextgame():
    global n,c11,c12,c13,c21,c22,c23,c31,c32,c33,g,xwin,owin
    g+=1
    n=c11=c12=c13=c21=c22=c23=c31=c32=c33=0
    bt=tk.Button(root,text=' ',command=click11,width=7,height=3)
    bt.grid(row=0,column=0)

    bt=tk.Button(root,text=' ',command=click12,width=7,height=3)
    bt.grid(row=0,column=1)

    bt=tk.Button(root,text=' ',command=click13,width=7,height=3)
    bt.grid(row=0,column=2)

    bt=tk.Button(root,text=' ',command=click21,width=7,height=3)
    bt.grid(row=1,column=0)

    bt=tk.Button(root,text=' ',command=click22,width=7,height=3)
    bt.grid(row=1,column=1)

    bt=tk.Button(root,text=' ',command=click23,width=7,height=3)
    bt.grid(row=1,column=2)

    bt=tk.Button(root,text=' ',command=click31,width=7,height=3)
    bt.grid(row=2,column=0)

    bt=tk.Button(root,text=' ',command=click32,width=7,height=3)
    bt.grid(row=2,column=1)

    bt=tk.Button(root,text=' ',command=click33,width=7,height=3)
    dr=int(g)-owin-xwin
    bt.grid(row=2,column=2)
    label=tk.Label(root,text='Game No.='+str(g+1)+'\nGames Won:\n'+str(xp)+':'+str(xwin)+'\n'+str(op)+':'+str(owin)+'\nGames Drawn:'+str(dr))
    label.grid(row=3,column=0,rowspan=4,columnspan=3)
       
#seperation

bt=tk.Button(root,text=' ',command=click11,width=7,height=3)
bt.grid(row=0,column=0)

bt=tk.Button(root,text=' ',command=click12,width=7,height=3)
bt.grid(row=0,column=1)

bt=tk.Button(root,text=' ',command=click13,width=7,height=3)
bt.grid(row=0,column=2)

bt=tk.Button(root,text=' ',command=click21,width=7,height=3)
bt.grid(row=1,column=0)

bt=tk.Button(root,text=' ',command=click22,width=7,height=3)
bt.grid(row=1,column=1)

bt=tk.Button(root,text=' ',command=click23,width=7,height=3)
bt.grid(row=1,column=2)

bt=tk.Button(root,text=' ',command=click31,width=7,height=3)
bt.grid(row=2,column=0)

bt=tk.Button(root,text=' ',command=click32,width=7,height=3)
bt.grid(row=2,column=1)

bt=tk.Button(root,text=' ',command=click33,width=7,height=3)
bt.grid(row=2,column=2)

name=tk.Label(root,text='Player \nwith X',width=5)
name.grid(row=0,column=3)
name1=tk.Entry(root,width=10)
name1.grid(row=0,column=4)

name=tk.Label(root,text='Player \nwith O',width=5)
name.grid(row=1,column=3)
name2=tk.Entry(root,width=10)
name2.grid(row=1,column=4)

nxtgame=tk.Button(root,text='Next Game\n(Mutual Draw)',width=10,height=2,command=nextgame)
nxtgame.grid(row=3,column=3,rowspan=2,columnspan=2)

def sta():
    global op,xp,name1,name2
    xp=name1.get()
    op=name2.get()
    name1.grid_forget()
    name2.grid_forget()
    name1=tk.Label(root,text=xp)
    name1.grid(row=0,column=4)
    name2=tk.Label(root,text=op)
    name2.grid(row=1,column=4)
    label=tk.Label(root,text='Game No.='+str(g+1)+'\nGames Won:\n'+str(xp)+':'+str(xwin)+'\n'+str(op)+':'+str(owin),anchor='w')
    label.grid(row=3,column=0,rowspan=3,columnspan=3)
    testing.grid_forget()
    registered=tk.Button(root,text='Names\nRegistered')
    registered.grid(row=2,column=3,columnspan=2)    

testing=tk.Button(root,text='Register \nNames',command=sta)
testing.grid(row=2,column=3,columnspan=2)
root.mainloop()


"""
def complay_x():
    global n
    if n%2==0:
        fnlist=[]
        for i in [clickc11,clickc12,clickc13,clickc21,clickc22,clickc23,clickc31,clickc32,clickc33]:
            if int(i)==0:
                fnlist.append(i)
            random.choice(fnlist)()
def complay_o():
    global n
    if n%2==1:
        fnlist=[]
        for i in [clickc11,clickc12,clickc13,clickc21,clickc22,clickc23,clickc31,clickc32,clickc33]:
            if int(i)==0:
                fnlist.append(i)
            random.choice(fnlist)()        
        
    
"""
