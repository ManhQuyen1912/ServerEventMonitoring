import threading
from flask import Flask, request, jsonify
import subprocess
import winEvtMonitor
import Configuration
import os

#flask app
app = Flask(__name__)
#function to run the thread
def run_flask():
    app.run()

def run_monitor():
    winEvtMonitor.winEvtMonitor()

def main():
    # Check if necessary files exist
    files_to_check = ['app.py', 'SqlService.py']
    base_path = 'D:\\HPT\\ServerWinEvtLg\\serverWinEvtLg\\'
    for file in files_to_check:
        file_path = os.path.join(base_path, file)
        if not os.path.exists(file_path):
            print(f"File {file} does not exist at path {file_path}")
            return
    # config load
    monitorThread = threading.Thread(target=run_monitor).start()
    flaskThread = threading.Thread(target=run_flask).start()
    UI = subprocess.Popen(['python', os.path.join(base_path, 'app.py')])
    db = subprocess.Popen(['python', os.path.join(base_path, 'SqlService.py')])

if __name__ == "__main__":
    main()