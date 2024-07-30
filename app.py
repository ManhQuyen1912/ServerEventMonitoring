from tkinter import * 
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from tkinter import ttk
from winEvtMonitor import fetch_all_logs, winEvtMonitor
from addfiltergui import *
from table import *
import threading

root = tb.Window(themename="darkly")
root.title("Server Event Monitoring Software")
root.maxsize(1200, 1600)
root.configure(bg="gray48")

tb.Label(root,text="Event Annouce",background="gray48",font=("helvatica",18)).grid()

def insert_new_log(log):
    insert(log, tree)

def start_monitoring():
    monitoring_thread = threading.Thread(target= winEvtMonitor, args=(insert_new_log,))
    monitoring_thread.daemon = True
    monitoring_thread.start()

tree = create_tree()

logs = fetch_all_logs()

for log in logs:
    insert_new_log(log)

# Create Frame
frame = Frame(root, width=400, height=600)
frame.grid(row=5, column=0,padx=20,pady=20)
frame.configure(bg='gray49')

button_send = tb.Button(frame,text="Send",bootstyle="success,outline",command=lambda:openAddFilterWindow(tree)).grid(row=8,column=1,padx=30)

start_monitoring()
root.mainloop()