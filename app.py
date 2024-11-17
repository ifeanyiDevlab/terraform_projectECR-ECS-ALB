from flask import flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def server_time():
    return {"server_time": datetime.now().isoformat()}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
