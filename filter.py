import win32evtlog
import util
import datetime

annouceFilterList = [[]]


def addFilter(evtCategory, dateStart, dateEnd, timeStart, timeEnd, sourceName, evtID, evtType, action):
    annouceFilterList.append([evtCategory, dateStart, dateEnd, timeStart, timeEnd, sourceName, evtID, evtType, action])

def timeLimitCheck(timeRecord, dateStart, dateEnd, timeStart, timeEnd):
    timeRC = datetime.strptime(timeRecord, "%Y-%m-%d %H:%M:%S")
    dateRc = timeRC.date()
    timeRc = timeRC.time()


    if dateStart != '':
        dateStart = datetime.strptime(dateStart, "%Y-%m-%d")
    else:
        dateStart = datetime.strptime("1970-01-01", "%Y-%m-%d")
    
    if dateEnd != '':
        dateEnd = datetime.strptime(dateEnd, "%Y-%m-%d")
    else:
        dateEnd = datetime.strptime("9999-12-31", "%Y-%m-%d")

    if timeStart != '':
        timeStart = datetime.strptime(timeStart, "%H:%M:%S")
    else:
        timeStart = datetime.strptime("00:00:00", "%H:%M:%S")
    
    if timeEnd != '':
        timeEnd = datetime.strptime(timeEnd, "%H:%M:%S")
    else:
        timeEnd = datetime.strptime("23:59:59", "%H:%M:%S")

    # check all condition
    if dateRc >= dateStart and dateRc <= dateEnd and timeRc >= timeStart and timeRc <= timeEnd:
        return True
    else:
        return False
    

def filter(record):
    # print(annouceFilterList)
    for filter in annouceFilterList:
        if filter == []: continue
        if record.EventCategory == filter[0]:
            if timeLimitCheck(record.TimeGenerated, filter[1], filter[2], filter[3], filter[4]):
                if record.SourceName == filter[5]:
                    if record.EventID == filter[6]:
                        if util.evtTypeToString(record) == filter[7]:
                            doAction(filter[8])
    return
        

def doAction(action):
    if action == "log":
        print("Log")
    elif action == "email":
        print("Email")
    elif action == "sms":
        print("SMS")
    else:
        print("Invalid action")

