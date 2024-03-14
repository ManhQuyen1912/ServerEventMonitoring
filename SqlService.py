import mysql.connector
from mysql.connector import errorcode
import win32evtlog
import util

config = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'database': 'hpt-winevntmnt',
    'raise_on_warnings': True
}

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

def query():
  return

def insert(record):
  add_record = ("INSERT INTO events "
               "(idEvents, Category, `Time generated`, `Source name`, ID, Type, Strings) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")
  # use the current number of record in database as id
  getNumRecord = ("SELECT COUNT(*) FROM events")
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