import tkinter as tk
import ttkbootstrap as tb
from tkinter import *

fontjuan=("helvatica",12)

def openAddFilterWindow():
    af = tk.Toplevel()
    af.title("ADD FILTER")
    af.maxsize(800,600)
    af.configure(bg="gray49")
    
    frame1 = Frame(af,width=400,height=600)
    frame1.grid()
    frame1.configure(bg='gray49')
    # Create frames and labels in frame
    evtCatL= tb.Label(frame1, 
                    text="Event Category",
                    font=fontjuan,
                    bootstyle='light, inverse').grid(row=0, column=0, padx=5, pady=5)
    entry1= tb.Entry(frame1,
                    font=fontjuan, 
                    width=15).grid(row=0,column=1,sticky=W,pady=5,padx=20)

    srcNameL= tb.Label(frame1, 
                    text="Source Name",
                    font=("helvatica",13),
                    bootstyle='light, inverse').grid(row=1, column=0, padx=5, pady=5)
    entry2= tb.Entry(frame1,
                    font=fontjuan,
                    width=15).grid(row=1,column=1,sticky=W,pady=5,padx=20)

    timeStL= tb.Label(frame1, 
                    text="Time Start",
                    font=fontjuan,
                    bootstyle='light, inverse').grid(row=2, column=0, padx=5, pady=5)
    entry3= tb.Entry(frame1,
                    font=fontjuan,
                    width=15).grid(row=2,column=1,sticky=W,pady=5,padx=20)

    timeEndL= tb.Label(frame1, 
                    text="Time End",
                    font=fontjuan,
                    bootstyle='light, inverse').grid(row=3, column=0, padx=5, pady=5)
    entry4=tb.Entry(frame1,
                    font=fontjuan,
                    width=15).grid(row=3,column=1,sticky=W,pady=5,padx=20)

    evtIDL= tb.Label(frame1, 
                    text="Event ID",
                    font=fontjuan,
                    bootstyle='light, inverse').grid(row=4, column=0, padx=5, pady=5)
    entry5=tb.Entry(frame1,
                    font=fontjuan,
                    width=15).grid(row=4,column=1,sticky=W,pady=5,padx=20)

    evtTypeL= tb.Label(frame1, 
                    text="Event Type",
                    font=fontjuan,
                    bootstyle='light, inverse').grid(row=5,column=0,pady=5, padx=5)
    eventType=["Information","Warning","Error","Audit Success","Audit Failure","Unknown"]
    comboBox= tb.Combobox(frame1,
                        bootstyle="success",
                        values = eventType,
                        width=17).grid(row=5,column=1,sticky=W,pady=5,padx=20)

    listsend=["MSTeams","Gmail"]
    chooseL = tb.Label(frame1,
                    text="Send to",
                    font=fontjuan,
                    bootstyle='light,inverse').grid(row=6,column=0,padx=5,pady=5)
    comboBox= tb.Combobox(frame1,
                        bootstyle="success",
                        values=listsend,
                        width=7).grid(row=6,column=1,padx=5,pady=5)

    mailL = tb.Label(frame1,
                    text="Your mail",
                    font=fontjuan,
                    bootstyle='light,inverse').grid(row=7,column=0,padx=5,pady=20)
    entry6= tb.Entry(frame1,
                    font=fontjuan, 
                    width=15).grid(row=7,column=1,sticky=W,pady=5,padx=20)

    # Function Get data from Entry
    def get_data():
        if(entry1.get()==''):
            evtCat = ''
        else:   
            evtCat = entry1.get()
        if(entry2.get()==''):
            srcName = ''
        else:
            srcName = entry2.get()
        if(entry3.get()==''):
            timeSt = ''
        else:
            timeSt = entry3.get()
        if(entry4.get()==''):
            timeEnd = ''
        else:
            timeEnd = entry4.get()
        if(entry5.get()==''):
            evtID = ''
        else:
            evtID = entry5.get()
        if(entry6.get()==''):
            evtType = ''
        else:
            evtType = entry6.get()   
    

    # Colors: default, primary, secondary, success, info, warning, danger, light, dark
    button_filter = tb.Button(af,text="Filter",bootstyle="success,outline",command=get_data).grid()
    # set combo default
    # comboBox.current(0)