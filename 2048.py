from tkinter import *
from tkinter import messagebox
import tkinter as tk
import time
import random


window = Tk()
window.title('2048')
window.geometry('500x700')
window.configure(background="white")
center = Frame(window, bg = 'white',width = 200,height = 200,padx=90,pady=30)
center.grid(row=0,column = 0)
ce = Frame(window, bg = 'white')
ce.grid(row=1,column = 0)

def startGame():
	kr1 = random.randint(0,3)
	kc1 = random.randint(0,3)
	kr2 = random.randint(0,3)
	kc2 = random.randint(0,3)
	b[kr1][kc1].configure(text=str(2))
	b[kr2][kc2].configure(text=str(2))

def upCmd():
	return

def downCmd():
	return 

def leftCmd():
	return

def rightCmd():
	return

b = [[0 for x in range(4)] for y in range(4)]

for i in range(4):
	for j in range(4):
		cell = Frame(center,bg = "lightgrey",highlightbackground = "black", 
                    highlightthickness = 2,width=80,height =80, padx=3,pady=3)
		cell.grid(row=i,column=j)
		b[i][j] = Button(cell,fg = "black",bg = "lightgrey",
				highlightbackground = "lightgrey",borderwidth=0,
				height =4,width =5)
		b[i][j].grid(row=i,column=j)

startGame()

up = Button(ce,text = "Up",bg = "blue", fg ="white",width = 10,height = 3,command = upCmd)
up.grid(row = 0,column = 0)
down = Button(ce,text = "Down",bg = "blue",fg = "white",width = 10,height = 3,command = downCmd)
down.grid(row = 0,column=1)
left = Button(ce,text = "Left",bg = "blue",fg = "white",width = 10,height = 3,command = leftCmd)
left.grid(row = 0,column=2)
right = Button(ce,text = "Right",bg = "blue",fg = "white",width = 10,height = 3,command = rightCmd)
right.grid(row = 0,column=3)


window.mainloop()