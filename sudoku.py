#!/usr/bin/env/python3

from tkinter import *
from tkinter import messagebox
import tkinter as tk
import time

window = Tk()
window.title('Sudoku')
window.geometry('700x700')

center = Frame(window, bg = 'white',width = 900,height = 900,padx=30,pady=30)
center.grid(row=0,column = 0)
puzzle = [ 0,0,7,0,0,0,3,0,0,
           0,0,0,0,0,0,0,0,0,
           1,4,6,0,7,0,2,5,8,
           0,0,4,8,0,5,1,0,0,
           7,0,8,0,6,0,5,0,2,
           0,6,0,0,4,0,0,3,0,
           0,0,0,0,0,0,0,0,0,
           2,0,0,7,5,4,0,0,6,
           0,0,0,6,0,9,0,0,0 ]

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

def clickAndAdd(b,r,c,i):
    if(i==0):
        b[r][c].configure(text = ' ')
    else:
        b[r][c].configure(text = str(i))
        if(errorCheck(b,r,c)):
            messagebox.showinfo(window,"err")
            b[r][c].configure(text=' ')



def clickBad(b,r,c,col):
    if(col=="red"):
        k=1
        for i in range(3):
            for j in range(3):
                btn = Button(window,text = str(k),
                    command = lambda k=k:clickAndAdd(b,r,c,k))
                btn.grid(row=i+1,column=j+1)
                k=k+1
        btn = Button(window,text = '0',command = lambda k=0:clickAndAdd(b[r][c],r,c,k))
        btn.grid(row=i+2,column=j)

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


def clicked():
	messagebox.showinfo('Hint',"Here is your hint")

btn_text = tk.StringVar()
def paused():
	val = btn_text.get()
	if(val == "Pause"):
		messagebox.showinfo('Paused', "Your window is now Paused!!!")
		btn_text.set("Resume")
	else:
		messagebox.showinfo('Paused', "Your window is now resumed!!!")
		btn_text.set("Pause")


# hint = Button(window,text = "Hint",bg = "blue", fg ="white", width = 10,height = 3,command = clicked)
# hint.grid(row = 0,column = 1)

# pause = Button(window,textvariable = btn_text,bg = "blue",fg="white", width = 10,height = 3,command = paused)
# btn_text.set("Pause")
# pause.grid(row = 1, column = 1)

window.mainloop()
