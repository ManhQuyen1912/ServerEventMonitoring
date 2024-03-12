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
    
def printRecord(record):
    print('Event Category:', record.EventCategory)
    print('Time Generated:', record.TimeGenerated)
    print('Source Name:', record.SourceName)
    print('Event ID:', record.EventID)
    print('Event Type:', evtTypeToString(record))
    print('Event Strings:', record.StringInserts)
    print()

def logRecord(record):
    #settings
    timezone = datetime.timezone(datetime.timedelta(hours=7))
    directory = 'logs/'

    currdate = datetime.datetime.now(timezone)

    filename = 'log_' + currdate.strftime('%m-%Y') + '.txt'

    with open(directory + filename, 'a') as file:
        file.write('Event Category: ' + str(record.EventCategory) + '\n')
        file.write('Time Generated: ' + str(record.TimeGenerated) + '\n')
        file.write('Source Name: ' + str(record.SourceName) + '\n')
        file.write('Event ID: ' + str(record.EventID) + '\n')
        file.write('Event Type: ' + evtTypeToString(record) + '\n')
        file.write('Event Strings: ' + str(record.StringInserts) + '\n\n')
        file.close()

        