from tkinter import *
from tkinter import messagebox
import tkinter as tk
import time
import random


window = Tk()
window.title('2048')
window.geometry('540x800')
window.configure(background="white")
center = Frame(window, bg = 'white',width = 200,height = 200,padx=30,pady=30)
center.grid(row=0,column = 0)
ce = Frame(window, bg = 'white')
ce.grid(row=1,column = 0)
b = [[0 for x in range(4)] for y in range(4)]
bcopy = [[0 for x in range(4)] for y in range(4)]
for i in range(4):
	for j in range(4):
		b[i][j] = 0

def startGame():
	kr1 = random.randint(0,3)
	kc1 = random.randint(0,3)
	kr2 = random.randint(0,3)
	kc2 = random.randint(0,3)
	while(kr1==kr2 and kc1==kc2):
		kr2 = random.randint(0,3)
		kc2 = random.randint(0,3)
	c[kr1][kc1].configure(text=str(2))
	c[kr2][kc2].configure(text=str(2))
	b[kr1][kc1] = 2
	b[kr2][kc2] = 2

def upCmd():
	for i in range(4):
		for j in range(4):
			bcopy[i][j] = b[i][j]

	for k in range(4):
		i = 0
		j = 0
		for i in range(3):
			while(b[i][k]==0 and i<3):
				i=i+1
			b[j][k] = b[i][k]

			print(b[j][k])
			if(j!=i):
				b[i][k] = 0
			if(b[j][k]!=0):
				c[j][k].configure(text = str(b[j][k]))
			else:
				c[j][k].configure(text = ' ')
			if(j!=i):
				c[i][k].configure(text=' ')
			# i=i+1
			j=j+1
		i=3
		while(i>0):
			if(b[i][k]==b[i-1][k] and b[i][k]!=0):
				b[i-1][k] = 2*b[i][k];
				b[i][k] = 0
				c[i][k].configure(text=' ')
				c[i-1][k].configure(text=str(b[i-1][k]))
			i=i-1
		
	kr = random.randint(0,3)
	kc = random.randint(0,3)
	while(b[kr][kc]!=0):
		kr = random.randint(0,3)
		kc = random.randint(0,3)

	c[kr][kc].configure(text=str(2))
	b[kr][kc] = 2
	return

def downCmd():
	for i in range(4):
		for j in range(4):
			bcopy[i][j] = b[i][j]

	for k in range(4):
		i = 3
		j = 3
		while(i>=0):
			while(b[i][k]==0 and i>0):
				i=i-1
			b[j][k] = b[i][k]

			print(b[j][k])
			if(j!=i):
				b[i][k] = 0
			if(b[j][k]!=0):
				c[j][k].configure(text = str(b[j][k]))
			else:
				c[j][k].configure(text = ' ')
			if(j!=i):
				c[i][k].configure(text=' ')
			i=i-1
			j=j-1
		i=3
		while(i>0):
			if(b[i][k]==b[i-1][k] and b[i][k]!=0):
				b[i][k] = 2*b[i-1][k];
				b[i-1][k] = 0
				c[i-1][k].configure(text=' ')
				c[i][k].configure(text=str(b[i][k]))
			i=i-1
	kr = random.randint(0,3)
	kc = random.randint(0,3)
	while(b[kr][kc]!=0):
		kr = random.randint(0,3)
		kc = random.randint(0,3)

	c[kr][kc].configure(text=str(2))
	b[kr][kc] = 2

	return 

def leftCmd():
	for i in range(4):
		for j in range(4):
			bcopy[i][j] = b[i][j]

	for k in range(4):
		i = 0
		j = 0
		for i in range(3):
			while(b[k][i]==0 and i<3):
				i=i+1
			b[k][j] = b[k][i]

			print(b[k][j])
			if(j!=i):
				b[k][i] = 0
			if(b[k][j]!=0):
				c[k][j].configure(text = str(b[k][j]))
			else:
				c[k][j].configure(text = ' ')
			if(j!=i):
				c[k][i].configure(text=' ')
			# i=i+1
			j=j+1
		i=0
		for i in range(3):
			if(b[k][i]==b[k][i+1] and b[k][i]!=0):
				b[k][i] = 2*b[k][i+1];
				b[k][i+1] = 0
				c[k][i+1].configure(text=' ')
				c[k][i].configure(text=str(b[k][i]))
			i=i+1
		
	kr = random.randint(0,3)
	kc = random.randint(0,3)
	while(b[kr][kc]!=0):
		kr = random.randint(0,3)
		kc = random.randint(0,3)

	c[kr][kc].configure(text=str(2))
	b[kr][kc] = 2
	return
	
def rightCmd():
	for i in range(4):
		for j in range(4):
			bcopy[i][j] = b[i][j]

	for k in range(4):
		i = 3
		j = 3
		while(i>=0):
			while(b[k][i]==0 and i>0):
				i=i-1
			b[k][j] = b[k][i]

			print(b[k][j])
			if(j!=i):
				b[k][i] = 0
			if(b[k][j]!=0):
				c[k][j].configure(text = str(b[k][j]))
			else:
				c[k][j].configure(text = ' ')
			if(j!=i):
				c[k][i].configure(text=' ')
			i=i-1
			j=j-1
		i=3
		while(i>0):
			if(b[k][i]==b[k][i-1] and b[k][i]!=0):
				b[k][i] = 2*b[k][i-1];
				b[k][i-1] = 0
				c[k][i-1].configure(text=' ')
				c[k][i].configure(text=str(b[k][i]))
			i=i-1
	kr = random.randint(0,3)
	kc = random.randint(0,3)
	while(b[kr][kc]!=0):
		kr = random.randint(0,3)
		kc = random.randint(0,3)

	c[kr][kc].configure(text=str(2))
	b[kr][kc] = 2

	return

def undoCmd():
	for i in range(4):
		for j in range(4):
			b[i][j] = bcopy[i][j]
			if(b[i][j]!=0):
				c[i][j].configure(text=str(b[i][j]))	
			else:
				c[i][j].configure(text=' ')
	return

c = [[0 for x in range(4)] for y in range(4)]

for i in range(4):
	for j in range(4):
		cell = Frame(center,bg = "lightgrey",highlightbackground = "black", 
                    highlightthickness = 2,width=80,height =80, padx=3,pady=3)
		cell.grid(row=i,column=j)
		c[i][j] = Button(cell,fg = "black",bg = "lightgrey",
				highlightbackground = "lightgrey",borderwidth=0,
				height =4,width =5)
		c[i][j].grid(row=i,column=j)

startGame()

up = Button(ce,text = "Up",bg = "blue", fg ="white",width = 10,height = 3,command = upCmd)
up.grid(row = 0,column = 0)
down = Button(ce,text = "Down",bg = "blue",fg = "white",width = 10,height = 3,command = downCmd)
down.grid(row = 0,column=1)
left = Button(ce,text = "Left",bg = "blue",fg = "white",width = 10,height = 3,command =leftCmd)
left.grid(row = 0,column=2)
right = Button(ce,text = "Right",bg = "blue",fg = "white",width = 10,height = 3,command = rightCmd)
right.grid(row = 0,column=3)
undo = Button(ce,text = "Undo",bg = "blue",fg = "white",width = 10,height = 3,command = undoCmd)
undo.grid(row = 0,column=4)


window.mainloop()