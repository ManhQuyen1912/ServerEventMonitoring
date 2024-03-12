import win32evtlog
import datetime

def evtTypeToString(record):
    if record.EventType == win32evtlog.EVENTLOG_ERROR_TYPE:
        return 'Error'
    elif record.EventType == win32evtlog.EVENTLOG_WARNING_TYPE:
        return 'Warning'
    elif record.EventType == win32evtlog.EVENTLOG_INFORMATION_TYPE:
        return 'Information'
    elif record.EventType == win32evtlog.EVENTLOG_AUDIT_SUCCESS:
        return 'Audit Success'
    elif record.EventType == win32evtlog.EVENTLOG_AUDIT_FAILURE:
        return 'Audit Failure'
    else:
        return 'Unknown'
    
def evtCtgrToString(record):
    if record.EventCategory == 0:
        return 'None'
    elif record.EventCategory == 1:
        return 'Device Driver'
    elif record.EventCategory == 2:
        return 'Service'
    elif record.EventCategory == 3:
        return 'File System'
    elif record.EventCategory == 4:
        return 'Object Access'
    elif record.EventCategory == 5:
        return 'Registry'
    elif record.EventCategory == 6:
        return 'Kernel'
    elif record.EventCategory == 7:
        return 'Process'
    elif record.EventCategory == 8:
        return 'Security'
    elif record.EventCategory == 9:
        return 'System'
    elif record.EventCategory == 10:
        return 'Printer'
    elif record.EventCategory == 11:
        return 'Initialization'
    elif record.EventCategory == 12:
        return 'Service Control Manager'
    elif record.EventCategory == 13:
        return 'Directory Service Access'
    elif record.EventCategory == 14:
        return 'Directory Service Changes'
    elif record.EventCategory == 15:
        return 'Kerberos'
    elif record.EventCategory == 16:
        return 'Active Directory'
    elif record.EventCategory == 17:
        return 'Account Logon'
    elif record.EventCategory == 18:
        return 'Account Management'
    elif record.EventCategory == 19:
        return 'Policy Change'
    elif record.EventCategory == 20:
        return 'Object Access'
    elif record.EventCategory == 21:
        return 'Privilege Use'
    elif record.EventCategory == 22:
        return 'Detailed Tracking'
    elif record.EventCategory == 23:
        return 'Logon/Logoff'
    elif record.EventCategory == 24:
        return 'System'
    elif record.EventCategory >= 25:
        return 'Miscellaneous'
def printRecord(record):
    print('Event Category:', record.EventCategory)
    print('Time Generated:', record.TimeGenerated)
    print('Source Name:', record.SourceName)
    print('Event ID:', record.EventID)
    print('Event Type:', evtTypeToString(record))
    print('Event Strings:', record.StringInserts)
    print()

def recordToStr(record):
    category = evtCtgrToString(record)
    time = str(record.TimeGenerated)
    source = record.SourceName
    eventID = str(record.EventID)
    eventType = evtTypeToString(record)
    eventStrings = str(record.StringInserts)

    res = category + '\t\t\t' + time + '\t\t' + source + '\t\t' + eventID + '\t' + eventType + '\t\t' + eventStrings + '\n'
    return res

def logRecord(record):
    #settings
    timezone = datetime.timezone(datetime.timedelta(hours=7))
    directory = 'logs/'

    currdate = datetime.datetime.now(timezone)

    filename = 'log_' + currdate.strftime('%m-%Y') + '.txt'

    with open(directory + filename, 'a') as file:
        #if file is empty, write header
        if file.tell() == 0:
            #header
            file.write('Event Category\tTime Generated\t\t\tSource Name\t\t\t\t\tEvent ID\tEvent Type\t\tEvent Strings\n')

        #write record
        file.write(recordToStr(record))
        #close
        file.close()

