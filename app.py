# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hi varshid welocome to kubernates!'

if __name__ == '__main__':
    # Use the host 0.0.0.0 to make the app accessible externally
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

