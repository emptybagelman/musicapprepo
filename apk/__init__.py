from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.json_provider_class.sort_keys = False # organise json in provided order, not sorted
CORS(app)
                                                # \/ add "ql" to end of postgres
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URL']

db = SQLAlchemy(app)