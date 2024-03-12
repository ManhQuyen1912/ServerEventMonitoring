import threading
from flask import Flask, request, jsonify
import winEvtMonitor
from blueprint import bp

#flask app
app = Flask(__name__)
app.register_blueprint(bp)
#function to run the thread
def run_flask():
    app.run()

def run_monitor():
    winEvtMonitor.winEvtMonitor()

#run the thread
if __name__ == '__main__':
    t2 = threading.Thread(target=run_monitor).start()
    t1 = threading.Thread(target=run_flask).start()
    

