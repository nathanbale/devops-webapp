from flask import Flask
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'fallback-secret-key')


@app.route('/')
def home():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Hello, staging environment! CI/CD is working!!! Current time: {now}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')






