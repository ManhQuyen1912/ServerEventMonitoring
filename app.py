from tkinter import * 
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="darkly")
root.title("Server Monitor Event Software")
root.maxsize(800, 600)
root.configure(background="white")

# Create Frame
left_frame = Frame(root, width=400, height=600)
left_frame.grid(row=0, column=0, padx=10, pady=10)
left_frame.configure(background='gray49')

# Create frames and labels in left_frame
evtCat= tb.Label(left_frame, 
                text="Event Category",
                font=("helvatica",13),
                bootstyle='light, inverse').grid(row=0, column=0, padx=5, pady=5)
entry1= tb.Entry(left_frame,
                font=("helvatica",12), 
                width=15).grid(row=1,column=0,sticky=E,pady=5,padx=20)

srcName= tb.Label(left_frame, 
                text="Source Name",
                font=("helvatica",13),
                bootstyle='light, inverse').grid(row=0, column=1, padx=5, pady=5)
entry2= tb.Entry(left_frame,
                font=("helvatica",12),
                width=15).grid(row=1,column=1,sticky=W,pady=5,padx=20)

timeSt= tb.Label(left_frame, 
                text="Time Start",
                font=("helvatica",13),
                bootstyle='light, inverse').grid(row=2, column=0, padx=5, pady=5)
entry3= tb.Entry(left_frame,
                font=("Helvatica",12),
                width=15).grid(row=3,column=0,sticky=E,pady=5,padx=20)

tiemEnd= tb.Label(left_frame, 
                  text="Time End",
                  font=("helvatica",13),
                  bootstyle='light, inverse').grid(row=2, column=1, padx=5, pady=5)
entry3=tb.Entry(left_frame,
                font=("Helvatica",12),
                width=15).grid(row=3,column=1,sticky=W,pady=5,padx=20)

evtID= tb.Label(left_frame, 
                text="Event ID",
                font=("helvatica",13),
                bootstyle='light, inverse').grid(row=4, column=0, padx=5, pady=5)
entry4=tb.Entry(left_frame,
                font=("Helvatica",12),
                width=15).grid(row=5,column=0,sticky=E,pady=5,padx=20)

evtType= tb.Label(left_frame, 
                  text="Event Type",
                  font=("helvatica",13),
                  bootstyle='light, inverse').grid(row=4,column=1,pady=5, padx=5)
eventType=["Information","Warning","Error","Audit Success","Audit Failure","Unknown"]
comboBox= tb.Combobox(left_frame,bootstyle="success",
                      values = eventType,
                      width=18).grid(row=5,column=1,sticky=E,pady=5,padx=20)

# Colors: default, primary, secondary, success, info, warning, danger, light, dark
button = tb.Button(text="Search",bootstyle="secondary,outline").grid(pady=20,padx=5)
# set combo default
# comboBox.current(0)

root.mainloop()