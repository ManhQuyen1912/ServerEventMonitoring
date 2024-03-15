from tkinter import * 
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from ttkbootstrap import Style
from main import *
from addfiltergui import *
from tkinter import ttk
import tkinter as tk
import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite3
connection = sqlite3.connect('path_to_your_database.db')
cursor = connection.cursor()

# Thực thi truy vấn SELECT để lấy dữ liệu từ bảng
cursor.execute("SELECT * FROM table_name")
rows = cursor.fetchall()

# Tạo giao diện
root = tk.Tk()
style = Style(theme='bootstrap')

treeview = ttk.Treeview(root, style="data.Treeview")
treeview['columns'] = ('column1', 'column2', 'column3')  # Các cột trong bảng

# Đặt tên cho các cột
treeview.heading('#0', text='ID')
treeview.heading('column1', text='Column 1')
treeview.heading('column2', text='Column 2')
treeview.heading('column3', text='Column 3')

# Thêm dữ liệu vào từng dòng của bảng
for row in rows:
    treeview.insert('', 'end', text=row[0], values=(row[1], row[2], row[3]))

treeview.pack(fill=tk.BOTH, expand=True)

# Đóng kết nối
connection.close()

root = tb.Window(themename="darkly")
root.title("Server Monitor Event Software")
root.maxsize(1200, 1600)
root.configure(bg="gray48")

tb.Label(root,text="Event Annouce",background="gray48",font=("helvatica",15)).grid()

# Create Frame
frame = Frame(root, width=400, height=600)
frame.grid(row=1, column=0,padx=20,pady=20)
frame.configure(bg='gray49')

button_send = tb.Button(frame,text="Send",bootstyle="success,outline",command=openAddFilterWindow).grid(row=8,column=1,padx=30)
root.mainloop()