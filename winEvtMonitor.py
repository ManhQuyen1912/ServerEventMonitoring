import win32evtlog
import util
from filter import filter
from SqlService import insert, fileConfig

#setting
config = fileConfig.get_all('SYSTEM')
config = {key: value for key, value in config.items()}
flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ

EVENT_TYPE_MAP = {
    1: "Error",
    2: "Warning",
    4: "Information",
    8: "Success Audit",
    16: "Failure Audit"
}

# Mapping event categories, this may vary based on the event source
CATEGORY_MAP = {
    0: "None",
    1: "Application",
    2: "System",
    3: "Security",
    4: "Setup"
}

def fetch_all_logs():
    # Open event log
    hand = win32evtlog.OpenEventLog(config['server'], config['logtype'])
    logs = []
    count =0

    while True:
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        if events:
            for event in events:
                if count != 100:
                    event_type_str = EVENT_TYPE_MAP.get(event.EventType, f"Unknown ({event.EventType})")
                    event_category_str = CATEGORY_MAP.get(event.EventCategory, f"Unknown ({event.EventCategory})")
                    event_dict = {
                        "Source Name": event.SourceName,
                        "Event ID": event.EventID,
                        "Event Type": event_type_str,
                        "Time Generated": event.TimeGenerated.Format(),
                        "Category": event_category_str,
                        "Strings": event.StringInserts
                    }
                    log_entry = f"{event_dict['Category']}\t{event_dict['Source Name']}\t{event_dict['Time Generated']}\t{event_dict['Event ID']}\t{event_dict['Event Type']}\t{event_dict['Strings']}"
                    logs.append(log_entry)
                    insert(event)
                    filter(event)
                    count = count +1
                else:
                    break
        else:
            break
    win32evtlog.CloseEventLog(hand)
    return logs

def winEvtMonitor(callback):
    #open event log
    hand = win32evtlog.OpenEventLog(config['server'], config['logtype'])

    #notify change when total event log change
    prev = 0

    while True:
        total = win32evtlog.GetNumberOfEventLogRecords(hand)
        if total != prev:
            # New events have been added
            latest_record_number = total - 1  # Get the index of the latest event
            # Read only the latest event
            events = win32evtlog.ReadEventLog(hand, flags, latest_record_number, 1)
            
            if events:
                latest_event = events[0]
                event_dict = {
                    "Source Name": latest_event.SourceName,
                    "Event ID": latest_event.EventID,
                    "Event Type": latest_event.EventType,
                    "Time Generated": latest_event.TimeGenerated.Format(),
                    "Category": latest_event.EventCategory,
                    "Strings": latest_event.StringInserts
                }
                log_entry = f"{event_dict['Category']}\t{event_dict['Source Name']}\t{event_dict['Time Generated']}\t{event_dict['Event ID']}\t{event_dict['Event Type']}\t{event_dict['Strings']}"
                callback(log_entry)
            insert(events[0])
            print("New event added")
            filter(events[0])
            # update prev
            prev = total
        
    

    

