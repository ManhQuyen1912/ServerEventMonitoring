import mysql.connector
from mysql.connector import errorcode
import util
from filter import addFilter
import Configuration
import json

fileConfig = Configuration.Configuration()

config = fileConfig.get_all('DATABASE')
# jsonize the config
config = {key: value for key, value in config.items()}
config['raise_on_warnings'] = bool(config['raise_on_warnings'])

# user=fileConfig.get_user()
# print(user)

databaseConfig = fileConfig.get_all('TABLENAME')

columnConfig = fileConfig.get_all('COLUMNNAME')
#jsonize the config
columnConfig = {key: value for key, value in columnConfig.items()}
# jsonize items inside
columnConfig['eventtable'] = json.loads(columnConfig['eventtable'].replace("'", '"'))
columnConfig['filtertable'] = json.loads(columnConfig['filtertable'].replace("'", '"'))

def loadFilter():
    queryStr = ("SELECT * FROM " + databaseConfig['filtertable'])
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
  # queryStr = ("SELECT * FROM " + databaseConfig['eventtable'] + 
  #             " WHERE " + columnConfig['eventtable']['Category'] + " = " + evtCategory +
  #             " AND " + columnConfig['eventtable']['Time generated'] + " BETWEEN " + dateStart + " AND " + dateEnd +
  #             " AND " + columnConfig['eventtable']['Source name'] + " = " + sourceName +
  #             " AND " + columnConfig['eventtable']['evntID'] + " = " + evtID +
  #             " AND " + columnConfig['eventtable']['Type'] + " = " + evtType)
  # cursor.execute(queryStr)
  # return cursor.fetchall()
  queryStr = "SELECT * FROM " + databaseConfig['eventtable'] + " WHERE "

  if dateStart == "" or dateEnd == "":
    dateStart = None
    dateEnd = None
  if timeStart == "" or timeEnd == "":
    timeStart = None
    timeEnd = None
    # Build WHERE clause dynamically based on non-empty arguments
  conditions = []
  if evtCategory != "":
    conditions.append(columnConfig['eventtable']['Category'] + " = '" + evtCategory + "'")
  if dateStart is not None:
    conditions.append(columnConfig['eventtable']['Time generated'] + " >= '" + dateStart + "'")
  if dateEnd is not None:
    conditions.append(columnConfig['eventtable']['Time generated'] + " <= '" + dateEnd + "'")
  if timeStart is not None:
    conditions.append(columnConfig['eventtable']['Time generated'] + " LIKE '" + timeStart + "%'")  # Handle partial time matches
  if timeEnd is not None:
    conditions.append(columnConfig['eventtable']['Time generated'] + " LIKE '%" + timeEnd + "'")  # Handle partial time matches
  if sourceName != "":
    conditions.append(columnConfig['eventtable']['Source name'] + " = '" + sourceName + "'")
  if evtID != "":
    conditions.append(columnConfig['eventtable']['evntID'] + " = '" + evtID + "'")
  if evtType != "":
    conditions.append(columnConfig['eventtable']['Type'] + " = '" + evtType + "'")

  # Add conditions to the WHERE clause
  if conditions:
    queryStr += " AND ".join(conditions)
  else:
    queryStr = queryStr[:-6]  # Remove trailing " WHERE " if no conditions

  # print(queryStr)
  cursor.execute(queryStr)
  # print(cursor.fetchall())
  return cursor.fetchall()

def insert(record):
  add_record = ("INSERT INTO " + databaseConfig['eventtable'] + " "
               "(" + columnConfig['eventtable']['id'] + ", " + columnConfig['eventtable']['Category'] + ", " + columnConfig['eventtable']['Time generated'] + ", " + columnConfig['eventtable']['Source name'] + ", " + columnConfig['eventtable']['evntID'] + ", " + columnConfig['eventtable']['Type'] + ", " + columnConfig['eventtable']['Strings'] + ") "
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")
  # use the current number of record in database as id
  getNumRecord = ("SELECT COUNT(*) FROM " + databaseConfig['eventtable'])
  cursor.execute(getNumRecord)
  id = str(cursor.fetchone()[0] + 1)

  category = util.evtCtgrToString(record)
  time = str(record.TimeGenerated)
  source = record.SourceName
  eventID = str(record.EventID)
  eventType = util.evtTypeToString(record)
  eventStrings = str(record.StringInserts)
  
  data_record = (id, category, time, source, eventID, eventType, eventStrings)
  # print(data_record)
  cursor.execute(add_record, data_record)
  cnx.commit()

def backup_filter(filter):
    add_record = ("INSERT INTO " + databaseConfig['filtertable'] + " "
                "(" + columnConfig['filtertable']['id'] + ", " + columnConfig['filtertable']['Category'] + ", " + columnConfig['filtertable']['dateStart'] + ", " + columnConfig['filtertable']['dateEnd'] + ", " + columnConfig['filtertable']['timeStart'] + ", " + columnConfig['filtertable']['timeEnd'] + ", " + columnConfig['filtertable']['sourceName'] + ", " + columnConfig['filtertable']['evtID'] + ", " + columnConfig['filtertable']['evtType'] + ", " + columnConfig['filtertable']['action'] + ") "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    # use the current number of record in database as id
    getNumRecord = ("SELECT COUNT(*) FROM " + databaseConfig['filtertable'])
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

# cursor.close()
# cnx.close()
                  
                  