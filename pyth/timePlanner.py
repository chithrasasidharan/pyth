from tkinter import *
from tkinter import messagebox
import random
import tkinter as tk


window = Tk()
window.title('Day Planner')
window.geometry('700x700')
window.configure(background="white")


activities = {0:
				{
					'name':"Learn algorithms",
					'occurrence':1,
					'credit':5,
					'estimatedTime':240,
					'scheduledAt':-1,
					'scheduledTo':-1

				},
			  1:
			  	{
			  		'name':"Learn python",
			  		'occurrence':1,
			  		'credit':5,
					'estimatedTime':120,
					'scheduledAt':-1,
					'scheduledTo':-1
			  	},
			  2:
			  	{	
			  		'name':"Read a book",
			  		'credit':4,
					'estimatedTime':30,
					'scheduledAt':-1,
					'scheduledTo':-1
			  	},
			  3:
			  	{	
			  		'name':"Do cube",
			  		'credit':2,
					'estimatedTime':15,
					'scheduledAt':-1,
					'scheduledTo':-1
			  	},
			  4:
			  	{	
			  		'name':"Learn a word",
			  		'credit':4,
					'estimatedTime':10,
					'scheduledAt':-1,
					'scheduledTo':-1
			  	},
			  
			  5:
			  	{	
			  		'name':"Read hindu",
			  		'credit':4,
					'estimatedTime':60,
					'scheduledAt':-1,
					'scheduledTo':-1
			  	},
			  
			  6:
			  	{	
			  		'name':"Bath",
			  		'credit':4,
			  		'estimatedTime' :10,
			  		'scheduledAt':-1,
					'scheduledTo':-1
			  	}
			 };


def clickOnB(b,i):
	messagebox.showinfo("see","Scheduled at "+str(activities[i]['scheduledAt'])+" to "+str(activities[i]['scheduledAt']))

scheduled = [0 for x in range(7)]
scheduled[0] = 0
for i in range(7):
	scheduled[i] = 0

def scheduleTasks():
	t = 600
	r = random.randint(0,6)
	for i in range(6):
		while(scheduled[r]==1):
			r = random.randint(0,6)
		scheduled[r] = 1
		# print(r)
		s = activities[r]['estimatedTime']
		# print(activities[r]['name'], "Start at ",t, "End at ",t+s)
		activities[r]['scheduledAt'] = t
		activities[r]['scheduledTo'] = t+s
		t = t+1.25*s
		if(t>840 and t<900):
			t = 840

l = [0 for x in range(7)]
scheduleTasks()
for i in range(7):
	l[i] = Button(window,text=activities[i]['name'],height=2,width=65,
	font=('Helvetica',15),command=lambda l=l,index=i:clickOnB(l,index))
	a=l[i]
	# print(a.cget('text'))
	if(i%2):
		l[i].configure(bg="blue")
	else:
		l[i].configure(bg="green")
	l[i].grid(row=i, column=0)



window.mainloop()
