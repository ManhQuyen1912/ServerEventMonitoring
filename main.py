import threading
from flask import Flask, request, jsonify
import subprocess
import winEvtMonitor

#flask app
app = Flask(__name__)
#function to run the thread
def run_flask():
    app.run()

def run_monitor():
    winEvtMonitor.winEvtMonitor()

def main():
    t2 = threading.Thread(target=run_monitor).start()
    t1 = threading.Thread(target=run_flask).start()
    UI = subprocess.Popen(['python', 'app.py'])
    
if __name__ == "__main__":
    main()