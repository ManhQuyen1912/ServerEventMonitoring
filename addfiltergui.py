import datetime
from tkinter import *
from tkcalendar import *
import ttkbootstrap as tb
import customtkinter as custk
from SqlService import query
from table import *

TKINTER_WIDGET={}
TKINTER_DATA={}

fontjuan=("helvatica",14)

def calen():
    global TKINTER_WIDGET
    global TKINTER_DATA

    TKINTER_WIDGET['frame_calendar'] = Frame(TKINTER_WIDGET['af'],width=230,height=300)
    TKINTER_WIDGET['frame_calendar'].grid(row=0,column=1,padx=15,pady=10,columnspan=3)

    # label Date
    label_date = Label(master = TKINTER_WIDGET['frame_calendar'],text="- Select Date -",width=20,height=5,font=("helvatica",18))
    label_date.grid(row=0, column=0, padx=5, columnspan=3)

    # Calendar
    # cal = Calendar(TKINTER_WIDGET['frame_calendar'], selectmode='day', date_pattern='dd/mm/y', maxdate=datetime.datetime.today())
    # cal.grid(row=0, column=0, padx=20, pady=30, columnspan=3, sticky='s')

    # Entry calendar
    TKINTER_WIDGET['entry_date']= Entry(master=TKINTER_WIDGET['frame_calendar'],text="Calendar",width=15,font=fontjuan)
    TKINTER_WIDGET['entry_date'].grid(row=1,column=0,padx=15,pady=5,columnspan=3)

    # label Time
    label_time = Label(master = TKINTER_WIDGET['frame_calendar'], text = "Time:",width=7, height=5,font=("helvatica",14))
    label_time.grid(row=2,column=0,padx=10,pady=10)

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
    TKINTER_WIDGET['spinbox_hours'] = Spinbox(TKINTER_WIDGET['frame_calendar'], values= TKINTER_DATA['values_hours'],justify= CENTER,width=10,wrap = True)
    TKINTER_WIDGET['spinbox_hours'].grid(row =2,column=1,padx=10)
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
    TKINTER_WIDGET['spinbox_minutes'] = Spinbox(TKINTER_WIDGET['frame_calendar'], values= TKINTER_DATA['values_minutes'],justify= CENTER, width = 10, wrap = True)
    TKINTER_WIDGET['spinbox_minutes'].grid(row = 2,column = 2, padx =10)
    TKINTER_WIDGET['spinbox_minutes'].bind("<MouseWheel>",scroll_minutes)

    # TextVariable for Minutes 
    TKINTER_DATA['string_var_minutes'] = StringVar()
    
    # Button Select Date Time OK
    button_datetime_ok = custk.CTkButton(master = TKINTER_WIDGET['frame_calendar'],text="OK",width=70,command=update_datetime)
    button_datetime_ok.grid(row = 3,column=0,padx=60,pady=15,sticky='sw',columnspan=3)

    # Button Select Date Time Cancel
    button_datetime_cancel = custk.CTkButton(master = TKINTER_WIDGET['frame_calendar'],text = "Cancel",fg_color="gray74",hover_color="#EEE",text_color="#000",width =70,command = post_top_level_select_datetime)
    button_datetime_cancel.grid(row = 3,column= 0,padx=60,pady=15,sticky='se',columnspan=3)

def button_click(value):
    global TKINTER_DATA
    if value == 1:
        TKINTER_DATA['select_start_or_end']=1
        calen()
    else:
        TKINTER_DATA['select_start_or_end']=0
        calen()

def post_top_level_select_datetime():
    global TKINTER_WIDGET
    TKINTER_WIDGET['frame_calendar'].grid_forget()
    # TKINTER_WIDGET['widget_Date'].destroy()

def update_datetime():
    global TKINTER_DATA
    global TKINTER_WIDGET

    new_date = TKINTER_WIDGET['entry_date'].get()
    new_time = f"{new_date} {TKINTER_WIDGET['spinbox_hours'].get()}:{TKINTER_WIDGET['spinbox_minutes'].get()}"

    # Destroy widget_Date
    post_top_level_select_datetime()    

    # Update Button Start Time or End Time
    if TKINTER_DATA['select_start_or_end']==0:
        TKINTER_WIDGET['button_start_time'].configure(text=new_time)
    else:
        TKINTER_WIDGET['button_end_time'].configure(text=new_time)

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

