import datetime
from tkinter import *
from tkcalendar import *
import ttkbootstrap as tb
import customtkinter as custk
import selectdatetime

TKINTER_WIDGET={}
TKINTER_DATA={}

fontjuan=("helvatica",14)

def post_top_level_select_datetime():
    global TKINTER_WIDGET
    TKINTER_WIDGET['widget_Date'].destroy()

def update_datetime():
    global TKINTER_DATA
    global TKINTER_WIDGET

    new_date = TKINTER_WIDGET['cal'].get_date()
    new_time = f"{new_date} {TKINTER_DATA['spinbox_hours'].get()}:{TKINTER_WIDGET['spinbox_minutes'].get()}"

    # Destroy widget_Date
    post_top_level_select_datetime()

    # Update Button Start Time
    TKINTER_WIDGET['button_start_time'].configure(text=new_time)

def scroll_hours(event):
    global TKINTER_WIDGET
    global TKINTER_DATA

    current_index = TKINTER_DATA['values_hours'].index(TKINTER_DATA['string_var_hours'].get())

    if event.delta > 0:
        if current_index < len(TKINTER_DATA['values_hours'])-1:
            current_index += 1
        else:
            current_index = 0
    else:
        current_index -= 1
    
    TKINTER_DATA['string_var_hours'].set(TKINTER_DATA['values_hours'][current_index])
    TKINTER_WIDGET['spinbox_hours'].config(textvariable=TKINTER_DATA['string_var_hours'])

def scroll_minutes(event):
    global TKINTER_WIDGET
    global TKINTER_DATA

    current_index = TKINTER_DATA['values_minutes'].index(TKINTER_WIDGET['spinbox_minutes'].get())

    if event.delta > 0:
        if current_index < len(TKINTER_DATA['values_minutes'])-1:
            current_index += 1
        else:
            current_index = 0
    else:
        current_index -= 1
    
    TKINTER_DATA['string_var_minutes'].set(TKINTER_DATA['values_minutes'][current_index])
    TKINTER_WIDGET['spinbox_minutes'].config(textvariable=TKINTER_DATA['string_var_minutes'])

def calendar():
    global TKINTER_WIDGET
    global TKINTER_DATA

    TKINTER_WIDGET['widget_Date'] = Toplevel(takefocus=True)
    TKINTER_WIDGET['widget_Date'].title("Select Date / Time")

    TKINTER_WIDGET['widget_Date'].geometry("230x300")
    TKINTER_WIDGET['widget_Date'].resizable(width=False, height=False)

    # frame calendar
    frame_calendar = custk.CTkFrame(master=TKINTER_WIDGET['widget_Date'],corner_radius=10)
    frame_calendar.grid(row=0,column=0,padx=15,pady=15,columnspan=3)

    # label Date
    label_date = custk.CTkLabel(master = frame_calendar,text="- Select Date -",width=30,height=5,corner_radius=7)
    label_date.grid(row=0, column=0, padx=10, pady=5, columnspan=3, sticky='n')

    # Calendar
    TKINTER_WIDGET['cal'] = Calendar(frame_calendar, selectmode='day', date_pattern='dd/mm/y', maxdate=datetime.datetime.today())
    TKINTER_WIDGET['cal'].grid(row=0, column=0, padx=20, pady=30, columnspan=3, sticky='s')

    # frame time
    frame_time = custk.CTkFrame(master = TKINTER_WIDGET['widget_Date'],corner_radius=10)
    frame_time.grid(row=1, column=0, padx=15, pady=5, columnspan=3)

    # label Time
    label_time = custk.CTkLabel(master = frame_time, text = "Time",width=30, height=5, corner_radius=7)
    label_time.grid(row=0,column=0,padx=10,pady=10)

    # create hours list
    TKINTER_DATA['values_hours'] = ['00']

    for i in range(1, 24):
        if len(str(i)) == 1:
            TKINTER_DATA['values_hours'].append(f'0{str(i)}')
        else:
            TKINTER_DATA['values_hours'].append(str(i))
        i+=1
    TKINTER_DATA['values_hours'] = tuple(TKINTER_DATA['values_hours'])

    # spinbox hours
    TKINTER_WIDGET['spinbox_hours'] = Spinbox(frame_time, values= TKINTER_DATA['values_hours'],justify= CENTER,width=10,wrap = True)
    TKINTER_WIDGET['spinbox_hours'].grid(row =0,column=1,padx=10)
    TKINTER_WIDGET['spinbox_hours'].bind("<MouseWheel>",scroll_hours)

    # Set Default Hour Value
    TKINTER_DATA['string_var_hours'] = StringVar()
    TKINTER_DATA['string_var_hours'].set('00')
    TKINTER_WIDGET['spinbox_hours'].config(textvariable = TKINTER_DATA['string_var_hours'])

    # create minutes list
    TKINTER_DATA['values_minutes'] = ['00']
    for i in range(1, 60):
        if len(str(i)) == 1:
            TKINTER_DATA['values_minutes'].append(f'0{str(i)}')
        else:
            TKINTER_DATA['values_minutes'].append(str(i))
        i+=1
    TKINTER_DATA['values_minutes'] = tuple(TKINTER_DATA['values_minutes'])

    # spinbox minutes
    TKINTER_WIDGET['spinbox_minutes'] = Spinbox(frame_time, values= TKINTER_DATA['values_minutes'],justify= CENTER, width = 10, wrap = True)
    TKINTER_WIDGET['spinbox_minutes'].grid(row = 0,column = 2, padx =10)
    TKINTER_WIDGET['spinbox_minutes'].bind("<MouseWheel>",scroll_minutes)

    # TextVariable for Minutes 
    TKINTER_DATA['string_var_minutes'] = StringVar()
    
    # Button Select Date Time OK
    button_datetime_ok = custk.CTkButton(master = TKINTER_WIDGET['widget_Date'],text="OK",width=70,command=update_datetime)
    button_datetime_ok.grid(row = 2,column=0,padx=60,pady=15,sticky='sw')

    # Button Select Date Time Cancel
    button_datetime_cancel = custk.CTkButton(master = TKINTER_WIDGET['widget_Date'],text = "Cancel",fg_color="gray74",hover_color="#EEE",text_color="#000",width =70,command = post_top_level_select_datetime)
    button_datetime_cancel.grid(row = 2,column= 0,padx=60,pady=15,sticky='se')

