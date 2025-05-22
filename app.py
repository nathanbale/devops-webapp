from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Hello, staging environment! CI/CD is working!!! Current time: {now}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')






