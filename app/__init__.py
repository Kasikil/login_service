from database_config import DatabaseConfig
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from config import Config

app = Flask(__name__)
app.config.from_object(DatabaseConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

if __name__ == '__main__':
    app.run(debug=True)
