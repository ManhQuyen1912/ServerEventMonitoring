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



    


def filter(record):
    print('announceFilterList' + annouceFilterList)
    # for filter in annouceFilterList:
    #     #TODO: finish filter condition
    #     if (filter[0] == record.EventCategory or filter[0]=='') and 1==1:
    #         return action(filter[5])
        

def action(action):
    if action == "log":
        print("Log")
    elif action == "email":
        print("Email")
    elif action == "sms":
        print("SMS")
    else:
        print("Invalid action")

# def searchRecord(filter):
