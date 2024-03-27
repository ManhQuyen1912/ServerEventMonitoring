from tkinter import *
import datetime
from tkcalendar import *
import customtkinter as custk


def scroll_hours(event):
    global values_hours
    global spinbox_hours
    global string_var_hours

    current_index = values_hours.index(string_var_hours.get())
    if event.delta > 0:
        if current_index < len(values_hours)-1:
            current_index += 1
        else:
            current_index = 0
    else:
        current_index -= 1
    string_var_hours.set(values_hours[current_index])
    spinbox_hours.config(textvariable=string_var_hours)

def scroll_minutes(event):
    global values_minutes
    global spinbox_minutes
    global string_var_minutes

    current_index = values_minutes.index(string_var_minutes.get())
    if event.delta >0:
        if current_index < len(values_minutes)-1:
            current_index +=1
        else:
            current_index =0
    else:
        current_index -=1
    string_var_minutes=set(values_minutes[current_index])
    spinbox_minutes.config(textvariable=string_var_minutes)

def post_top_level_select_datetime():
    global widget_Date
    widget_Date.destroy()

def update_datetime():
    global cal
    global spinbox_hours
    global spinbox_minutes

    # Get new date time details
    new_date = cal.get_date()
    new_time = f'{new_date} {spinbox_hours.get()}:{spinbox_minutes.get()}'

    # Destroy widget_Date
    post_top_level_select_datetime()

    # Update Date Entry
    print(new_time)

def select_date_time():
    global widget_Date
    global values_hours
    global values_minutes
    global spinbox_hours
    global spinbox_minutes
    global string_var_hours
    global string_var_minutes
    global cal

    widget_Date = custk.CTkToplevel(takefocus=True)
    widget_Date.title("Select Date / Time")

    widget_Date.geometry("230x300")
    widget_Date.resizable(width=False, height=False)

    # frame calendar
    frame_calendar = custk.CTkFrame(master=widget_Date,corner_radius=10)
    frame_calendar.grid(row=0,column=0,padx=15,pady=15,columnspan=3)

    # label Date
    label_date = custk.CTkLabel(master = frame_calendar,text="- Select Date -",width=30,height=5,corner_radius=7)
    label_date.grid(row=0, column=0, padx=10, pady=5, columnspan=3, sticky='n')

    # Calendar
    cal = Calendar(frame_calendar, selectmode='day', date_pattern='dd/mm/y', maxdate=datetime.datetime.today())
    cal.grid(row=0, column=0, padx=20, pady=30, columnspan=3, sticky='s')

    # frame time
    frame_time = custk.CTkFrame(master = widget_Date,corner_radius=10)
    frame_time.grid(row=1, column=0, padx=15, pady=5, columnspan=3)

    # label Time
    label_time = custk.CTkLabel(master = frame_time, text = "Time",width=30, height=5, corner_radius=7)
    label_time.grid(row=0,column=0,padx=10,pady=10)

    # create hours list
    values_hours = ['00']

    for i in range(1, 24):
        if len(str(i)) == 1:
            values_hours.append(f'0{str(i)}')
        else:
            values_hours.append(str(i))
        i+=1
    values_hours = tuple(values_hours)

    # spinbox hours
    spinbox_hours = Spinbox(frame_time, values= values_hours,justify= CENTER,width=10,wrap = True)
    spinbox_hours.grid(row =0,column=1,padx=10)
    spinbox_hours.bind("<MouseWheel>",scroll_hours)

    # Set Default Hour Value
    string_var_hours = StringVar()
    string_var_hours.set('00')
    spinbox_hours.config(textvariable = string_var_hours)

    # create minutes list
    values_minutes = ['00']
    for i in range(1, 60):
        if len(str(i)) == 1:
            values_minutes.append(f'0{str(i)}')
        else:
            values_minutes.append(str(i))
        i+=1
    values_minutes = tuple(values_minutes)

    # spinbox minutes
    spinbox_minutes = Spinbox(frame_time, values= values_minutes,justify= CENTER, width = 10, wrap = True)
    spinbox_minutes.grid(row = 0,column = 2, padx =10)
    spinbox_minutes.bind("<MouseWheel>",scroll_minutes)

    # TextVariable for Minutes 
    string_var_minutes = StringVar()
    
    # Button Select Date Time OK
    button_datetime_ok = custk.CTkButton(master = widget_Date,text="OK",width=70,command=update_datetime)
    button_datetime_ok.grid(row = 2,column=0,padx=60,pady=15,sticky='sw')

    # Button Select Date Time Cancel
    button_datetime_cancel = custk.CTkButton(master = widget_Date,text = "Cancel",fg_color="gray74",hover_color="#EEE",text_color="#000",width =70,command = post_top_level_select_datetime)
    button_datetime_cancel.grid(row = 2,column= 0,padx=60,pady=15,sticky='se')

    # Function Get data from Entry
    # hàm vẫn còn thiếu eventType và listsend
#     def get_data():
#         filterList = []
#         entries = [eventCate, srcName, timeStart, timeEnd, dateStart, dateEnd, eventID, urMail]
#         for entry in entries:
#             if entry.get() is not None:
#                 filterList.append(entry.get())
#             else:
#                 filterList.append('')
#         return filterList
if __name__ == "__main__":
    root = custk.CTk()
    select_date_time()
    root.mainloop()