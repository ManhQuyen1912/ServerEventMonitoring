import win32evtlog

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
