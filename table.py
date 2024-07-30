from tkinter import *
import ttkbootstrap as tb

def create_tree():
    tree = tb.ttk.Treeview(columns=("1","2","3","4","5","6"),show='headings',height= 10)
    tree.column("#1",anchor='center',stretch=YES,width=140)
    tree.heading("#1", text="Event Category")
    tree.column("#2",anchor='center',stretch=YES)
    tree.heading("#2", text="Source Name")
    tree.column("#3",anchor='center',stretch=YES,width=220)
    tree.heading("#3", text="Time Generated")
    tree.column("#4",anchor='center',stretch=YES,width=120)
    tree.heading("#4", text="Event ID")
    tree.column("#5",anchor='center',stretch=YES,width=110)
    tree.heading("#5", text="Event Type")
    tree.column("#6",stretch=YES)
    tree.heading("#6", text="Event String")
    tree.grid()
    return tree

def insert(x,tree):
    y=x.split("\t")
    tree.insert(
        "",
        tb.END,
        text=1,
        values=(y[0],y[1],y[2],y[3],y[4],y[5])
    )
    
def clear_tree(tree):
    # Get all existing children (rows)
    children = tree.get_children()

    # Efficiently delete all children in a loop
    for child in children:
        tree.delete(child)

def inserttuple(y,tree):
    tree.insert(
        "",
        tb.END,
        text=1,
        values=(y[1],y[3],y[2],y[4],y[5],y[6])
    )