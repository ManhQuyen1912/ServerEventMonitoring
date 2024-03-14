import win32evtlog
import util
from filter import filter
from SqlService import insert

#setting
server = 'localhost'
logtype = 'System'
flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ


def winEvtMonitor():
    #open event log
    hand = win32evtlog.OpenEventLog(server, logtype)
    

    #notify change when total event log change
    prev = 0

    while True:
    
        total = win32evtlog.GetNumberOfEventLogRecords(hand)
        if total != prev:
            # update new handle
            hand = win32evtlog.OpenEventLog(server, logtype)
            # print new event
            event = win32evtlog.ReadEventLog(hand, flags, 0)[0]
            # util.printRecord(event)
            # util.logRecord(event)
            insert(event)
            filter(event)
            # update prev
            prev = total
        
    

    

