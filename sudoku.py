#!/usr/bin/env/python3

from tkinter import *
from tkinter import messagebox
import tkinter as tk
import time
import random


window = Tk()
window.title('Sudoku')
window.geometry('700x700')
window.configure(background="white")
center = Frame(window, bg = 'white',width = 200,height = 200,padx=30,pady=30)
center.grid(row=0,column = 0)
ce = Frame(window, bg = 'white')
ce.grid(row=1,column = 0)
timeFrame = Frame(ce,bg="blue")
timeFrame.grid(row=0,column=1)

timer=[0,0,0]
state = False
def update_time():
    if(state):
        global timer
        timer[2]+=1
        if(timer[2]>=60):
            timer[2] = 0
            timer[1]+=1
        if(timer[1]>=60):
            timer[0]+=1
            timer[1]=0
        timeString = str(timer[0])+':'+str(timer[1])+':'+str(timer[2])
        show.config(text=timeString)
    ce.after(1000,update_time)

def start():
    global state
    state = True

def paused():
    val = btn_text.get()
    global state
    if(val == "Pause"):
        state = False
        for x in range(9):
            for y in range(9):
                if(b[x][y].cget('fg')=="red"):
                    b[x][y].configure(bg="red")
                else:
                    b[x][y].configure(bg="black")
        # messagebox.showinfo('Paused', "Your window is now Paused!!!")
        btn_text.set("Resume")
    else:
        state = True
        for x in range(9):
            for y in range(9):
                if(b[x][y].cget('highlightbackground')=="lightgreen"):
                    b[x][y].configure(bg="lightgreen")
                else:
                    b[x][y].configure(bg="white")
        # messagebox.showinfo('Paused', "Your window is now resumed!!!")
        btn_text.set("Pause")# state = False
start()
show = Label(timeFrame,text ='00:00:00',height=3,width=10,bg="blue",fg="white",
    font = ('Helvetica',20))
show.grid(row=1,column=1)
update_time()

def findEmptyLoc(a,l):
    for i in range(9):
        for j in range(9):
            if(a[i][j]==0):
                l[0] = i
                l[1] = j
                return True
    return False
def ErrorCheckGrid(a,r,c,k):
    cs = [0 for x in range(9)]
    r1 = -1
    c1 = -1
    if(r%3==1):
        r1 = r-1
    if(c%3==1):
        c1 = c-1 
    if(r%3==2):
        r1 = r-2
    if(c%3==2):
        c1 = c-2
    if(r%3==0):
        r1 = r
    if(c%3==0):
        c1 = c
    x = 0
    for i in range(3):
        for j in range(3):
            if((i+r1)!=r and (j+c1)!=c):
                cs[x] = a[i+r1][j+c1]
                x = x+1
    for x in range(9):
        if(cs[x]==k):
            return 1


def errorCheck(a,r,c,k):
    cs = [0 for x in range(9)]
    for x in range(9):
        if(x!=r):
            cs[x] = a[x][c]
    for x in range(9):
        if(cs[x]==k):
            return 1
    for x in range(9):
        if(x!=c):
            cs[x] = a[r][x]
    for x in range(9):
        if(cs[x]==k):
            return 1
    if(ErrorCheckGrid(a,r,c,k)==1):
        return 1

def solveSudoku(a):
    l=[0,0]
     
    if(not findEmptyLoc(a,l)):
        return True
     
    row=l[0]
    col=l[1]
     
    for num in range(1,10):
         
        # if looks promising
        if(not errorCheck(a,row,col,num)):
             
            # make tentative assignment
            a[row][col]=num
 
            # return, if sucess, ya!
            if(solveSudoku(a)):
                return True
 
            # failure, unmake & try again
            a[row][col] = 0
             
    # this triggers backtracking        
    return False


     
    # creating a 2D array for the grid
grid=[[0 for x in range(9)]for y in range(9)]
     
    # assigning values to the grid
