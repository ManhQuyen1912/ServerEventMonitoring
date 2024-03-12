from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="darkly")
root.title("Server Monitor Event Software")
# root.geometry("800x600")

# frame = tb.Frame(root, width= 800, height=600,bootstyle="light")
# frame.pack(pady=20)

# my_label = tb.Label(frame, text="Event Type",font=("Helvetica",12))
# my_label.pack(pady=10,padx=20,anchor=W)

# evt_Cate = tb.Label(frame,text="Event Category",font=("helvatica",12))
# evt_Cate.pack(pady=10,padx=20,anchor=E)
root.maxsize(800, 600)  # specify the max size the window can expand to

# Create left and right frames
left_frame = Frame(root, width=400, height=600, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)

# Create frames and labels in left_frame
Label(left_frame, text="Event Category").grid(row=0, column=0, padx=5, pady=5)
entry1=tb.Entry(left_frame,font=("helvatica",12),width=15).grid(row=1,column=0,sticky=E,pady=5,padx=20)

Label(left_frame, text="Time Generated").grid(row=0, column=1, padx=5, pady=5)
entry2=tb.Entry(left_frame,font=("helvatica",12),width=15).grid(row=1,column=1,sticky=W,pady=5,padx=20)

Label(left_frame, text="Source Name").grid(row=2, column=0, padx=5, pady=5)
entry3=tb.Entry(left_frame,font=("Helvatica",12),width=15).grid(row=3,column=0,sticky=E,pady=5,padx=20)

Label(left_frame, text="Event ID").grid(row=2, column=1, padx=5, pady=5)
entry4=tb.Entry(left_frame,font=("Helvatica",12),width=15).grid(row=3,column=1,sticky=W,pady=5,padx=20)

Label(left_frame, text="Event Type").grid(row=4,column=0,pady=5, padx=5)
eventType=["Information","Warning","Error","Audit Success","Audit Failure","Unknown"]
comboBox= tb.Combobox(left_frame,bootstyle="success",values = eventType,width=18).grid(row=5,column=0,sticky=W,pady=5,padx=20)

# set combo default
# comboBox.current(0)

root.mainloop()