def get_data(tree):
    global TKINTER_WIDGET
    global TKINTER_DATA
    #values= ['entry_category','entry_source_name','button_start_time','button_end_time','entry_event_id','combobox_event_type','combobox_send_to','entry_your_email']
    TKINTER_DATA['filterList']=[]

    #0
    # Lấy giá trị từ entry_event_category
    event_category = TKINTER_WIDGET['entry_event_category'].get()
    if event_category:
        TKINTER_DATA['filterList'].append(event_category)
    else:
        TKINTER_DATA['filterList'].append('')
    
    #1
    # Lấy giá trị từ entry_source_name
    source_name = TKINTER_WIDGET['entry_source_name'].get()
    if source_name:
        TKINTER_DATA['filterList'].append(source_name)
    else:
        TKINTER_DATA['filterList'].append('')
    
    #2
    # Lấy giá trị từ button_start_time
    start_time = TKINTER_WIDGET['button_start_time'].cget('text')
    if start_time:
        TKINTER_DATA['filterList'].append(start_time)
    else:
        TKINTER_DATA['filterList'].append('')
    
    #3
    # Lấy giá trị từ button_end_time
    end_time = TKINTER_WIDGET['button_end_time'].cget('text')
    if end_time:
        TKINTER_DATA['filterList'].append(end_time)
    else:
        TKINTER_DATA['filterList'].append('')
    
    #4
    # Lấy giá trị từ entry_event_id
    event_id = TKINTER_WIDGET['entry_event_id'].get()
    if event_id:
        TKINTER_DATA['filterList'].append(event_id)
    else:
        TKINTER_DATA['filterList'].append('')
    
    #5
    # Lấy giá trị từ combobox_event_type
    event_type = TKINTER_WIDGET['combobox_event_type'].get()
    if event_type:
        TKINTER_DATA['filterList'].append(event_type)
    else:
        TKINTER_DATA['filterList'].append('')
    
    #6
    # Lấy giá trị từ combobox_send_to
    send_to = TKINTER_WIDGET['combobox_send_to'].get()
    if send_to:
        TKINTER_DATA['filterList'].append(send_to)
    else:
        TKINTER_DATA['filterList'].append('')
    
    #7
    # Lấy giá trị từ entry_your_email
    your_email = TKINTER_WIDGET['entry_your_email'].get()
    if your_email:
        TKINTER_DATA['filterList'].append(your_email)
    else:
        TKINTER_DATA['filterList'].append('')
    # print(TKINTER_DATA['filterList'])
    logs = query(TKINTER_DATA['filterList'][0],'','','','',TKINTER_DATA['filterList'][1],TKINTER_DATA['filterList'][4],TKINTER_DATA['filterList'][5],'')
    print(logs)
    clear_tree(tree)
    for log in logs:
        inserttuple(log,tree)
    TKINTER_WIDGET['af'].destroy()

def openAddFilterWindow(tree):
    global TKINTER_WIDGET
    global TKINTER_DATA
    
    TKINTER_WIDGET['af'] = Toplevel()
    TKINTER_WIDGET['af'].title("ADD FILTER")
    TKINTER_WIDGET['af'].maxsize(1000,1000)
    TKINTER_WIDGET['af'].configure(bg="gray49")
    
    frame1 = Frame(TKINTER_WIDGET['af'],width=400,height=600)
    frame1.grid(row=0,column=0)
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
    TKINTER_WIDGET['button_start_time']=custk.CTkButton(master=frame1,fg_color="black",hover_color="white",text_color="#00BC8C",border_color="#00BC8C",text=current_datetime,command=lambda: button_click(0))
    TKINTER_WIDGET['button_start_time'].grid(row=2,column=1,padx=5,pady=10)

    # Label and entry end time
    TKINTER_WIDGET['label_end_time']=custk.CTkLabel(master=frame1,text="End Date",font=fontjuan,corner_radius=7)
    TKINTER_WIDGET['label_end_time'].grid(row=3,column=0,padx=5,pady=5)

    TKINTER_WIDGET['button_end_time']=custk.CTkButton(master=frame1,fg_color="black",hover_color="white",text_color="#00BC8C",border_color="#00BC8C",text=current_datetime,command=lambda: button_click(1))
    TKINTER_WIDGET['button_end_time'].grid(row=3,column=1,padx=5,pady=10)

    # Label and entry Event ID
    TKINTER_WIDGET['label_event_id']=custk.CTkLabel(master=frame1,text="Event ID",font=fontjuan,corner_radius=7)
    TKINTER_WIDGET['label_event_id'].grid(row=4,column=0,padx=5,pady=5)

    TKINTER_WIDGET['entry_event_id']=tb.Entry(frame1,font=fontjuan,width=15)
    TKINTER_WIDGET['entry_event_id'].grid(row=4,column=1,pady=5,padx=10)

    # Label and combobox event type
    TKINTER_WIDGET['label_event_type']=custk.CTkLabel(master=frame1,text="Event Type",font=fontjuan,corner_radius=7)
    TKINTER_WIDGET['label_event_type'].grid(row=5,column=0,padx=5,pady=5)

    TKINTER_WIDGET['combobox_event_type']=custk.CTkComboBox(master=frame1,corner_radius=10,values = ("","Information","Warning","Error","Audit Success","Audit Failure","Unknown"))        
    TKINTER_WIDGET['combobox_event_type'].grid(row=5,column=1,pady=5,padx=10)

    # Label and combobox send to
    TKINTER_WIDGET['label_send_to']=custk.CTkLabel(master=frame1,text="Send to",font=fontjuan,corner_radius=7)
    TKINTER_WIDGET['label_send_to'].grid(row=6,column=0,padx=5,pady=5)

    TKINTER_WIDGET['combobox_send_to']=custk.CTkComboBox(master=frame1,corner_radius=10,values=("","MSTeams","Email"))
    TKINTER_WIDGET['combobox_send_to'].grid(row=6,column=1,pady=5,padx=10)

    # Label and entry your email
    TKINTER_WIDGET['label_your_email']=custk.CTkLabel(master=frame1,text="Your Email",font=fontjuan,corner_radius=7)
    TKINTER_WIDGET['label_your_email'].grid(row=7,column=0,pady=5,padx=5)

    TKINTER_WIDGET['entry_your_email']=tb.Entry(frame1,font=fontjuan,width=15)
    TKINTER_WIDGET['entry_your_email'].grid(row=7,column=1,pady=5,padx=10)

    # Button filter
    TKINTER_WIDGET['button_filter']=custk.CTkButton(master=TKINTER_WIDGET['af'],text="Extract",width=70,command=lambda:get_data(tree))
    TKINTER_WIDGET['button_filter'].grid(row=1,column=0,padx=10,pady=15)