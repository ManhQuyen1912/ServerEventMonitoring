from filter import addFilter

def addFilterInterface(evtCategory, dateStart, dateEnd, timeStart, timeEnd, sourceName, evtID, evtType, action):
    addFilter(evtCategory, dateStart, dateEnd, timeStart, timeEnd, sourceName, evtID, evtType, action)
    return

def searchRcInterface():
    return