def openAddFilterWindow():
    global TKINTER_WIDGET
    global TKINTER_DATA
    
    af = Toplevel()
    af.title("ADD FILTER")
    af.maxsize(800,600)
    af.configure(bg="gray49")
    
    frame1 = Frame(af,width=400,height=600)
    frame1.grid()
    frame1.configure(bg='gray49')

    # Create frames and labels in frame
    # Label and entry event category
    TKINTER_WIDGET['label_event_category']=custk.CTkLabel(master=frame1,text="Event Category",width=130,height=30,font=fontjuan,corner_radius=7)
    TKINTER_WIDGET['label_event_category'].grid(row=0,column=0,padx=5,pady=5)

    TKINTER_WIDGET['entry_event_category']=tb.Entry(frame1,font=fontjuan,width=15)
    TKINTER_WIDGET['entry_event_category'].grid(row=0,column=1,padx=5,pady=10)

    # Label and entry source name
    TKINTER_WIDGET['label_source_name']=custk.CTkLabel(master=frame1,text="Source Name",width=130,height=30,font=fontjuan,corner_radius=7)
    TKINTER_WIDGET['label_source_name'].grid(row=1,column=0,padx=5,pady=5)

    TKINTER_WIDGET['entry_source_name']=tb.Entry(frame1,font=fontjuan,width=15)
    TKINTER_WIDGET['entry_source_name'].grid(row=1,column=1,pady=5,padx=10)

    # Label and entry start time
    TKINTER_WIDGET['label_start_time']=custk.CTkLabel(master=frame1,text="Start Date",font=fontjuan,corner_radius=7)
    TKINTER_WIDGET['label_start_time'].grid(row=2,column=0,padx=5,pady=5)

    current_datetime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    TKINTER_WIDGET['button_start_time']=custk.CTkButton(master=frame1,fg_color="black",hover_color="white",text_color="#00BC8C",border_color="#00BC8C",text=current_datetime,command=selectdatetime.select_date_time)
    TKINTER_WIDGET['button_start_time'].grid(row=2,column=1,padx=5,pady=10)

    # Label and entry end time
    TKINTER_WIDGET['label_end_time']=custk.CTkLabel(master=frame1,text="End Date",font=fontjuan,corner_radius=7)
    TKINTER_WIDGET['label_end_time'].grid(row=3,column=0,padx=5,pady=5)

    TKINTER_WIDGET['button_end_time']=custk.CTkButton(master=frame1,fg_color="black",hover_color="white",text_color="#00BC8C",border_color="#00BC8C",text=current_datetime,command=selectdatetime.select_date_time)
    TKINTER_WIDGET['button_end_time'].grid(row=3,column=1,padx=5,pady=10)

    # Label and entry Event ID
    TKINTER_WIDGET['label_event_id']=custk.CTkLabel(master=frame1,text="Event ID",font=fontjuan,corner_radius=7)
    TKINTER_WIDGET['label_event_id'].grid(row=4,column=0,padx=5,pady=5)

    TKINTER_WIDGET['entry_event_id']=tb.Entry(frame1,font=fontjuan,width=15)
    TKINTER_WIDGET['entry_event_id'].grid(row=4,column=1,pady=5,padx=10)

    # Label and combobox event type
    TKINTER_WIDGET['label_event_type']=custk.CTkLabel(master=frame1,text="Event Type",font=fontjuan,corner_radius=7)
    TKINTER_WIDGET['label_event_type'].grid(row=5,column=0,padx=5,pady=5)

    TKINTER_WIDGET['combobox_event_type']=custk.CTkComboBox(master=frame1,corner_radius=10,values = ("Information","Warning","Error","Audit Success","Audit Failure","Unknown"))        
    TKINTER_WIDGET['combobox_event_type'].grid(row=5,column=1,pady=5,padx=10)

    # Label and combobox send to
    TKINTER_WIDGET['label_send_to']=custk.CTkLabel(master=frame1,text="Send to",font=fontjuan,corner_radius=7)
    TKINTER_WIDGET['label_send_to'].grid(row=6,column=0,padx=5,pady=5)

    TKINTER_WIDGET['combobox_send_to']=custk.CTkComboBox(master=frame1,corner_radius=10,values=("MSTeams","Email"))
    TKINTER_WIDGET['combobox_send_to'].grid(row=6,column=1,pady=5,padx=10)

    # Label and entry your email
    TKINTER_WIDGET['label_your_email']=custk.CTkLabel(master=frame1,text="Your Email",font=fontjuan,corner_radius=7)
    TKINTER_WIDGET['label_your_email'].grid(row=7,column=0,pady=5,padx=5)

    TKINTER_WIDGET['entry_your_email']=tb.Entry(frame1,font=fontjuan,width=15)
    TKINTER_WIDGET['entry_your_email'].grid(row=7,column=1,pady=5,padx=10)