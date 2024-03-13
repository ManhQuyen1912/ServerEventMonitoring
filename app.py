from tkinter import * 
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from main import *

root = tb.Window(themename="darkly")
root.title("Server Monitor Event Software")
root.maxsize(800, 600)
root.configure(background="white")

# Create Frame
frame = Frame(root, width=400, height=600)
frame.grid(row=0, column=0,padx=20,pady=20)
frame.configure(background='gray49')

# Create frames and labels in frame
evtCatL= tb.Label(frame, 
                text="Event Category",
                font=("helvatica",13),
                bootstyle='light, inverse').grid(row=0, column=0, padx=5, pady=5)
entry1= tb.Entry(frame,
                font=("helvatica",12), 
                width=15).grid(row=0,column=1,sticky=W,pady=5,padx=20)

srcNameL= tb.Label(frame, 
                text="Source Name",
                font=("helvatica",13),
                bootstyle='light, inverse').grid(row=1, column=0, padx=5, pady=5)
entry2= tb.Entry(frame,
                font=("helvatica",12),
                width=15).grid(row=1,column=1,sticky=W,pady=5,padx=20)

timeStL= tb.Label(frame, 
                text="Time Start",
                font=("helvatica",13),
                bootstyle='light, inverse').grid(row=2, column=0, padx=5, pady=5)
entry3= tb.Entry(frame,
                font=("Helvatica",12),
                width=15).grid(row=2,column=1,sticky=W,pady=5,padx=20)

timeEndL= tb.Label(frame, 
                  text="Time End",
                  font=("helvatica",13),
                  bootstyle='light, inverse').grid(row=3, column=0, padx=5, pady=5)
entry4=tb.Entry(frame,
                font=("Helvatica",12),
                width=15).grid(row=3,column=1,sticky=W,pady=5,padx=20)

evtIDL= tb.Label(frame, 
                text="Event ID",
                font=("helvatica",13),
                bootstyle='light, inverse').grid(row=4, column=0, padx=5, pady=5)
entry5=tb.Entry(frame,
                font=("Helvatica",12),
                width=15).grid(row=4,column=1,sticky=W,pady=5,padx=20)

evtTypeL= tb.Label(frame, 
                  text="Event Type",
                  font=("helvatica",13),
                  bootstyle='light, inverse').grid(row=5,column=0,pady=5, padx=5)
eventType=["Information","Warning","Error","Audit Success","Audit Failure","Unknown"]
comboBox= tb.Combobox(frame,
                      bootstyle="success",
                      values = eventType,
                      width=17).grid(row=5,column=1,sticky=W,pady=5,padx=20)

listsend=["MSTeams","Gmail"]
chooseL = tb.Label(frame,
                  text="Send to",
                  font=("helvatica",13),
                  bootstyle='light,inverse').grid(row=6,column=0,padx=5,pady=5)
comboBox= tb.Combobox(frame,
                      bootstyle="success",
                      values=listsend,
                      width=7).grid(row=6,column=1,padx=5,pady=5)

mailL = tb.Label(frame,
                text="Your mail",
                font=("helvatica",13),
                bootstyle='light,inverse').grid(row=7,column=0,padx=5,pady=20)
entry6= tb.Entry(frame,
                font=("helvatica",12), 
                width=15).grid(row=7,column=1,sticky=W,pady=5,padx=20)

# Function Get data from Entry
def get_data():
    evtCat = evtCatL.get()
    srcName = srcNameL.get()
    timeSt = timeStL.get()
    timeEnd = timeEndL.get()
    evtID = evtIDL.get()
    evtType = evtTypeL.get()    

# Colors: default, primary, secondary, success, info, warning, danger, light, dark
button_search = tb.Button(frame,text="Search",bootstyle="success,outline",command=get_data).grid(row=8,column=0,padx=10,sticky=E)
button_send = tb.Button(frame,text="Send",bootstyle="success,outline").grid(row=8,column=1,padx=30,sticky=W)
# set combo default
# comboBox.current(0)

root.mainloop()