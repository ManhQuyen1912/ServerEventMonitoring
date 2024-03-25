import mysql.connector
from mysql.connector import errorcode
import win32evtlog
import util
from filter import addFilter

config = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'database': 'hpt-winevntmnt',
    'raise_on_warnings': True
}

databaseConfig = {
    'eventTable': 'events',
    'filterTable': 'filter_backup'
}

columnConfig = {
  'filterTable': {
      'id': 'idfilter_backup',
      'Category': 'evtCategory',
      'dateStart': 'dateStart',
      'dateEnd': 'dateEnd',
      'timeStart': 'timeStart',
      'timeEnd': 'timeEnd',
      'sourceName': 'sourceName',
      'evtID': 'evtID',
      'evtType': 'type',
      'action': 'Action'
  },
  'eventTable': {
      'id': 'idEvents',
      'Category': 'Category',
      'Time generated': '`Time generated`',
      'Source name': '`Source name`',
      'evntID': 'ID',
      'Type': 'Type',
      'Strings': 'Strings'
  }
           
}
def loadFilter():
    queryStr = ("SELECT * FROM " + databaseConfig['filterTable'])
    cursor.execute(queryStr)
    filters = cursor.fetchall()
    for filter in filters:
        addFilter(filter[1], filter[2], filter[3], filter[4], filter[5], filter[6], filter[7], filter[8], filter[9])
        


try:
  cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

cursor = cnx.cursor()
loadFilter()

def query(evtCategory, dateStart, dateEnd, timeStart, timeEnd, sourceName, evtID, evtType, action):
  queryStr = ("SELECT * FROM " + databaseConfig['eventTable'] + 
              " WHERE " + columnConfig['eventTable']['Category'] + " = " + evtCategory +
              " AND " + columnConfig['eventTable']['Time generated'] + " BETWEEN " + dateStart + " AND " + dateEnd +
              " AND " + columnConfig['eventTable']['Source name'] + " = " + sourceName +
              " AND " + columnConfig['eventTable']['evntID'] + " = " + evtID +
              " AND " + columnConfig['eventTable']['Type'] + " = " + evtType)
  cursor.execute(queryStr)
  return cursor.fetchall()

def insert(record):
  add_record = ("INSERT INTO " + databaseConfig['eventTable'] + " "
               "(" + columnConfig['eventTable']['id'] + ", " + columnConfig['eventTable']['Category'] + ", " + columnConfig['eventTable']['Time generated'] + ", " + columnConfig['eventTable']['Source name'] + ", " + columnConfig['eventTable']['evntID'] + ", " + columnConfig['eventTable']['Type'] + ", " + columnConfig['eventTable']['Strings'] + ") "
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")
  # use the current number of record in database as id
  getNumRecord = ("SELECT COUNT(*) FROM " + databaseConfig['eventTable'])
  cursor.execute(getNumRecord)
  id = str(cursor.fetchone()[0] + 1)

  category = util.evtCtgrToString(record)
  time = str(record.TimeGenerated)
  source = record.SourceName
  eventID = str(record.EventID)
  eventType = util.evtTypeToString(record)
  eventStrings = str(record.StringInserts)
  
  data_record = (id, category, time, source, eventID, eventType, eventStrings)
  cursor.execute(add_record, data_record)
  cnx.commit()

def backup_filter(filter):
    add_record = ("INSERT INTO " + databaseConfig['filterTable'] + " "
                "(" + columnConfig['filterTable']['id'] + ", " + columnConfig['filterTable']['Category'] + ", " + columnConfig['filterTable']['dateStart'] + ", " + columnConfig['filterTable']['dateEnd'] + ", " + columnConfig['filterTable']['timeStart'] + ", " + columnConfig['filterTable']['timeEnd'] + ", " + columnConfig['filterTable']['sourceName'] + ", " + columnConfig['filterTable']['evtID'] + ", " + columnConfig['filterTable']['evtType'] + ", " + columnConfig['filterTable']['action'] + ") "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    # use the current number of record in database as id
    getNumRecord = ("SELECT COUNT(*) FROM " + databaseConfig['filterTable'])
    cursor.execute(getNumRecord)
    id = str(cursor.fetchone()[0] + 1)

    category = filter[0]
    dateStart = filter[1]
    dateEnd = filter[2]
    timeStart = filter[3]
    timeEnd = filter[4]
    sourceName = filter[5]
    evtID = filter[6]
    evtType = filter[7]
    action = filter[8]

    data_record = (id, category, dateStart, dateEnd, timeStart, timeEnd, sourceName, evtID, evtType, action)
    cursor.execute(add_record, data_record)
    cnx.commit()


                  
                  