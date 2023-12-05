from tkinter import *
from tkinter import messagebox
#FUNCTION FOR DELETION
def deleteTask():
    lb.delete(ANCHOR)
#FUNCTION FOR ADDING TASK
def newTask():
    task=my_entry.get()
    if task!="":
        lb.insert(END,task)
        my_entry.delete(0,"end")
    else:
        messagebox.showwarning("warning","please enter a task")
# PARENT WINDOW CODE
tl = Tk()
tl.geometry('500x400+500+200')
tl.title("TO-DO LIST")
tl.config(bg="#50C878")
tl.resizable(width=True, height=True)  #WIDTH AND HEIGHT CAN BE CHANGED ACCORDINGLY

#WIDGETS CREATION(BUTTONS,SCROLL BAR,LISTBOX)
frame=Frame(tl)
frame.pack(pady=10)    #FRAME IS NEEDED TO USE BUTTONS,SCROLL BAR

# TASKS WE ADD WILL BE DISPLAYED
lb=Listbox(frame,width=35,height=10,font=('Times',15),highlightthickness=0,bd=0,fg='#464646',selectbackground='#a6a6a6')
lb.pack(side=LEFT,fill=BOTH)

#DEFAULT TASKS 
task_list=["exercise","study","drink water"]
for item in task_list:
    lb.insert(END,item)

# SCROLL BAR CODE
sb=Scrollbar(frame)
sb.pack(side=RIGHT,fill=BOTH)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

#TO ENTER TASKS
my_entry=Entry(tl,font=('Times',24))
my_entry.pack(pady=20)
button_frame=Frame(tl)
button_frame.pack(pady=20)

# ADD BUTTON AND ITS FUNCTION CALL
addTask_btn=Button(button_frame,text='ADD task',font=('Times',14),bg='#ff8b61',padx=20,pady=10,command=newTask)
addTask_btn.pack(fill=BOTH,expand=True,side=LEFT)

# DEL BUTTON AND ITS FUNCTION CALL
delTask_btn=Button(button_frame,text='Delete Task',font=('Times',14),bg='#c5f776',padx=20,pady=10,command=deleteTask)
delTask_btn.pack(fill=BOTH,expand=True,side=LEFT)

#CALLING MAIN
tl.mainloop()
