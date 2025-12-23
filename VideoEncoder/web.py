from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/health')
def health_check():
    return "OK", 200

def run():
    app.run(host='0.0.0.0', port=8080)

def start_web_server():
    server = Thread(target=run)
    server.daemon = True
    server.start()
