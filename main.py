import threading
from flask import Flask, request, jsonify
import subprocess
import winEvtMonitor
import Configuration

#flask app
app = Flask(__name__)
#function to run the thread
def run_flask():
    app.run()

def run_monitor():
    winEvtMonitor.winEvtMonitor()


def main():
    # config load
    monitorThread = threading.Thread(target=run_monitor).start()
    flaskThread = threading.Thread(target=run_flask).start()
    UI = subprocess.Popen(['python', 'app.py'])
    db = subprocess.Popen(['python', 'SqlService.py'])

    
    
if __name__ == "__main__":
    main()