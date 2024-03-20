from filter import addFilter
from table import insert

def addFilterInterface(evtCategory, dateStart, dateEnd, timeStart, timeEnd, sourceName, evtID, evtType, action):
    addFilter(evtCategory, dateStart, dateEnd, timeStart, timeEnd, sourceName, evtID, evtType, action)
    return

def searchRcInterface(evtCategory, dateStart, dateEnd, timeStart, timeEnd, sourceName, evtID, evtType, action):
    res = search(evtCategory, dateStart, dateEnd, timeStart, timeEnd, sourceName, evtID, evtType, action)
    for record in res:
        insert(record)
    return