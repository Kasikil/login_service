from flask import Flask
from config import Config

app = Flask(__name__)

from app import routes

if __name__ == '__main__':
    app.run(debug=True)