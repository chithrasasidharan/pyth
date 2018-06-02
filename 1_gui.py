from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

window = Tk()
window.title("Calculator")
window.geometry('300x200')

lbl1= Label(window,text = "Number1	")
lbl1.grid(column = 0,row = 0)

num1 = Entry(window, width = 10)
num1.focus()
num1.grid(column = 1,row = 0)

lbl2 = Label(window, text = "Number2	")
lbl2.grid(column = 0,row = 1)

num2 = Entry(window,width = 10)
num2.grid(column = 1,row = 1)

status_label = Label(window,text="")
status_label.grid(column = 0,row = 4)

def clickedAdd():
	if(num1.get() and num2.get()!=""):
		try:
                        val1 = float(num1.get())
                        val2 = float(num2.get())
                        if(val1+val2==0):
                                messagebox.showinfo('Result',"0")
                        else:
                                messagebox.showinfo('Result',val1+val2)
                        status_label.configure(text = "Operation successful")
		except:
			status_label.configure(text = "Invalid input")
	else:
		status_label.configure(text = "Fill in all the required fields")

def clickedSub():
        if(num1.get() and num2.get()!=""):
                try:
                        val1 = float(num1.get())
                        val2 = float(num2.get())
                        if(val1-val2==0):
                                messagebox.showinfo('Result',"0")
                        else:
	                        messagebox.showinfo('Result',val1-val2)
                        status_label.configure(text = "Operation successful")
                except:
                        status_label.configure(text = "Invalid input")
        else:
                status_label.configure(text = "Fill in all the required fields")
add = Button(window, text = "+",command =clickedAdd)
add.grid(column = 1,row = 3)

sub = Button(window, text = "-",command =clickedSub)
sub.grid(column = 0,row = 3)


window.mainloop()