grid=[[0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [9,0,0,0,0,0,0,0,0],
          [0,0,0,0,9,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]]
     
    # if sucess print the grid
solveSudoku(grid)
for p in range(60):
    i = random.randint(0,8)
    j = random.randint(0,8)
    if(grid[i][j]!=0):
        grid[i][j] = 0
    else:
        p-=2

for i in range(9):
    for j in range(9):
        print(grid[i][j])

puzzle = [0 for x in range(81)]
m = 0
i=0
j=0
for i in range(9):
    for j in range(9):
        puzzle[m] = grid[i][j]
        m+=1

# puzzle = [ 0,0,7,0,0,0,3,0,0,
#            0,0,0,0,0,0,0,0,0,
#            1,4,6,0,7,0,2,5,8,
#            0,0,4,8,0,5,1,0,0,
#            7,0,8,0,6,0,5,0,2,
#            0,6,0,0,4,0,0,3,0,
#            0,0,0,0,0,0,0,0,0,
#            2,0,0,7,5,4,0,0,6,
#            0,0,0,6,0,9,0,0,0 ]

cells = {}
colour = {}
i=0

def ErrorCheckGrid(b,r,c):
    cs = [0 for x in range(9)]
    r1 = -1
    c1 = -1
    if(r%3==1):
        r1 = r-1
    if(c%3==1):
        c1 = c-1 
    if(r%3==2):
        r1 = r-2
    if(c%3==2):
        c1 = c-2
    if(r%3==0):
        r1 = r
    if(c%3==0):
        c1 = c
    x = 0
    for i in range(3):
        for j in range(3):
            if((i+r1)!=r and (j+c1)!=c):
                cs[x] = b[i+r1][j+c1].cget('text')
                x = x+1
    for x in range(9):
        if(cs[x]==b[r][c].cget('text')):
            return 1


def errorCheck(b,r,c):
    cs = [0 for x in range(9)]
    for x in range(9):
        if(x!=r):
            cs[x] = b[x][c].cget('text')
    for x in range(9):
        if(cs[x]==b[r][c].cget('text')):
            return 1
    for x in range(9):
        if(x!=c):
            cs[x] = b[r][x].cget('text')
    for x in range(9):
        if(cs[x]==b[r][c].cget('text')):
            return 1
    if(ErrorCheckGrid(b,r,c)==1):
        return 1

def check(b):
    for i in range(9):
        for j in range(9):
            if(b[i][j]==' '):
                return 0
    return 1


l = Label(window, text="Its an error!",font=('Helvetica',20))
def clickAndAdd(b,r,c,i):
    if(i==0):
        b[r][c].configure(text=' ')
        l.grid_forget()
    else:
        b[r][c].configure(text = str(i))
        if(errorCheck(b,r,c)):
            l.grid(row=2,column=0)
            # messagebox.showinfo(window,"err")
            # b[r][c].configure(text=' ')


k=1
for i in range(3):
    for j in range(3):
        btn = Button(center,text = str(k),fg = "white",bg = "blue")
        btn.grid(row=i+3,column=j+10)
        k=k+1
btn = Button(center,text = '0',fg="white",bg="blue")
btn.grid(row=i+4,column=j+9)
i=0
def clickBad(b,r,c,col):
    l.grid_forget()
    if(col=="red"):
        
        k=1
        for i in range(3):
            for j in range(3):
                btn = Button(center,text = str(k),fg = "white",bg = "blue",
                    command = lambda k=k:clickAndAdd(b,r,c,k))
                btn.grid(row=i+3,column=j+10)
                k=k+1
        btn = Button(center,text = '0',fg="white",bg="blue",command = lambda k=0:clickAndAdd(b,r,c,k))
        btn.grid(row=i+4,column=j+9)

b = [[0 for x in range(9)] for y in range(9)]
for rowindex in range(9):
    for colindex in range(9):
                cell = Frame(center,bg = "white",highlightbackground = "black", 
                    highlightthickness = 1,width=50,height =50, padx=3,pady=3)
                if(puzzle[i]==0):
                        puzzle[i]=' '
                        colour[i] = "red"
                else:
                        colour[i] = "black"
                if (rowindex in (0,1,2,6,7,8) and colindex in (3,4,5) or (rowindex in (3,4,5) and colindex in (0,1,2,6,7,8))):
                        cell.configure(background = "lightgreen")
                        b[rowindex][colindex] = Button(cell,fg = colour[i],text = str(puzzle[i]),
                            highlightbackground = "lightgreen",bg = "lightgreen",
                            borderwidth=0,height =2,width =2)
                else:
                        cell.configure(background="white")
                        b[rowindex][colindex] = Button(cell,fg = colour[i],text = str(puzzle[i]),
                            highlightbackground = "white",bg = "white",
                            borderwidth=0,height =2,width =2)
                b[rowindex][colindex].configure(command = lambda b =b,rowindex = rowindex, colindex=colindex:clickBad(b,rowindex,colindex,colour[rowindex*9+colindex]))
                b[rowindex][colindex].grid(row = rowindex,column = colindex)
                i=i+1
                cell.grid(row=rowindex,column=colindex)
                l.grid_forget()

def clicked():
    messagebox.showinfo('Hint',"Here is your hint")

btn_text = tk.StringVar()


def clearCmd():
    if(pause.cget('text')=="Resume"):
        messagebox.showinfo(window,"Cant clear while paused")
        return
    for x in range(9):
        for y in range(9):
            if(b[x][y].cget('fg')=="red"):
                b[x][y].configure(text=' ')
# buttonplace = Frame(window, bg = 'white',width =100,height = 510,padx=950,pady=30)
# buttonplace.grid(row = 0,column = 10)


pause = Button(ce,textvariable = btn_text,bg = "blue",fg="white", width = 10,height = 3,command = paused)
btn_text.set("Pause")
pause.grid(row = 0, column = 0)
clear = Button(ce,text = "Clear all",bg = "blue", fg ="white",width = 10,height = 3,command = clearCmd)
clear.grid(row = 0,column = 2)

window.mainloop()
