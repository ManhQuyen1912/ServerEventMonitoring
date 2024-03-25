import tkinter as tk
import ttkbootstrap as tb
from tkinter import *

fontjuan=("helvatica",12)
filterList = []
def openAddFilterWindow():
    af = tk.Toplevel()
    af.title("ADD FILTER")
    af.maxsize(800,600)
    af.configure(bg="gray49")
    
    frame1 = Frame(af,width=400,height=600)
    frame1.grid()
    frame1.configure(bg='gray49')
    # Create frames and labels in frame
    tb.Label(frame1, 
            text="Event Category",
            font=fontjuan,
            bootstyle='light, inverse').grid(row=0, column=0, padx=5, pady=5)
    eventCate= tb.Entry(frame1,
                    font=fontjuan, 
                    width=15)
    eventCate.grid(row=0,column=1,sticky=W,pady=5,padx=20)

    tb.Label(frame1, 
            text="Source Name",
            font=("helvatica",13),
            bootstyle='light, inverse').grid(row=1, column=0, padx=5, pady=5)
    srcName= tb.Entry(frame1,
                    font=fontjuan,
                    width=15)
    srcName.grid(row=1,column=1,sticky=W,pady=5,padx=20)

    tb.Label(frame1, 
            text="Time Start",
            font=fontjuan,
            bootstyle='light, inverse').grid(row=2, column=0, padx=5, pady=5)
    timeStart= tb.Entry(frame1,
                    font=fontjuan,
                    width=15)
    timeStart.grid(row=2,column=1,sticky=W,pady=5,padx=20)

    tb.Label(frame1, 
            text="Time End",
            font=fontjuan,
            bootstyle='light, inverse').grid(row=3, column=0, padx=5, pady=5)
    timeEnd=tb.Entry(frame1,
                    font=fontjuan,
                    width=15)
    timeEnd.grid(row=3,column=1,sticky=W,pady=5,padx=20)
    
    tb.Label(frame1,
            text = "Date",
            font = fontjuan,
            bootstyle = 'light, inverse').grid(row=4, column=0,padx=5,pady=5)
    date = tb.Entry(frame1,
                      font = fontjuan,
                      width = 15)
    date.grid(row = 4,column = 1, padx=5,pady=5)

    tb.Label(frame1, 
            text="Event ID",
            font=fontjuan,
            bootstyle='light, inverse').grid(row=5, column=0, padx=5, pady=5)
    eventID=tb.Entry(frame1,
                    font=fontjuan,
                    width=15)
    eventID.grid(row=5,column=1,sticky=W,pady=5,padx=20)

    tb.Label(frame1, 
            text="Event Type",
            font=fontjuan,
            bootstyle='light, inverse').grid(row=6,column=0,pady=5, padx=5)
    tb.Combobox(frame1,
                bootstyle="success",
                values =("Information","Warning","Error","Audit Success","Audit Failure","Unknown"),
                width=17).grid(row=6,column=1,sticky=W,pady=5,padx=20)

    tb.Label(frame1,
            text="Send to",
            font=fontjuan,
            bootstyle='light,inverse').grid(row=7,column=0,padx=5,pady=5)
    tb.Combobox(frame1,
                bootstyle="success",
                values=("MSTeams","Gmail"),
                width=7).grid(row=7,column=1,padx=5,pady=5)

    tb.Label(frame1,
            text="Your mail",
            font=fontjuan,
            bootstyle='light,inverse').grid(row=8,column=0,padx=5,pady=20)
    urMail = tb.Entry(frame1,
                     font=fontjuan, 
                     width=15)
    urMail.grid(row=8,column=1,sticky=W,pady=5,padx=20)

    # Function Get data from Entry
    # hàm vẫn còn thiếu eventType và listsend
    def get_data():
        entries = [eventCate, srcName, timeStart, timeEnd, date, eventID, urMail]
        for entry in entries:
            if entry.get() is not None:
                filterList.append(entry.get())
            else:
                filterList.append('')
        return filterList
    
    # Function Filter data
    def filtering(filterList):
        filter_list = get_data()  # Lấy các giá trị nhập từ hàm get_data()
        filtered_results = []

        # Nên lưu dữ liệu theo kiểu dictionary bởi vì nếu chỉ lưu theo text và ngăn cách giữa các
        # phần tử chỉ bằng \t sẽ rất khó để filter dữ liệu
        # data = {
        #     'eventCate': ''
        #     'srcName' : ''
        #     'timeGene' : ''
        #     'eventID' : ''
        #     'eventType' : ''
        #     'eventStr' : ''
        # }

        for data_row in your_data_list:
            if (filter_list[0] == '' or data_row["Event Category"] == filter_list[0]) and \
            (filter_list[1] == '' or data_row["Source Name"] == filter_list[1]) and \
            (filter_list[2] == '' or data_row["Time Generated"] >= filter_list[2]) and \
            (filter_list[3] == '' or data_row["Time Generated"] <= filter_list[3]) and \
            (filter_list[4] == '' or data_row["Date"] == filter_list[4]) and \
            (filter_list[5] == '' or data_row["Event ID"] == filter_list[5]) and \
            (filter_list[6] == '' or data_row["Email"] == filter_list[6]):
                filtered_results.append(data_row)
        return filtered_results
    
    # Colors: default, primary, secondary, success, info, warning, danger, light, dark
    button_filter = tb.Button(af,text="Filter",bootstyle="success,outline",command=filtering).grid()
    # set combo default
    # comboBox.current(0)