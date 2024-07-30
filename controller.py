from filter import addFilter
from table import insert
from SqlService import backup_filter
from util import search

def addFilterInterface(evtCategory, dateStart, dateEnd, timeStart, timeEnd, sourceName, evtID, evtType, action):
    addFilter(evtCategory, dateStart, dateEnd, timeStart, timeEnd, sourceName, evtID, evtType, action)
    backup_filter([evtCategory, dateStart, dateEnd, timeStart, timeEnd, sourceName, evtID, evtType, action])
    return

def searchRcInterface(evtCategory, dateStart, dateEnd, timeStart, timeEnd, sourceName, evtID, evtType, action):
    res = search(evtCategory, dateStart, dateEnd, timeStart, timeEnd, sourceName, evtID, evtType, action)
    for record in res:
        print(record)
        insert(record)
    return