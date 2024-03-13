from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="darkly")
root.title("Server Monitor Event Software")
root.geometry("800x600")

# frame = Frame(root, width= 800, height=600,)
# frame.grid(row = 2, column=1,padx=5,pady=5)

my_label = tb.Label(root, text="Event Type",font=("Helvetica",12))
my_label.pack(pady=10,padx=20,anchor=W)

# Label(frame,text="Event Category").grid(row=0,column=0,padx=10,pady=10)

eventType=["Information","Warning"]

comboBox= tb.Combobox(root,bootstyle="success",values = eventType)
comboBox.pack(pady=0,padx=20,anchor=W)
# set combo default
# comboBox.current(0)

root.mainloop()