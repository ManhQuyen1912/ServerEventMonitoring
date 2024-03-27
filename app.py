from tkinter import * 
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from tkinter import ttk
from addfiltergui import *
from table import *

root = tb.Window(themename="darkly")
root.title("Server Monitor Event Software")
root.maxsize(1200, 1600)
root.configure(bg="gray48")

tb.Label(root,text="Event Annouce",background="gray48",font=("helvatica",18)).grid()

tree = create_tree()
txt="None\t2024-03-13 15:07:22\tService Control Manager\t1073748864\tInformation\t('Background Intelligent Transfer Service', 'auto start', 'demand start', 'BITS')"
insert(txt,tree)
i="None\t2024-03-13 06:33:18\tMicrosoft-Windows-Time-Service\t158\tInformation\t('VMICTimeProvider',)"
insert(i,tree)


# Create Frame
frame = Frame(root, width=400, height=600)
frame.grid(row=5, column=0,padx=20,pady=20)
frame.configure(bg='gray49')

button_send = tb.Button(frame,text="Send",bootstyle="success,outline",command=openAddFilterWindow).grid(row=8,column=1,padx=30)
root.mainloop()