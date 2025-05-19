from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, DevOps world! If you see this, your CI/CD works!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
