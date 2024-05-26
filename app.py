from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

# Import database models with app context
with app.app_context():
    from models import *
migrate = Migrate(app, db)

from routes import *

if __name__ == "__main__":
    app.logger.info("Starting app")
    app.run(debug=True)
